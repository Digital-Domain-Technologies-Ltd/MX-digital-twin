# MX Deployment Guide

**Quick reference for deploying MX configuration to a new openclaw instance.**

## Package Location

```
/Users/tomcranstoun/clawd/mx-transfer/
```

## Distribution Options

### Option 1: GitHub Repository

**Create public repo:**
```bash
cd /Users/tomcranstoun/clawd/mx-transfer
git init
git add .
git commit -m "Initial MX transfer package v1.0"
gh repo create mx-config --public --source=. --push
```

**Share URL:**
```
https://github.com/ddttom/mx-config
```

**Others can clone:**
```bash
cd ~/clawd
git clone https://github.com/ddttom/mx-config .
```

### Option 2: Tarball Archive

**Create archive:**
```bash
cd /Users/tomcranstoun/clawd
tar -czf mx-transfer-v1.0.tar.gz mx-transfer/
```

**Share file:**
- Upload to website/cloud storage
- Email to recipients
- Copy directly to target machine

**Others can extract:**
```bash
cd ~/clawd
tar -xzf mx-transfer-v1.0.tar.gz
mv mx-transfer/* .
```

### Option 3: Direct Copy

**Via USB/external drive:**
```bash
cp -r /Users/tomcranstoun/clawd/mx-transfer /Volumes/USB/
```

**Via network:**
```bash
scp -r /Users/tomcranstoun/clawd/mx-transfer user@host:~/clawd/
```

## Deployment Checklist

### On Source Machine (You)
- [x] Package created in `/Users/tomcranstoun/clawd/mx-transfer/`
- [ ] Choose distribution method (GitHub/tarball/direct copy)
- [ ] Verify all files present (see MANIFEST.md)
- [ ] Test checksums: `shasum -a 256 *.md`
- [ ] Distribute package

### On Target Machine (Recipient)

**Pre-deployment:**
- [ ] Install openclaw (clawdbot binary)
- [ ] Create workspace: `mkdir -p ~/clawd`
- [ ] Optional tools: neomutt, gh, ollama

**Deployment:**
- [ ] Copy/clone package to `~/clawd/`
- [ ] Read README.md
- [ ] Follow SETUP.md instructions
- [ ] Customize USER.md (critical!)
- [ ] Customize TOOLS.md
- [ ] Configure HEARTBEAT.md
- [ ] Create memory/ directory

**Post-deployment:**
- [ ] Start openclaw: `clawdbot gateway start`
- [ ] Test first session: say "hello"
- [ ] Verify MX reads configuration files
- [ ] Check tone and personality correct
- [ ] Test memory file creation

## Recommended: Create GitHub Repo

**Why GitHub?**
- Easy to share via URL
- Version control included
- Can accept contributions/improvements
- Others can fork and customize
- Track issues/questions

**Create repo:**
```bash
cd /Users/tomcranstoun/clawd/mx-transfer
git init
git add .
git commit -m "MX transfer package v1.0 - openclaw configuration"
gh repo create mx-config --public --source=. --push
```

**Add description:**
```
MX (Machine eXperience) configuration for openclaw platform. 
Transfer personality and settings to new instances. 
Embodies Convergence Principle and Robot-First Web advocacy.
```

**Add topics:**
```
openclaw, clawdbot, ai-assistant, mx-community, robot-first-web
```

## Usage Example

**Recipient receives GitHub URL:**
```
https://github.com/ddttom/mx-config
```

**They clone and customize:**
```bash
# Install openclaw first
cd ~/clawd
git clone https://github.com/ddttom/mx-config .

# Customize
nano USER.md      # Add their context
nano TOOLS.md     # Add their setup
nano HEARTBEAT.md # Configure monitoring

# Start
clawdbot gateway start
```

## Maintenance

### Update Package
When you improve MX configuration:
```bash
cd /Users/tomcranstoun/clawd/mx-transfer
cp ~/clawd/SOUL.md .
cp ~/clawd/AGENTS.md .
# Update other files as needed
git add .
git commit -m "Update configuration v1.1"
git push
```

### Version Tagging
```bash
git tag -a v1.0 -m "Initial release"
git push origin v1.0
```

## Support

After deployment, recipients can:
- Open GitHub issues (if using repo)
- Email you directly
- Check openclaw docs: https://docs.openclaw.bot
- Join MX community: https://github.com/MX-Experience

---

**Package ready to deploy!** ✅

Choose your distribution method and share.

**"Design for machines. Benefit humans. Advance both."** ⚡
