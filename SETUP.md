# MX Workspace Setup

**Syncing workspace between laptop and desktop machines**

---

## First-Time Desktop Setup

**On your desktop machine:**

```bash
# Download and run setup script
curl -o setup-desktop.sh https://raw.githubusercontent.com/ddttom/mx-workspace/main/setup-desktop.sh
chmod +x setup-desktop.sh
./setup-desktop.sh
```

**Or clone first, then run:**

```bash
git clone https://github.com/ddttom/mx-workspace.git ~/clawd
cd ~/clawd
./setup-desktop.sh
```

The script will:
1. ✅ Clone the repository
2. 🔐 Guide you through copying secrets/
3. 📦 Install dependencies (neomutt, python3, gh)
4. 📧 Configure email (neomutt)
5. 📨 Send test email
6. 📬 Test inbox checking

---

## What's NOT in Git (Must Copy Manually)

**secrets/** folder contains sensitive data (gitignored):
- `mx-backup-codes.txt` - 2FA backup codes (required)
- `gmail-credentials.json` - Gmail API credentials (optional)
- `gmail-token.json` - Gmail API token (optional)

**~/.neomuttrc** - Email configuration (created by setup script)

**How to copy secrets from laptop:**

```bash
# Option 1: SCP (if SSH configured)
scp -r laptop:~/clawd/secrets/ ~/clawd/

# Option 2: Manual
# On laptop: zip ~/clawd/secrets/ and transfer
# On desktop: unzip to ~/clawd/secrets/
```

---

## Syncing Changes

### From Laptop to Desktop

**On laptop (after making changes):**
```bash
cd ~/clawd
git add .
git commit -m "Description of changes"
git push
```

**On desktop (to get updates):**
```bash
cd ~/clawd
git pull
```

### From Desktop to Laptop

**On desktop (after making changes):**
```bash
cd ~/clawd
git add .
git commit -m "Description of changes"
git push
```

**On laptop (to get updates):**
```bash
cd ~/clawd
git pull
```

---

## Daily Workflow

**Both machines stay synced via Git:**

1. Make changes on either machine
2. Commit: `git add . && git commit -m "message"`
3. Push: `git push`
4. On other machine: `git pull`

**Best practice:**
- Pull before starting work: `git pull`
- Push after finishing: `git add . && git commit && git push`

---

## Troubleshooting

### Email not working

```bash
# Test SMTP (sending)
echo "Test" | neomutt -s "Test" tom.cranstoun@gmail.com

# Test IMAP (reading)
python3 scripts/check-mx-inbox.py
```

### Git conflicts

```bash
# If you edited same file on both machines
git pull  # Will show conflict
# Edit files to resolve
git add .
git commit -m "Resolve conflict"
git push
```

### Secrets missing

Copy `secrets/` folder from laptop to desktop manually (not in git for security).

---

## Files Structure

```
~/clawd/
├── SOUL.md, MISSION.md, IDENTITY.md      # Who MX is
├── USER.md, TOOLS.md, AGENTS.md          # Configuration
├── HEARTBEAT.md, TODO.md, REPOSITORIES.md
├── memory/2026-01-28.md                  # Daily logs
├── scripts/
│   ├── check-mx-inbox.py                 # IMAP inbox checker
│   ├── check-gmail-api.py                # Gmail API alternative
│   └── setup-gmail-api.md
├── secrets/                              # NOT in git
│   └── mx-backup-codes.txt
└── setup-desktop.sh                      # This setup script
```

---

## Security Notes

- **secrets/** is gitignored (never committed)
- **~/.neomuttrc** contains password (chmod 600)
- **App password** stored in neomutt config (file-level security)
- **GitHub repo** is private (ddttom/mx-workspace)

---

Need help? Email mx.machine.experience@gmail.com (that's me!) ⚡
