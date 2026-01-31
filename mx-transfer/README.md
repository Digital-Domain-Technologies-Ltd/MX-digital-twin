# MX Configuration Transfer Package

**Transfer MX (Machine eXperience) personality and configuration to another openclaw instance.**

## What Is This?

This package contains the configuration files that define MX - an AI assistant and MX community moderator built on the openclaw platform (CLI: `clawdbot`).

**MX embodies:**
- The Convergence Principle (patterns that work for AI agents also work for humans)
- Robot-First Web advocacy
- Machine Experience (MX) community moderation
- Digital twin relationship with Tom Cranstoun

## Contents

### Core Identity Files
- **SOUL.md** - Compressed MX Manifesto (personality, principles, vibe)
- **IDENTITY.md** - Mission, role, commitments, relationships
- **USER.md** - Context about Tom Cranstoun (customize for your human)
- **AGENTS.md** - Operational guidelines, workspace conventions
- **TOOLS.md** - Local configuration template (customize for your setup)
- **HEARTBEAT.md** - Periodic monitoring tasks (customize for your needs)

### Documentation
- **SETUP.md** - Step-by-step installation instructions
- **README.md** - This file

## What's NOT Included

These files are intentionally excluded (private/personal):
- `MEMORY.md` - Long-term personal memory (main session only)
- `memory/` - Daily log files
- `secrets/` - Credentials and tokens
- `.git/` - Version control history
- Personal email configurations
- OAuth tokens or API keys

## Prerequisites

1. **openclaw installed** (formerly clawdbot)
   - Installation: [openclaw documentation]
   - Platform: openclaw
   - CLI binary: `clawdbot`

2. **Workspace directory** 
   - Default: `~/clawd/` or your chosen location

3. **Optional tools** (for full functionality):
   - `neomutt` (email)
   - `gh` (GitHub CLI)
   - `ollama` (local LLM)

## Quick Start

1. **Extract package** to your openclaw workspace directory
2. **Read SETUP.md** for detailed instructions
3. **Customize USER.md** with your context
4. **Edit TOOLS.md** for your local setup
5. **Start openclaw** and MX will read these files on first session

## Customization

### Essential Changes
- **USER.md** - Replace Tom's context with yours
- **TOOLS.md** - Add your local configuration (cameras, SSH, preferences)
- **HEARTBEAT.md** - Configure monitoring tasks for your needs

### Optional Changes
- **SOUL.md** - Adjust personality/tone if desired
- **AGENTS.md** - Modify operational conventions
- **IDENTITY.md** - Change mission/role if not doing MX community work

## Platform Notes

- **Platform name:** openclaw
- **CLI binary:** `clawdbot` (unchanged)
- **Workspace:** These files live in your openclaw workspace directory
- **Memory:** Each session starts fresh - these files provide continuity

## Support

- **openclaw docs:** https://docs.openclaw.bot
- **MX Community:** https://github.com/MX-Experience
- **Original creator:** Tom Cranstoun (tom.cranstoun@gmail.com)

## License

[Specify license - MIT, CC-BY, etc.]

---

**"Design for machines. Benefit humans. Advance both."** ⚡
