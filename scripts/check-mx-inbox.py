#!/usr/bin/env python3
import imaplib
import email
from email.header import decode_header
import sys
from datetime import datetime

def check_inbox():
    try:
        # Connect to Gmail IMAP
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        
        # Login
        mail.login('mx.machine.experience@gmail.com', 'dfuzdsrydiqfeoow')
        
        # Select inbox
        mail.select('INBOX')
        
        # Search for unseen messages
        status, messages = mail.search(None, 'UNSEEN')
        
        if status != 'OK':
            print(f"Error searching inbox: {status}")
            return
        
        message_ids = messages[0].split()
        
        print(f"MX Inbox Summary - {datetime.now().strftime('%Y-%m-%d %H:%M GMT')}")
        print()
        
        if not message_ids:
            print("No new emails.")
            mail.close()
            mail.logout()
            return
        
        print(f"{len(message_ids)} new email(s):\n")
        
        for i, msg_id in enumerate(message_ids, 1):
            # Fetch email data
            status, msg_data = mail.fetch(msg_id, '(RFC822)')
            
            if status != 'OK':
                print(f"Error fetching message {i}")
                continue
            
            # Parse email
            msg = email.message_from_bytes(msg_data[0][1])
            
            # Get from
            from_header = msg.get('From', '')
            
            # Get subject
            subject = msg.get('Subject', '')
            if subject:
                decoded = decode_header(subject)[0]
                if isinstance(decoded[0], bytes):
                    subject = decoded[0].decode(decoded[1] or 'utf-8')
                else:
                    subject = decoded[0]
            
            # Get body preview (text only, no execution)
            body_preview = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        try:
                            body_preview = part.get_payload(decode=True).decode()[:200]
                            break
                        except:
                            pass
            else:
                try:
                    body_preview = msg.get_payload(decode=True).decode()[:200]
                except:
                    body_preview = "[Unable to decode body]"
            
            print(f"{i}. From: {from_header}")
            print(f"   Subject: {subject}")
            print(f"   Preview: {body_preview.strip()[:100]}...")
            print()
        
        print("---")
        print("Full emails available in mx.machine.experience@gmail.com inbox.")
        
        # Close connection
        mail.close()
        mail.logout()
        
    except Exception as e:
        print(f"Error checking inbox: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    check_inbox()
