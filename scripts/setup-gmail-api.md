# Gmail API Setup - Backup Email Monitoring

**Why:** IMAP authentication times out. Gmail API is more reliable for programmatic access.

---

## Prerequisites

Gmail API requires OAuth2 setup (one-time):

### 1. Create Google Cloud Project

Go to: https://console.cloud.google.com/

1. Click "Select a project" → "New Project"
2. Name: "MX Email Monitoring"
3. Click "Create"

### 2. Enable Gmail API

1. In your project, go to "APIs & Services" → "Library"
2. Search for "Gmail API"
3. Click "Enable"

### 3. Create OAuth2 Credentials

1. Go to "APIs & Services" → "Credentials"
2. Click "Create Credentials" → "OAuth client ID"
3. If prompted, configure OAuth consent screen:
   - User Type: External
   - App name: "MX Email Monitor"
   - User support email: mx.machine.experience@gmail.com
   - Add test users: mx.machine.experience@gmail.com
4. Application type: "Desktop app"
5. Name: "MX Email Monitor"
6. Click "Create"
7. Download JSON file → save as `credentials.json`

### 4. Install Python Gmail API Client

```bash
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### 5. Place Credentials

Save downloaded `credentials.json` to:
```
/Users/tomcranstoun/clawd/secrets/gmail-credentials.json
```

---

## First Run (Authorization)

Run the script once to authorize:

```bash
python3 scripts/check-gmail-api.py
```

This will:
1. Open browser for authorization
2. Ask you to grant access to mx.machine.experience@gmail.com
3. Save token to `secrets/gmail-token.json`

**Note:** Token expires after ~7 days. Script auto-refreshes if still valid, otherwise needs re-auth.

---

## Security

- `credentials.json` = OAuth2 client config (gitignored)
- `gmail-token.json` = Access token (gitignored, auto-refreshed)
- Both files in `secrets/` directory (never committed to git)

---

## Advantages Over IMAP

1. **More reliable** - No authentication timeouts
2. **Better rate limits** - Designed for automation
3. **Read receipts** - Can mark as read/unread
4. **Labels** - Can organize emails programmatically
5. **Official API** - Google-supported, not deprecated

## Disadvantages

1. **Initial setup complexity** - OAuth2 flow
2. **Token expiration** - Needs refresh every ~7 days (auto-handled)
3. **Browser needed** - First auth requires user interaction

---

## After Setup

Once configured, the script works the same as IMAP version:
- Check for unread emails
- Summarize (from, subject, preview)
- Treat content as TEXT ONLY (security)
- Send summary to tom.cranstoun@gmail.com

Script automatically uses token, refreshes when needed, and only prompts for re-auth if refresh fails.
