#!/usr/bin/env python3
"""
Email triage and classification system for Tom's personal email.
Categorizes, filters adverts/puffery, and summarizes inbox.
"""

import imaplib
import email
from email.header import decode_header
from datetime import datetime
import re

# Spam/puffery patterns (marketing, newsletters, automated)
PUFFERY_PATTERNS = [
    r'unsubscribe',
    r'newsletter',
    r'promotional',
    r'marketing@',
    r'noreply@',
    r'no-reply@',
    r'promo',
    r'offer',
    r'sale',
    r'discount',
    r'deal',
    r'subscribe',
    r'notification@',
]

# Financial keywords
FINANCIAL_KEYWORDS = [
    'invoice', 'payment', 'bank', 'credit card', 'statement',
    'transaction', 'paypal', 'stripe', 'receipt', 'billing'
]

# Work/professional keywords
WORK_KEYWORDS = [
    'meeting', 'call', 'schedule', 'agenda', 'proposal',
    'contract', 'project', 'deadline', 'client', 'cms', 'aem', 'adobe'
]

# Urgent indicators
URGENT_KEYWORDS = [
    'urgent', 'asap', 'important', 'action required', 'immediate',
    'deadline', 'today', 'expires', 'expiring', 'final notice'
]

def decode_header_value(header):
    """Decode email header handling various encodings."""
    if not header:
        return ""
    
    decoded_parts = decode_header(header)
    result = []
    for part, encoding in decoded_parts:
        if isinstance(part, bytes):
            try:
                result.append(part.decode(encoding or 'utf-8', errors='ignore'))
            except:
                result.append(part.decode('utf-8', errors='ignore'))
        else:
            result.append(str(part))
    return ''.join(result)

def is_puffery(subject, from_header, body):
    """Detect marketing/newsletter/spam emails."""
    text = f"{subject} {from_header} {body}".lower()
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in PUFFERY_PATTERNS)

def classify_email(subject, from_header, body):
    """Classify email into categories."""
    text = f"{subject} {body}".lower()
    
    categories = []
    
    # Check urgency first
    if any(keyword in text for keyword in URGENT_KEYWORDS):
        categories.append('URGENT')
    
    # Check type
    if any(keyword in text for keyword in FINANCIAL_KEYWORDS):
        categories.append('Financial')
    
    if any(keyword in text for keyword in WORK_KEYWORDS):
        categories.append('Work')
    
    # Default to personal if no other category
    if not categories or categories == ['URGENT']:
        categories.append('Personal')
    
    return categories

def triage_email(subject, from_header, body):
    """Triage into action buckets."""
    categories = classify_email(subject, from_header, body)
    
    if 'URGENT' in categories:
        return 'ACTION REQUIRED'
    elif 'Financial' in categories:
        return 'REVIEW'
    elif 'Work' in categories:
        return 'ACTION NEEDED'
    else:
        return 'FYI'

def check_inbox(email_address, password, limit=20):
    """
    Check inbox and return triaged emails.
    Limit to recent emails to avoid overwhelming summaries.
    """
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(email_address, password)
        mail.select('INBOX')
        
        # Search for unseen messages
        status, messages = mail.search(None, 'UNSEEN')
        
        if status != 'OK':
            return None, "Search failed"
        
        email_ids = messages[0].split()
        
        if not email_ids:
            return [], None
        
        # Process most recent emails (limited to avoid overload)
        triaged_emails = []
        
        for email_id in email_ids[-limit:]:  # Most recent N emails
            status, msg_data = mail.fetch(email_id, '(RFC822)')
            
            if status != 'OK':
                continue
                
            msg = email.message_from_bytes(msg_data[0][1])
            
            # Decode headers
            subject = decode_header_value(msg['Subject'])
            from_header = decode_header_value(msg['From'])
            date_header = msg.get('Date', '')
            
            # Get body snippet
            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        try:
                            body = part.get_payload(decode=True).decode(errors='ignore')[:500]
                            break
                        except:
                            pass
            else:
                try:
                    body = msg.get_payload(decode=True).decode(errors='ignore')[:500]
                except:
                    body = ""
            
            # Skip puffery
            if is_puffery(subject, from_header, body):
                continue
            
            # Classify and triage
            categories = classify_email(subject, from_header, body)
            triage_bucket = triage_email(subject, from_header, body)
            
            triaged_emails.append({
                'from': from_header,
                'subject': subject,
                'date': date_header,
                'categories': categories,
                'triage': triage_bucket,
                'snippet': body[:150]
            })
        
        mail.close()
        mail.logout()
        
        # Sort by triage priority
        priority_order = {'ACTION REQUIRED': 0, 'ACTION NEEDED': 1, 'REVIEW': 2, 'FYI': 3}
        triaged_emails.sort(key=lambda x: priority_order.get(x['triage'], 99))
        
        return triaged_emails, None
        
    except Exception as e:
        return None, str(e)

if __name__ == '__main__':
    # Test with Tom's account
    emails, error = check_inbox('tom.cranstoun@gmail.com', 'ghompawbdiyiqbwx', limit=20)
    
    if error:
        print(f"ERROR: {error}")
    elif not emails:
        print("NO_NEW_EMAILS")
    else:
        print(f"Found {len(emails)} emails after filtering puffery:\n")
        for e in emails:
            print(f"[{e['triage']}] {' | '.join(e['categories'])}")
            print(f"From: {e['from']}")
            print(f"Subject: {e['subject']}")
            print(f"Snippet: {e['snippet'][:100]}...")
            print()
