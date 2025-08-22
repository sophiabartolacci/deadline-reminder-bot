# Notion Discord Bot

A bot that fetches tasks from a Notion database and sends daily to-do lists to Discord.

## Setup

1. Create Notion integration at [notion.so/my-integrations](https://www.notion.so/my-integrations)
2. Create Discord bot at [Discord Developer Portal](https://discord.com/developers/applications)
3. Copy `.env.example` to `.env` and fill in your tokens
4. Install dependencies: `pip install -r requirements.txt`
5. Run: `python bot.py`

## Environment Variables

- `NOTION_TOKEN` - Your Notion integration token
- `DATABASE_ID` - Your Notion database ID
- `DISCORD_TOKEN` - Your Discord bot token
- `CHANNEL_ID` - Discord channel ID to send messages

## Usage

- `python bot.py` - Send tasks once
- `python scheduler.py` - Run with daily scheduling