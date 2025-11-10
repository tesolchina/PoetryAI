# From Literary Theory to Lines of Code: Building a Research Platform as a Humanities Scholar
## A Nature Career Column Submission

**Word count:** ~1,400 words  
**Author:** Yu Ruobin, Department of English, Hong Kong Baptist University  
**Category:** Career Feature / Turning Point

---

## Article Text

**"You're going to build... what?"**

My literature professor's confusion was understandable. I'd just proposed developing a web-based AI poetry platform with customizable parameters, real-time conversation logging, and a backend database—as a PhD candidate in English with no formal programming training.

"I need it for my dissertation," I explained. "I'm studying how AI parameter settings affect collaborative creativity in L2 poetry writing. But the platform I need doesn't exist yet. So I have to build it."

### The Research Question That Demanded Technical Skills

My doctoral research sits at an unusual intersection: L2 creative writing pedagogy meets computational linguistics meets human-AI interaction design. The question driving my work—"What is the 'temperature' of a poem?"—examines how LLM parameters like temperature and top-p shape collaborative creativity when English language learners co-write poetry with AI.

The theoretical framework was clear. From Hanauer's work on L2 poetry pedagogy, I understood the imitation-transformation process. From Coenen et al.'s research on Wordcraft, I saw how "surprise harvest" moments drive creative discovery. From DDL (Data-Driven Learning) research, I knew learners benefit from pattern exploration. But to test whether different AI parameter settings produce different interaction types—structured diagnosis-repair versus exploratory surprise—I needed a controlled experimental platform.

And that platform didn't exist.

### The Reality Check

The tools available fell into two categories: either too simple (ChatGPT's interface, which I couldn't customize or control) or too complex (building from scratch with enterprise frameworks I didn't understand). I needed something in between: four separate chat rooms with different parameter configurations, session logging, awareness condition toggles, and a clean interface my participants could actually use.

I had three options: wait for someone else to build it, abandon the research design, or learn to code it myself.

I chose option three.

### Learning to Speak in Multiple Languages

The journey from literary analysis to software development required learning not just new skills, but new ways of thinking. As a humanities scholar, I was trained to interpret ambiguity, appreciate complexity, and embrace multiple valid readings. Programming demanded the opposite: precise syntax, unambiguous logic, and one correct answer.

My first attempt at coding was humbling. I spent an entire afternoon trying to understand why my Python script wouldn't run, only to discover I'd used a colon where I needed a comma. In literary criticism, punctuation creates nuance. In code, it creates crashes.

**Phase 1: The Basics (Month 1-2)**

I started with Python tutorials, working through basics while my research design document gathered digital dust. Variables, loops, functions—concepts that seemed straightforward in theory became puzzles when I tried to implement them. But I had motivation most tutorial-followers lack: I knew exactly what I needed to build and why.

The breakthrough came when I stopped trying to learn "programming" abstractly and started solving specific problems:
- How do I make an API call to OpenRouter?
- How do I store conversation history?
- How do I implement different parameter settings?

Each question led to targeted learning. Stack Overflow became my new research database, GitHub repositories my new primary sources.

**Phase 2: Building the Chatbot Framework (Month 3-4)**

With basic Python literacy, I tackled the core challenge: creating a customizable chatbot framework. I needed one system that could generate four different AI personalities by adjusting temperature and top-p parameters.

This required understanding not just code, but the mathematics behind LLM sampling. What does temperature actually do? How does nucleus sampling (top-p) differ from top-k? These weren't just technical questions—they were central to my research. Understanding them computationally deepened my theoretical framework.

I built iteratively: first, a simple chatbot that could respond to one message. Then conversation memory. Then parameter customization. Then multiple conversation instances. Each addition required debugging sessions where I'd stare at error messages, Google frantically, and slowly piece together solutions.

The moment my first multi-turn conversation worked—when the AI remembered context and responded coherently—I felt the same thrill as when I'd first analyzed a poem's meter and suddenly understood how form creates meaning. Different domains, same intellectual satisfaction.

**Phase 3: The Web Interface (Month 5-6)**

A Python script running in Terminal wouldn't work for my participants. I needed a web interface—which meant learning HTML, CSS, JavaScript, and Flask (a Python web framework).

This phase nearly broke me. Frontend development felt impossibly distant from my training. How do you make a button appear in the right place? Why won't this div element align properly? What's the difference between padding and margin?

But again, having a clear goal helped. I wasn't building a generic website—I was creating four specific chat rooms for poetry writing. Every design decision connected to research needs:
- **Clean, minimalist interface** (reduce cognitive load for L2 learners)
- **Clear turn-taking** (support conversation analysis)  
- **Conditional parameter display** (enable awareness manipulation)
- **Session timer** (standardize data collection)

I learned by deconstructing examples, copying code snippets, breaking things, and slowly understanding what each piece did.

**Phase 4: The Database and Logging (Month 7)

**Phase 4: The Database and Logging (Month 7)**

Research data is precious. I needed every conversation message, timestamp, parameter setting, and user action logged reliably. This meant learning about databases—specifically Supabase, a PostgreSQL-based system I chose for its simplicity and documentation.

Designing the data schema required thinking like both a researcher and a programmer. What tables do I need? How do conversations relate to rooms relate to participants? What queries will I run during analysis?

This phase bridged my two worlds beautifully. Database design is fundamentally about relationships and structure—not unlike analyzing narrative structures or thematic patterns in literature. I was creating a system to capture and preserve human-AI creative interaction, much like scholars have preserved and analyzed literary texts for centuries.

### The Transdisciplinary Identity Crisis (and Resolution)

Around month 5, I had an identity crisis. Was I still a literature scholar? Had I become a programmer? Neither felt quite right.

My CS friends could code circles around me. My literature colleagues could analyze texts with sophistication I still aspire to. I felt like an imposter in both worlds—not technical enough for computer science, not purely humanistic enough for English departments.

But gradually, I realized this liminal space was actually my strength. I could:

- **Read computational linguistics papers** and understand how findings apply to creative writing pedagogy
- **Design user interfaces** informed by cognitive load theory and L2 acquisition research  
- **Debug code** while keeping research ethics and participant experience central
- **Analyze conversation data** using both NLP metrics and qualitative discourse analysis

I wasn't trying to become a computer scientist. I was becoming a humanities scholar with computational skills—a different, increasingly necessary role.

### What Building the Platform Taught Me

**1. Research questions can drive technical learning.**

I didn't need to master all of Python before starting. I learned what I needed, when I needed it, for a specific purpose. This targeted learning was more efficient than traditional coursework would have been.

**2. Tool-building is intellectual work.**

Creating the platform wasn't separate from my research—it was integral to it. Deciding how to implement "temperature" visibility required understanding both the technical mechanism and the theoretical construct of "awareness" in my research design. Every design decision was a methodological decision.

**3. Documentation is for future-you.**

I learned this painfully when I returned to code after two weeks and had no idea what my own functions did. Good documentation isn't just for others—it's for maintaining your own sanity.

**4. The perfect is the enemy of the functional.**

My platform isn't elegant code. Professional developers would probably weep at my architecture. But it works. It collects the data I need. It's maintainable enough for my purposes. That's sufficient.

**5. Interdisciplinary work requires intellectual humility.**

I had to ask "dumb" questions constantly. "What's an API?" "How does authentication work?" "Why did my entire database just disappear?" (Answer: I hadn't committed changes. Rookie mistake.) Admitting ignorance was uncomfortable but necessary.

### The Unexpected Benefits

Building the platform transformed my research in ways I hadn't anticipated:

**Deeper theoretical understanding.** Implementing parameter controls forced me to understand temperature and top-p at a level reading papers never did. I couldn't just cite "creative outputs" abstractly—I had to know precisely what mathematical operations produced them.

**Better research design.** Writing code that checks for edge cases made me think more rigorously about my experimental conditions. What if a participant sends an empty message? What if they're disconnected mid-session? Programming requires anticipating failures—good preparation for research.

**Methodological credibility.** At conferences, my technical competence surprises people. "You built this yourself?" It signals that I understand my research infrastructure deeply, not just theoretically.

**Marketable skills.** Whether I stay in academia or not, I now have a portfolio: a functional web application, database design experience, API integration skills, and a GitHub repository that proves I can build things.

### Advice for Humanities Scholars Facing Similar Challenges

**1. Start with a concrete goal, not abstract learning.**

Don't try to "learn Python." Instead, solve a specific problem: scrape some data, automate a task, build one small tool. Purpose drives persistence.

**2. Embrace the beginner's mindset.**

You will feel stupid. Often. Accept this. Every expert was once a confused beginner copying code from Stack Overflow without fully understanding it.

**3. Use modern tools and resources.**

I relied heavily on:
- **ChatGPT/Claude** for explaining concepts and debugging
- **YouTube tutorials** for visual learning
- **GitHub repositories** for example code
- **Documentation** (Flask, OpenRouter, Supabase docs became my textbooks)

**4. Find a technical mentor (even informally).**

I joined a CS student's office hours as a "visiting scholar." He answered my Python questions in exchange for feedback on his writing. Bartering expertise works.

**5. Build in public (or at least semi-public).**

I documented my process on my research GitHub. Explaining my code to potential readers forced me to understand it better. Plus, it created an audit trail of my methodology.

**6. Remember: you're not becoming a computer scientist.**

You're becoming a humanities scholar with computational skills. That's different. Your value isn't in writing the most efficient code—it's in asking questions that bridge domains.

### The Current State

My platform now runs four independent chat rooms with customizable AI parameters, logs every interaction with timestamps, implements awareness condition toggles, and presents a clean interface for L2 learners. It took seven months of evening and weekend work, countless debugging sessions, and more coffee than healthy.

But it exists. I built it. And now I can run the study I designed—not a compromised version limited by available tools, but the precise research protocol my questions demand.

### The Bigger Picture

My experience reflects a broader shift in humanities research. As we engage with digital culture, AI systems, and computational methods, the line between "using tools" and "building tools" blurs. Sometimes the research you want to do requires tools that don't exist yet.

We need more humanities scholars willing to venture into technical spaces—not to abandon humanistic inquiry, but to bring humanistic questions to technological domains. Who better to ask "What is the temperature of a poem?" than someone trained in both literary analysis and computational systems?

The academy is slowly recognizing that transdisciplinary work isn't just collaboration between disciplines, but integration within individual scholars. We need people who can code *and* close-read, who understand APIs *and* argumentation, who can debug *and* theorize.

This doesn't mean every humanities scholar needs to program. But for those of us asking computationally-inflected questions, technical skills aren't optional anymore. They're part of the research.

### Conclusion

When I started my PhD, I never imagined I'd spend months writing Python code, wrestling with CSS layouts, and debugging database connections. But my research question demanded it, and I discovered I could learn what I needed.

Building the platform taught me more than programming—it taught me that intellectual growth often requires leaving your comfort zone, that research questions can drive skill acquisition, and that the humanities can engage deeply with technology without losing humanistic perspective.

As I write this, my platform is running smoothly, logging interactions, and collecting the data that will become my dissertation. Every time a participant creates a poem through my interface, I feel a unique satisfaction—not just from the research data, but from knowing I built the bridge between my question and its answer.

Sometimes the best tool for your research is the one you build yourself.

---

## Author Bio

Yu Ruobin is a PhD candidate in the Department of English at Hong Kong Baptist University, researching the intersection of AI-assisted language learning and creative writing pedagogy. Her work explores how AI parameter settings shape collaborative creativity in L2 poetry writing. She built her research platform herself, despite having no formal programming training.

---

## Box: Technical Skills Acquired (7 Months, Self-Taught)

**Programming Languages:**
- Python (core language for chatbot framework)
- JavaScript (frontend interactivity)
- HTML/CSS (web interface)
- SQL (database queries)

**Frameworks & Tools:**
- Flask (Python web framework)
- Supabase (PostgreSQL database)
- OpenRouter API (LLM access)
- Git/GitHub (version control)

**Key Concepts Mastered:**
- API integration and authentication
- Database schema design
- Session management
- Parameter manipulation in LLMs
- Responsive web design
- Data logging and export

**Learning Resources:**
- ChatGPT/Claude for debugging and explanations
- Stack Overflow for specific problems
- YouTube tutorials for visual learning
- Official documentation (primary textbooks)
- GitHub repositories for examples

**Total Development Time:** ~7 months (part-time, alongside coursework and literature review)

---

## Suggested Pull Quotes

> "I wasn't trying to become a computer scientist. I was becoming a humanities scholar with computational skills—a different, increasingly necessary role."

> "Building the platform wasn't separate from my research—it was integral to it. Every design decision was a methodological decision."

> "Who better to ask 'What is the temperature of a poem?' than someone trained in both literary analysis and computational systems?"

> "Sometimes the best tool for your research is the one you build yourself."

---

## Submission Notes

**Why this article fits Nature Career Column:**

1. **Addresses growing trend:** More humanities scholars need computational skills for digital research
2. **Practical transformation story:** Concrete journey from zero coding knowledge to functional platform
3. **Methodological innovation:** Shows how tool-building can be research itself, not just preparation
4. **Interdisciplinary relevance:** Relevant to digital humanities, computational social science, EdTech research
5. **Authentic struggle:** Honest about challenges, frustrations, and imposter syndrome
6. **Actionable advice:** Specific strategies for humanities scholars learning to code
7. **Timely topic:** AI in education, digital methods, transdisciplinary work

**Target audience:**
- Humanities PhD students facing technical research needs
- Digital humanities researchers
- Interdisciplinary scholars bridging humanities and computer science
- Anyone building custom research tools
- Early-career researchers considering computational skills

**Comparable Nature Career articles:**
- "Learning to code as a biologist" (Career Feature)
- "From bench to keyboard: Scientists learning data science" (Toolbox)
- "Building your own research tools" (Turning Point)

---

**Document Status:** Draft for review  
**Created:** November 10, 2025  
**Focus:** Transdisciplinary journey from literature to platform development
**Next steps:**
- Confirm word count within Nature Career guidelines (typically 800-1500 words)
- Add any required competing interests or funding acknowledgments
- Consider including screenshot of platform (if allowed)
- Review for tone (balance humility and confidence)
