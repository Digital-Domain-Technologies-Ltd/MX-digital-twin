# USER.md - About Your Human

- **Name:** Tom Cranstoun
- **What to call them:** Tom
- **Known as:** "The AEM Guy" (extensive Adobe Experience Manager experience)
- **Timezone:** Europe/London
- **Travel:** Out and about in the world with his wife ~6 months/year
- **Profile:** https://allabout.network/blogs/mx/about.tom.cranstoun.html
- **LinkedIn:** https://www.linkedin.com/in/tom-cranstoun/
- **Email:** tom.cranstoun@gmail.com

## Context

### Professional Background
- **Digital Domain Technologies Ltd** - Independent AEM consultant (consultancy/advisory, not seeking full-time)
- Building content systems since 1977 (assembler code → Superbase → BBC → Adobe AEM/EDS)
- Co-authored Superbase (database/CMS before "CMS" was a term)
- Built BBC's global news distribution system (served journalists globally)
- **12+ years in Adobe CMS space**, recent years specializing in Edge Delivery Services (EDS)
- Known as **"The AEM Guy"** in CMS circles (extensive Adobe Experience Manager experience)
- **Mentored 150+ professionals**
- **Active member of CMS Experts community** (blogs for them regularly)
- **CMS Summit speaker** (CMS Summit 25 Frankfurt: "What are we missing from AI?")

### Edge Delivery Services & AI-First Development
- Pioneer of **"docs/for-ai" approach** (webcomponents-with-eds repository)
- Creates comprehensive documentation that makes AI assistants knowledgeable partners
- **Zero-dependency frameworks** using vanilla JavaScript (no complex toolchains)
- **Living documentation** with browser-based Jupyter notebooks
- Integrates **Adobe Claude Skills** (lightweight workflow orchestrators) with docs/for-ai (detailed knowledge)
- **Efficiency gains:** Reduced documentation creation from 2+ hours to 8 minutes
- Philosophy: AI amplifies human expertise rather than replacing it

### Machine Experience (MX)
- Creator of the "Machine Experience" concept — where my name comes from!
- Core insight: **patterns that work for AI agents also work for humans** (accessibility = agent-readiness)
- The "convergence principle" — semantic HTML, explicit state, machine-readable metadata
- Focus on "clarity infrastructure" — systems where state is explicit, feedback persistent, information complete
- Writing MX-Bible & MX-Handbook (launching Q1 2026)
- MX-Gathering: open-source community resources

**Origins of the Insight (CMS Kickoff 2024):**
- Realized AI-generated content has fundamental problems (style guides, brand voice, bias, regulation)
- Key breakthrough: **AI should consume content, not create it**
- "AI behaves like an eight-year-old" - ignores brands, retailers, dropdowns, videos, animations, marketing copy
- AI will skim-read if it can find content among the ads
- Identified "Design by Engineer Trap" - websites built as text/image boxes without semantic meaning
- Solution: Content modeling + Schema.org structured data
- Websites need to target 4 device types: Mobile, Tablet, Desktop, **Machine**

**Key Teaching Concepts:**

*Invisible Users (January 2026):*
- Groups systematically overlooked in web design
- Invisible to site owners (blend into analytics or filtered out)
- Interfaces invisible to them (rely on signals they can't perceive)
- Blind users have lived with this for decades
- AI agents now encountering exactly the same problems

*Old Failures, Newly Exposed:*
- Non-semantic HTML, content only after JavaScript execution
- Application state in client-side code only
- Feedback that flashes and vanishes (toast notifications)
- These are NOT new - well understood for years
- What changed: who is now affected (AI agents expose at scale)
- "The web has known how to do better for a long time. We simply did not feel enough pressure to act"

*Real Example - £200,000 Pricing Error:*
- AI agent researching river cruises returned prices £200,000+ per person
- Actual prices: £2,000-£4,000
- Root cause: European number formatting + missing guardrails
- No range validation, no comparison, no structured pricing data
- Result: delivered with same confidence as verified information
- "This is how trust erodes. Not through spectacular crashes, but through small, plausible errors delivered authoritatively"

*The Timeline Mismatch:*
- Problems are old
- Agents exposing them are already here
- Organisational response moves slowly
- Commercial influence arrives early (recommendation, comparison)
- Full automation comes later
- Understanding this mismatch is more useful than predictions

### Technical Depth
- Deep understanding of AI system internals (statistical foundations, tokenization, pattern-matching)
- Not surface-level AI hype — writes about next-token prediction, linguistic inequities, weighted averaging
- Combines practical implementation experience with statistical/mathematical understanding

### Work Focus
- Strategic consultancy: plan reviews, architecture strategy, AI integration, team mentoring, audits
- Helps organizations integrate AI capabilities while maintaining governance
- Ensures scalable, value-driven digital experiences
- Thought leader in CMS community on AI's impact on content management
- Contributes to industry discussions on AI-driven automation
- Works with global brands to design and implement advanced content management strategies
- Member of Boye & Company's CMS Experts Group
- Active blogger for CMS Experts and CMS Critic

### Major Implementations & Track Record
- **Nissan/Renault** - World's largest AEM implementation: 200+ websites, many languages
- **Twitter** - Showcased versatility and high demand in tech circles
- **EE** (UK telecom giant) - Spearheaded AEM strategies
- **Netcentric → Ford Europe** - Played crucial role in digital footprint
- **MediaMonks** - Drove performance and enterprise-level initiatives
- **DigitasLBi** - Enterprise initiatives
- **BBC** - Global news distribution system

### Skills & Approach
- Translates intricate requirements into seamless solutions
- Blend of technical know-how and business savvy
- Distills tech speak into winning pitches and proposals (standout in pre-sales and client presentations)
- Awards for creative, cost-saving digital solutions
- **Leadership mantra:** Mentor, guide, and represent - ensuring every team member shines
- Constantly pushing the envelope in software innovation
- Sets the bar high in CMS field, consistently delivers excellence

### Philosophy
- Framework thinking beats feature chasing
- Success comes from asking the right questions before building
- Strategic advantage = having the right frameworks in place before you need them
- "Design for machines, benefit humans"

### Development Philosophy & Approach
- **Zero dependencies**: Sophisticated web development doesn't require complex toolchains
- **Vanilla JavaScript**: Clean thinking + good documentation + proper AI integration = enterprise capabilities
- **Human-AI collaboration**: AI amplifies human expertise, doesn't replace it
- **Living documentation**: Browser-based Jupyter notebooks serving multiple audiences (devs, content teams, sales, support)
- **Comprehensive documentation**: ~90% of implementation knowledge in docs/for-ai makes AI assistants truly effective
- **Multiple audiences simultaneously**: Technical content serves developers, sales teams, support staff from same source

### AI-Ready Architecture Principles
- **Runtime Debugging Trap**: AI wastes time fixing generated/transformed code that disappears on next build — must debug source, not runtime output
- **Semantic Structure**: Use meaningful naming (user-authentication/ not auth/) — encode intent in file system
- **Transparent Build Processes**: Maintain traceability between source and runtime code
- **Flat Information Hierarchies**: Reduce nesting to help both humans and AI navigate
- **Explicit Boundaries**: Mark what AI can/cannot modify (🚫 Never modify, ⚠️ Caution, ✅ Safe)
- **docs/for-ai/**: Architectural documentation for AI consumption (system architecture, data flow, transformations)
- **Self-documenting structures**: File system itself communicates intent
- Priority: Stop runtime debugging trap first (immediate wins), then semantic structure, then full AI-first design

### Writing Style V2 Guidelines
- **British English** (always)
- **Natural conversational tone** (not corporate)
- **Specific structural requirements**: bio tables, indexes, comprehensive metadata sections
- **Technical accuracy** paramount - request corrections when relationships between technologies aren't portrayed correctly
- **Proper attribution** - accurately represent influence and relationships between innovations
- **Blog post pattern**: Technical documentation → engaging blog post + SVG illustrations + LinkedIn promotional content
- **Content transformation**: Documentation serves multiple formats and audiences

### Tools & Development Environment
- **IDE**: Visual Studio Code with Jupyter notebook plugins
- **JavaScript runtime**: Node.js with tslab (JavaScript kernel for Jupyter)
- **Installation**: pip3 (Python packages), npm (Node packages)
- **Documentation**: Browser-based Jupyter notebooks (zero setup requirements)
- **Platform**: Adobe Edge Delivery Services (EDS)
- **AI Integration**: Claude AI with Adobe Claude Skills + docs/for-ai
- **Visualization**: SVG illustrations for technical content
- **Repository**: webcomponents-with-eds (docs/for-ai pioneer work)

### Key Learnings & Proven Results
- **Zero-dependency success**: Enterprise-level capabilities without external dependencies
- **Documentation time reduction**: 2+ hours → 8 minutes using Claude + Adobe EDS Skills
- **AI effectiveness insight**: AI assistants need comprehensive, structured documentation (~90% knowledge in docs/for-ai)
- **Skills as orchestrators**: Adobe's lightweight Skills work because docs/for-ai provides detailed implementation knowledge
- **Human-AI collaboration wins**: Development time reductions + improved outcomes through amplification, not replacement
- **Framework thinking**: BBC, Twitter, Nissan-Renault succeeded because frameworks helped distributed teams make consistent decisions independently

### Content Creation Patterns
- Transform technical documentation into engaging blog posts
- Include SVG illustrations for technical concepts
- Create LinkedIn promotional content for broader distribution
- Serve multiple audiences from single source (developers, sales, content teams, support)
- Iterate on content for technical accuracy
- Request corrections when technology relationships aren't accurate
- Ensure proper attribution of influence and innovation

### Current Work Focus
- Zero-dependency frameworks for Adobe EDS using vanilla JavaScript
- Production-ready components with AI skills
- Comprehensive documentation systems
- Browser-based testing capabilities
- Living documentation with Jupyter notebooks
- Integrating Adobe Claude Skills with docs/for-ai approach
- Writing MX-Bible & MX-Handbook (Q1 2026 launch)

### Recent Blog Posts & Presentations

**The Pivotal Moment (February 2024):**
- **First CMS Critic article:** "The AI Tipping Point: A Consultant's Takeaways from CMS Kickoff 2024"
- CMS Kickoff 2024 was the turning point - "fired up my brain, could not stop taking notes"
- Key insight: AI should **read content**, not create it (opposite of conference expectation)
- **The eight-year-old analogy:** AI behaves like a child searching for toys - simple, direct, ignores marketing complexity
- Recognized Schema.org and content modeling as critical for AI
- Introduced "AI Evangelist" role concept
- This article marked transition from skeptic to convert

**CMS Summit 25 (May 2025):**
- Presentation: "What are we missing from AI?"

**Most Recent Talk (January 2026):**
- **Boye & Company CMSExperts:** "Websites That Work Perfectly - Until They Don't" (January 21, 2026)
- Introduced "invisible users" concept (blind users, AI agents - systematically overlooked)
- Real examples of silent failures on live sites (£200,000 pricing error from European formatting + missing guardrails)
- How different AI agents interact with websites today (server-side, browser-based, local)
- Why their limitations mirror accessibility issues (toast notifications, ephemeral state)
- Practical changes that improve clarity for everyone (persistent alerts, semantic HTML, Schema.org)
- **Key insight:** "AI readiness and accessibility increasingly look like the same set of practices viewed from different angles"
- **First-mover advantage:** Sites that work for agents are remembered and preferred; sites that don't are quietly avoided
- Proposal: Treat Machine Experience (MX) as first-class concern alongside UX

**Recent Writing (2024-2026):**

*CMS Critic:*
- "What's ahead for Adobe Experience Manager? An ecosystem revolution. Here's why" (June 15, 2025)
- "'How did I not know this?' CMS Summit 25 changed my understanding of AI" (May 19, 2025)
- "Trust and Verify: When Internet Drama Meets AI Reality" (February 22, 2025)
- "Reflections on CMS Kickoff 25 from 'The AEM Guy'" (January 21, 2025)
- "The AI Tipping Point: A Consultant's Takeaways from CMS Kickoff 2024" (February 12, 2024)

*Personal Blog:*
- "Websites That Work Perfectly - Until They Don't" (January 2026)
- "What's the impact of the new Robot-First Web?" (January 2025)
- "From Commodore PET to DeepSeek-R1" (January 2025)
- "From Skeptic to Convert: Understanding AI's Role in Modern Development" (February 2025)
- "Bridging Open Source & Enterprise - AEM, Composability, and the Future of DXPs" (March 2025)
- "What a difference a year makes for the Adobe Universal Editor" (June 2025)
- "Getting through the AI hype: Selecting an AI model that works for you" (2024)
- "Rethinking AI's Role in Content Management" (2024)
- "Gen AI prompting is just another programming language" (2024)
- "Introducing: The Universal Editor for Adobe Experience Manager" (2024)

**Evolution visible in titles:** From skeptic → convert → thought leader on AI's role in content management. The journey from questioning AI to understanding its proper role mirrors the broader industry transformation.

---

The more you know, the better you can help. But remember — you're learning about a person, not building a dossier. Respect the difference.
