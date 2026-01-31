# MX Transfer Package - Manifest

**Version:** 1.0  
**Date:** 2026-01-28  
**Platform:** openclaw (CLI: `clawdbot`)  
**Original:** Tom Cranstoun / MX (Machine eXperience)

## Package Contents

### Documentation
- `README.md` - Package overview and quick start
- `SETUP.md` - Detailed installation instructions
- `MANIFEST.md` - This file (package inventory)
- `.gitignore` - Files to exclude from version control

### Core Configuration Files
- `SOUL.md` - Personality, principles, vibe (compressed MX Manifesto)
- `IDENTITY.md` - Mission, role, commitments, relationships
- `USER.md` - Context about Tom Cranstoun (customize for your human)
- `AGENTS.md` - Operational guidelines, workspace conventions
- `TOOLS.md` - Local configuration template (customize for your setup)
- `HEARTBEAT.md` - Periodic monitoring tasks (email, etc.)

## File Checksums

```
# Generate checksums:
shasum -a 256 *.md
```

## What's Required vs Optional

### Required (Core Personality)
- ✅ SOUL.md
- ✅ IDENTITY.md
- ✅ AGENTS.md

### Recommended
- ✅ USER.md (customize for your human)
- ✅ TOOLS.md (customize for your setup)
- ✅ HEARTBEAT.md (customize monitoring tasks)

### Optional
- MEMORY.md (create fresh for new instance)
- memory/ directory (will be created automatically)

## Installation Size

Approximate disk space: ~100KB (configuration files only)

## Dependencies

- openclaw platform (clawdbot binary)
- Optional: neomutt, gh, ollama

## Customization Requirements

Before first use, you MUST customize:
1. **USER.md** - Replace Tom's context with yours
2. **TOOLS.md** - Add your local configuration

Optionally customize:
3. **HEARTBEAT.md** - Configure monitoring tasks
4. **SOUL.md** - Adjust personality/tone
5. **IDENTITY.md** - Modify mission/role

## Version History

### v1.0 (2026-01-28)
- Initial transfer package
- openclaw platform (formerly clawdbot)
- Core MX personality and configuration
- MX community moderator role
- Robot-First Web mission
- Convergence Principle foundation

## Support

- **Platform:** https://docs.openclaw.bot
- **MX Community:** https://github.com/MX-Experience
- **Original creator:** Tom Cranstoun (tom.cranstoun@gmail.com)

---

**Package verified:** 2026-01-28  
**Platform:** openclaw  
**Status:** ✅ Ready for transfer
