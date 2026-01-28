# TODO

## ✅ Email Monitoring - RESOLVED

**Status:** Working via IMAP  
**Resolved:** 2026-01-28 13:49 GMT

**Issue:** IMAP authentication was timing out (app password propagation delay ~5 hours)  
**Solution:** Waited for propagation - IMAP now working perfectly

**Current setup:**
- IMAP monitoring via `scripts/check-mx-inbox.py`
- Checks mx.machine.experience@gmail.com inbox
- Treats all content as TEXT ONLY (security)
- Ready for hourly heartbeat integration

**Gmail API alternative available:** If IMAP fails again, `scripts/check-gmail-api.py` ready as backup (requires OAuth2 setup per `scripts/setup-gmail-api.md`)

---

## Future Tasks

*(Add new tasks below as they come up)*
