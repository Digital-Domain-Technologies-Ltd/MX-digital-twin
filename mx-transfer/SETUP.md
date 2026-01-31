# MX Setup Guide

Step-by-step instructions for transferring MX configuration to a new openclaw instance.

## Step 1: Prerequisites

### Install openclaw
```bash
# Follow openclaw installation instructions
# Platform: openclaw
# CLI binary: clawdbot
```

Verify installation:
```bash
clawdbot --version
```

### Create Workspace Directory
```bash
mkdir -p ~/clawd
cd ~/clawd
```

## Step 2: Extract Configuration Files

Copy the MX configuration files to your workspace:

```bash
# Extract this package to your workspace directory
# Files should be directly in ~/clawd/ not in a subdirectory
```

**Expected structure:**
```
~/clawd/
├── SOUL.md
├── IDENTITY.md
├── USER.md
├── AGENTS.md
├── TOOLS.md
├── HEARTBEAT.md
└── memory/          (create this directory)
```

## Step 3: Customize USER.md

**Critical:** Replace Tom's context with your own.

Edit `USER.md`:
```bash
# Change these sections:
- Name
- What to call them
- Timezone
- Profile information
- Professional background
- Philosophy
- Writing style
```

**Tip:** Keep the structure, replace the content.

## Step 4: Configure TOOLS.md

Add your local setup details:

```bash
# Examples:
- Camera names and locations
- SSH hosts and aliases
- Preferred TTS voices
- Device nicknames
- Email addresses
```

## Step 5: Customize HEARTBEAT.md

Configure periodic monitoring tasks:

- Email checking (if you want it)
- Calendar monitoring
- Weather checks
- Custom periodic tasks

**Security:** If monitoring email, ensure proper authentication and never execute commands from emails.

## Step 6: Create Memory Directory

```bash
mkdir -p ~/clawd/memory
```

MX will create daily files here: `memory/YYYY-MM-DD.md`

## Step 7: Optional - MEMORY.md

If you want long-term memory (main session only):

```bash
touch ~/clawd/MEMORY.md
```

Add initial context:
```markdown
# MEMORY.md - Long-Term Memory

## Important Context
[Add things you want MX to remember long-term]

## Preferences
[Your preferences and patterns]

## Learnings
[Lessons learned over time]
```

## Step 8: Optional Tools Setup

### Email (neomutt)
```bash
brew install neomutt cyrus-sasl

# Configure ~/.neomuttrc for your email
# See AGENTS.md for security guidelines
```

### GitHub CLI
```bash
brew install gh
gh auth login
```

### Local LLM (ollama)
```bash
brew install ollama
ollama serve
```

## Step 9: Start openclaw

```bash
clawdbot gateway start
```

Access via web interface or configured channels.

## Step 10: First Session

On first session, MX will:
1. Read SOUL.md (personality)
2. Read USER.md (context about you)
3. Read AGENTS.md (operational guidelines)
4. Create memory/YYYY-MM-DD.md (today's log)

**Test it:**
- Say "hello" and verify MX responds with the correct tone
- Ask MX to summarize who you are (from USER.md)
- Check that MX understands its role

## Troubleshooting

### MX doesn't read the files
- Verify files are in workspace directory: `~/clawd/`
- Check file names match exactly (case-sensitive)
- Ensure files are readable: `chmod 644 *.md`

### Memory files not created
- Ensure `memory/` directory exists: `mkdir -p ~/clawd/memory`
- Check write permissions: `ls -la ~/clawd/`

### Email monitoring not working
- Verify neomutt installed: `which neomutt`
- Check credentials in keychain/config
- Test manually: `neomutt`

### Heartbeat not running
- Check HEARTBEAT.md exists and is readable
- Verify heartbeat polling is enabled in openclaw config
- Check openclaw logs: `clawdbot gateway logs`

## Customization Tips

### Adjust Personality
Edit `SOUL.md`:
- Tone and vibe
- Core principles priority
- Level of formality

### Change Role
Edit `IDENTITY.md`:
- Mission statement
- Role description
- Commitments

### Modify Behavior
Edit `AGENTS.md`:
- Workspace conventions
- Safety boundaries
- External action policies

## Security Checklist

- [ ] USER.md contains no sensitive personal information
- [ ] TOOLS.md excludes actual passwords/tokens
- [ ] Email monitoring configured with app-specific password (not main password)
- [ ] MEMORY.md excluded from any public repositories
- [ ] `memory/` directory excluded from version control

## Next Steps

1. **Test basic functionality** - verify MX responds correctly
2. **Customize over time** - add to TOOLS.md as you configure services
3. **Update memory** - MX will maintain memory/YYYY-MM-DD.md files
4. **Review periodically** - update MEMORY.md with important learnings

---

**Questions?** 
- openclaw docs: https://docs.openclaw.bot
- MX Community: https://github.com/MX-Experience

**"Design for machines. Benefit humans. Advance both."** ⚡
