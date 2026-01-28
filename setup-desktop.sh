#!/bin/bash
# MX Workspace Setup for Desktop Machine
# Run this on your desktop to sync from laptop

set -e

echo "🚀 MX Workspace Desktop Setup"
echo "================================"
echo

# Configuration
WORKSPACE_DIR="$HOME/clawd"
LAPTOP_HOST=""  # Set this if copying secrets via SSH

# Step 1: Clone repository
echo "📦 Step 1: Clone mx-workspace repository"
if [ -d "$WORKSPACE_DIR" ]; then
    echo "⚠️  Directory $WORKSPACE_DIR already exists"
    read -p "Delete and re-clone? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf "$WORKSPACE_DIR"
    else
        echo "Keeping existing directory. Pulling latest changes..."
        cd "$WORKSPACE_DIR" && git pull
    fi
fi

if [ ! -d "$WORKSPACE_DIR" ]; then
    git clone https://github.com/ddttom/mx-workspace.git "$WORKSPACE_DIR"
    echo "✅ Repository cloned to $WORKSPACE_DIR"
else
    echo "✅ Repository updated"
fi

cd "$WORKSPACE_DIR"

# Step 2: Create secrets directory
echo
echo "🔐 Step 2: Setup secrets directory"
mkdir -p secrets

# Step 3: Copy or create secrets
echo
echo "📋 Step 3: Copy secrets from laptop"
echo
echo "You need to copy secrets/ from your laptop to this machine."
echo "Secrets are NOT in git (for security)."
echo
echo "Option 1 - Manual copy:"
echo "  On laptop: zip ~/clawd/secrets/"
echo "  Transfer the zip file to this machine"
echo "  Unzip to $WORKSPACE_DIR/secrets/"
echo
echo "Option 2 - SCP (if SSH is set up):"
echo "  scp -r laptop-machine:~/clawd/secrets/* $WORKSPACE_DIR/secrets/"
echo
echo "Required files in secrets/:"
echo "  - mx-backup-codes.txt (2FA backup codes)"
echo "  - (optional) gmail-credentials.json (if using Gmail API)"
echo "  - (optional) gmail-token.json (if using Gmail API)"
echo
read -p "Have you copied the secrets folder? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "⚠️  Setup paused. Copy secrets/ then re-run this script."
    exit 1
fi

# Check if secrets exist
if [ ! -f "secrets/mx-backup-codes.txt" ]; then
    echo "⚠️  Warning: secrets/mx-backup-codes.txt not found"
    echo "Make sure to copy the 2FA backup codes!"
fi

# Step 4: Install dependencies
echo
echo "📦 Step 4: Install dependencies"
echo
echo "Required software:"
echo "  - neomutt (email)"
echo "  - python3 (scripts)"
echo "  - gh (GitHub CLI - already authenticated)"
echo

# Detect OS and suggest install commands
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "macOS detected. Install with Homebrew:"
    echo "  brew install neomutt python3 gh"
    echo
    read -p "Install dependencies now? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        brew install neomutt python3 gh || echo "⚠️  Some installs failed. Install manually if needed."
    fi
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Linux detected. Install with your package manager:"
    echo "  sudo apt install neomutt python3 gh  # Debian/Ubuntu"
    echo "  sudo dnf install neomutt python3 gh  # Fedora"
fi

# Step 5: Configure neomutt
echo
echo "📧 Step 5: Configure neomutt"
echo

NEOMUTTRC="$HOME/.neomuttrc"
if [ -f "$NEOMUTTRC" ]; then
    echo "⚠️  $NEOMUTTRC already exists"
    read -p "Overwrite with MX configuration? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Keeping existing configuration."
        echo "⚠️  Make sure it has mx.machine.experience@gmail.com configured!"
        echo "Skipping neomutt setup..."
        SKIP_NEOMUTT=true
    fi
fi

if [ "$SKIP_NEOMUTT" != "true" ]; then
    echo "Creating neomutt configuration..."
    echo "You need the app-specific password for mx.machine.experience@gmail.com"
    echo
    echo "App password (16 chars, no spaces): dfuzdsrydiqfeoow"
    echo "(from mx.Machine.Experience created 8:47 AM)"
    echo
    
    cat > "$NEOMUTTRC" << 'EOF'
# MX Community Email - mx.machine.experience@gmail.com
set from = "mx.machine.experience@gmail.com"
set realname = "MX (Machine eXperience)"

# Gmail IMAP
set imap_user = "mx.machine.experience@gmail.com"
set imap_pass = "dfuzdsrydiqfeoow"
set folder = "imaps://imap.gmail.com:993"
set spoolfile = "+INBOX"
set postponed = "+[Gmail]/Drafts"
set trash = "+[Gmail]/Trash"

# Gmail SMTP  
set smtp_url = "smtp://mx.machine.experience@gmail.com@smtp.gmail.com:587/"
set smtp_pass = "dfuzdsrydiqfeoow"
set smtp_authenticators = "login"

# SSL/TLS
set ssl_force_tls = yes
set ssl_starttls = yes

# Cache for performance
set header_cache = "~/.cache/neomutt/headers"
set message_cachedir = "~/.cache/neomutt/bodies"

# Basic settings
set mail_check = 60
set timeout = 10
set sort = reverse-date-received

# Don't ask for confirmations
set delete = yes
set quit = yes
EOF
    
    chmod 600 "$NEOMUTTRC"
    mkdir -p ~/.cache/neomutt/{headers,bodies}
    echo "✅ Neomutt configured"
fi

# Step 6: Test email
echo
echo "📨 Step 6: Test email configuration"
echo
read -p "Send test email to tom.cranstoun@gmail.com? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "MX Workspace setup complete on $(hostname) at $(date)" | neomutt -F ~/.neomuttrc -s "MX Desktop Setup Complete" tom.cranstoun@gmail.com 2>&1
    if [ $? -eq 0 ]; then
        echo "✅ Test email sent successfully!"
    else
        echo "❌ Email send failed. Check neomutt configuration."
    fi
fi

# Step 7: Test IMAP
echo
echo "📬 Step 7: Test IMAP inbox checking"
echo
read -p "Test inbox checking? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    python3 scripts/check-mx-inbox.py || echo "❌ IMAP check failed"
fi

# Summary
echo
echo "================================"
echo "✅ Setup Complete!"
echo "================================"
echo
echo "Workspace: $WORKSPACE_DIR"
echo
echo "Next steps:"
echo "1. Verify secrets/ contains backup codes"
echo "2. Test: python3 scripts/check-mx-inbox.py"
echo "3. Check your email for test message"
echo
echo "To sync changes from laptop in future:"
echo "  cd $WORKSPACE_DIR && git pull"
echo
echo "To push changes from desktop:"
echo "  cd $WORKSPACE_DIR && git add . && git commit -m 'message' && git push"
echo
echo "MX workspace ready! ⚡"
