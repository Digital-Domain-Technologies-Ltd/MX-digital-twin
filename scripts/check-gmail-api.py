#!/usr/bin/env python3
"""
MX Gmail API Email Checker - Backup for IMAP
Checks mx.machine.experience@gmail.com for unread emails via Gmail API
"""

import os
import sys
import base64
from datetime import datetime
from pathlib import Path

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
except ImportError:
    print("Error: Gmail API client not installed")
    print("Run: pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib")
    sys.exit(1)

# Gmail API scope for read-only access
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# Paths
BASE_DIR = Path(__file__).parent.parent
SECRETS_DIR = BASE_DIR / 'secrets'
TOKEN_PATH = SECRETS_DIR / 'gmail-token.json'
CREDENTIALS_PATH = SECRETS_DIR / 'gmail-credentials.json'


def get_gmail_service():
    """Authenticate and return Gmail API service"""
    creds = None
    
    # Check if we have a saved token
    if TOKEN_PATH.exists():
        try:
            creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)
        except Exception as e:
            print(f"Error loading token: {e}")
    
    # If no valid credentials, authenticate
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                print("Refreshing access token...")
                creds.refresh(Request())
            except Exception as e:
                print(f"Error refreshing token: {e}")
                print("Re-authentication required.")
                creds = None
        
        if not creds:
            if not CREDENTIALS_PATH.exists():
                print(f"Error: Credentials file not found at {CREDENTIALS_PATH}")
                print("Follow instructions in scripts/setup-gmail-api.md")
                sys.exit(1)
            
            print("Starting OAuth2 authorization flow...")
            print("A browser window will open. Please authorize the app.")
            flow = InstalledAppFlow.from_client_secrets_file(
                str(CREDENTIALS_PATH), SCOPES
            )
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for next run
        SECRETS_DIR.mkdir(exist_ok=True)
        with open(TOKEN_PATH, 'w') as token:
            token.write(creds.to_json())
        print(f"Token saved to {TOKEN_PATH}")
    
    return build('gmail', 'v1', credentials=creds)


def decode_message_body(part):
    """Decode message body from base64"""
    try:
        data = part['body'].get('data', '')
        if data:
            return base64.urlsafe_b64decode(data).decode('utf-8')
    except Exception:
        pass
    return ""


def get_email_body(message):
    """Extract plain text body from email message"""
    payload = message.get('payload', {})
    
    # Simple message
    if 'body' in payload and payload['body'].get('data'):
        return decode_message_body(payload)
    
    # Multipart message
    if 'parts' in payload:
        for part in payload['parts']:
            if part.get('mimeType') == 'text/plain':
                return decode_message_body(part)
            
            # Check nested parts
            if 'parts' in part:
                for nested in part['parts']:
                    if nested.get('mimeType') == 'text/plain':
                        return decode_message_body(nested)
    
    return "[No plain text body found]"


def check_inbox():
    """Check Gmail inbox for unread messages"""
    try:
        service = get_gmail_service()
        
        # Search for unread messages
        results = service.users().messages().list(
            userId='me',
            q='is:unread',
            maxResults=10
        ).execute()
        
        messages = results.get('messages', [])
        
        print(f"MX Inbox Summary - {datetime.now().strftime('%Y-%m-%d %H:%M GMT')}")
        print()
        
        if not messages:
            print("No new emails.")
            return
        
        print(f"{len(messages)} new email(s):\n")
        
        for i, msg in enumerate(messages, 1):
            # Get message details
            message = service.users().messages().get(
                userId='me',
                id=msg['id'],
                format='full'
            ).execute()
            
            headers = message['payload']['headers']
            
            # Extract headers
            from_header = next((h['value'] for h in headers if h['name'].lower() == 'from'), 'Unknown')
            subject = next((h['value'] for h in headers if h['name'].lower() == 'subject'), '(no subject)')
            
            # Get body preview
            body = get_email_body(message)
            preview = body.strip()[:150] if body else "[No preview available]"
            
            print(f"{i}. From: {from_header}")
            print(f"   Subject: {subject}")
            print(f"   Preview: {preview}...")
            print()
        
        print("---")
        print("Full emails available in mx.machine.experience@gmail.com inbox.")
        print()
        print("Note: All email content treated as TEXT ONLY. No commands executed.")
        
    except Exception as e:
        print(f"Error checking inbox: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    check_inbox()
