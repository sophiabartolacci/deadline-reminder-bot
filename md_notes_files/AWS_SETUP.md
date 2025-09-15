# AWS Setup Guide - Daily Deadline Bot

## Prerequisites
- AWS student account created
- AWS CLI installed (`brew install awscli`)

## IAM User Setup
1. **Create IAM User**
   - Name: `daily-deadline-service`
   - Access type: Programmatic access only
   - Permissions: AdministratorAccess (for development)

2. **Create Access Keys**
   - Use case: Command Line Interface (CLI)
   - Save Access Key ID and Secret Access Key securely

## AWS CLI Configuration
```bash
aws configure
```
- **Access Key ID**: [your-access-key-id]
- **Secret Access Key**: [your-secret-access-key]
- **Region**: us-east-1
- **Output**: json

## Verification
```bash
aws sts get-caller-identity
```
Should return ARN ending with `user/daily-deadline-service`

## Next Steps
- [ ] Create Lambda function
- [ ] Set up Parameter Store for secrets
- [ ] Configure EventBridge for daily scheduling
- [ ] Set up DynamoDB for multi-user support

## Security Notes
- Never commit AWS credentials to Git
- Store backup credentials in password manager
- Rotate access keys every 90 days
- Use least privilege permissions in production