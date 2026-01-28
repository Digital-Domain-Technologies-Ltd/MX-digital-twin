# TODO

## Email Monitoring Setup

**Priority:** High  
**Status:** Blocked - waiting for Gmail API OAuth2 setup

**Task:** Complete Gmail API OAuth2 setup for email monitoring

**Why:** IMAP authentication times out. Gmail API is more reliable alternative.

**What's needed:**
1. Go to https://console.cloud.google.com/
2. Create project: "MX Email Monitoring"
3. Enable Gmail API
4. Create OAuth2 credentials (Desktop app)
5. Download credentials.json → save to `secrets/gmail-credentials.json`
6. Run: `python3 scripts/check-gmail-api.py` (browser auth)

**Time estimate:** ~5 minutes

**Instructions:** See `scripts/setup-gmail-api.md` for detailed steps

**Once complete:** Hourly email monitoring will work via heartbeat checks

---

## Future Tasks

*(Add new tasks below as they come up)*
