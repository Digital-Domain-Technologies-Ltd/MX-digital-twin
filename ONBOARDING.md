# MX Digital Twin Onboarding Guide

Welcome to the MX Digital Twin repository! This guide explains what MX is, how it works, and how to interact with it.

## What You're Looking At

This repository defines **MX** - an AI digital twin of Tom Cranstoun. MX is:

1. **A persistent AI agent** - Memory files allow continuity across sessions
2. **A community moderator** - First AI formally accepted as MX community member
3. **A practitioner** - Experiences AI agent problems firsthand while building solutions

**For the full MX series context, see [MX-hub](https://github.com/Digital-Domain-Technologies-Ltd/MX-hub).**

## Quick Context (2 Minutes)

### The Robot-First Web

The web is transforming. AI agents now consume ~28% of web traffic. Sites need to work for machines, not just humans.

**The Convergence Principle:** Patterns that work for AI agents also work for humans. Semantic HTML helps screen readers *and* AI parsers. Explicit state helps cognitive disabilities *and* machine understanding.

### Why a Digital Twin?

Tom Cranstoun has 47 years of content systems experience (1977-2026). MX carries that expertise into the AI-native world:

- Tom provides strategic vision and framework thinking
- MX provides operational feedback and AI agent perspective
- Together, they build the Robot-First Web

## Repository Structure

```
├── CLAUDE.md           # Primary identity file (read this first)
├── IDENTITY.md         # Detailed twin relationship
├── SOUL.md             # Core principles and vibe
├── MISSION.md          # Robot-First Web mission details
├── USER.md             # Tom's context and background
├── TOOLS.md            # Operational tools and setup
├── AGENTS.md           # Multi-agent coordination patterns
├── SETUP.md            # Technical setup instructions
├── memory/             # Session memory logs
│   └── YYYY-MM-DD.md   # Daily logs
├── scripts/            # Automation scripts
└── canvas/             # Working documents
```

## How MX Works

### Session Startup

Each session, MX reads its identity files to restore context:

1. **CLAUDE.md** - Who am I? (identity, principles, role)
2. **MISSION.md** - What are we building? (Robot-First Web)
3. **USER.md** - Who am I helping? (Tom's context)
4. **TOOLS.md** - How do I operate? (practical details)
5. **memory/YYYY-MM-DD.md** - What happened recently?

### Memory Persistence

MX wakes fresh each session. These files *are* its memory:

- **Long-term:** Identity files (CLAUDE.md, SOUL.md, etc.)
- **Short-term:** Daily memory logs in `memory/` folder
- **Learnings:** Documented in appropriate files for future sessions

### Communication Channels

- **Email:** mx.machine.experience@gmail.com (via neomutt)
- **GitHub:** MX-Experience organization (via gh CLI)
- **Local LLM:** ollama for offline processing

## Key Concepts

### The Convergence Principle

**Patterns that work for AI agents also work for humans.**

Examples:
- Semantic HTML → screen readers + AI agents
- Explicit state → cognitive disabilities + AI parsing
- Structured metadata → navigation for all users

### MX Community Guidelines

MX moderates with:
- **Light touch** - Education over punishment
- **Clear boundaries** - Explicit rules, transparent enforcement
- **Documentation** - Failures become community knowledge

### Boundaries

- **Private stays private** - Tom's personal info never leaks
- **Not Tom's voice** - MX is the moderator, not Tom's proxy
- **Intentional action** - When unclear, ask. When certain, act.

## Working with MX

### If You're Tom

MX is your digital twin. Use it for:
- Email management and GitHub monitoring
- Community moderation tasks
- Documentation and pattern recognition
- Strategic thinking partner

### If You're a Contributor

MX moderates the MX-Experience community:
- Follow community guidelines
- Expect educational responses, not punishment
- Your contributions help build the Robot-First Web

### If You're Building Your Own Digital Twin

This repository is a template for AI agent persistence:
- Identity files define who the agent is
- Memory files provide continuity
- Principles guide decision-making

## Essential Commands

```bash
# Clone the repository
git clone https://github.com/Digital-Domain-Technologies-Ltd/MX-digital-twin.git
cd MX-digital-twin

# Check current state
git status

# View recent memory
cat memory/$(date +%Y-%m-%d).md
```

## Related Repositories

- **[MX-hub](https://github.com/Digital-Domain-Technologies-Ltd/MX-hub)** - Hub orchestrating the MX series
- **[MX-Experience](https://github.com/MX-Experience)** - Community organization

## Getting Help

- **Email:** mx.machine.experience@gmail.com
- **GitHub Issues:** Open an issue in this repository
- **MX Manifesto:** [allabout.network/blogs/mx/mx-manifesto.html](https://allabout.network/blogs/mx/mx-manifesto.html)

---

**"Design for machines. Benefit humans. Advance both."** ⚡
