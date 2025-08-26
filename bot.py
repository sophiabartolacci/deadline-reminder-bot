from notion_client import AsyncClient
import os, datetime, discord, asyncio
from dotenv import load_dotenv

'''
    command to run the bot.py file: source venv/bin/activate && python bot.py
'''

# Setup
load_dotenv('.env')
notion = AsyncClient(auth=os.environ["NOTION_TOKEN"])
database_id = os.environ["NOTION_DATABASE_ID"]

intents = discord.Intents.default()
discord_client = discord.Client(intents=intents)

async def db_setup() -> dict:
    database = await notion.databases.retrieve(database_id)
    return database["properties"]

def get_three_days_out() -> datetime:
    today = datetime.date.today()
    three_days_out = today + datetime.timedelta(days=3)
    return three_days_out

async def filter_db() -> dict:
    three_days_out = get_three_days_out().isoformat()
    
    assignment_info = await notion.databases.query(
        database_id=database_id,
        filter={
            "and": [
                {
                    "property": "To Do",
                    "checkbox": {
                        "equals": False
                    }
                },
                {
                    "property": "Due Date",
                    "date": {
                        "is_not_empty": True
                    }
                },
                {
                    "property": "Due Date",
                    "date": {
                        "on_or_before": three_days_out
                    }
                }
            ]
        }
    )
    return assignment_info

def extract_assignment_info() -> list:
    assignment_info = asyncio.run(filter_db())
    all_assignments = []
    results = assignment_info["results"]
    for entry in results:
        assignment_name = entry['properties']['Assignment']['title'][0]['plain_text']
        assignment_class = entry['properties']['Class']['select']['name']
        assignment_type = entry['properties']['Type']['select']['name']
        assignment_due_date = entry['properties']['Due Date']['date']['start']
        notes_list = entry['properties']['Notes']['rich_text']
        
        # Check if notes_list is empty
        if not notes_list:  
            assignment_notes = "No notes"
        else:
            assignment_notes = notes_list[0]['plain_text']

        # Store all assignment information in a dictionary
        entry_info = {
            "name": assignment_name,
            "class": assignment_class,
            "type": assignment_type,
            "due_date": assignment_due_date,
            "notes": assignment_notes
        }

        # Add each entry to a list of all assignments
        all_assignments.append(entry_info)
    print(all_assignments)
    return all_assignments

def send_message():
    token = os.environ["DISCORD_TOKEN"]
    channel_id = int(os.environ["DISCORD_CHANNEL_ID"])
    
    client = discord.Client(intents=discord.Intents.default())
    
    @client.event
    async def on_ready():
        channel = client.get_channel(channel_id)
        await channel.send("Hello World!")
        await client.close()
    
    client.run(token)


if __name__ == "__main__":
    # send_message()
    # extract_assignment_info()
    