# Draft 03 (Revised) — Nature Career Column with Personal Experience

**Working title:** How AI helped three humanities scholars break through the barriers of research  
**Authors:** Simon Wang, Ruobin Yu, Stuart Christie  
**Target:** ~1,000 words

---

## Opening Hook

Our research began with a simple idea: use AI to help language learners write poetry. But as the study took shape, we kept running into barriers — and AI kept helping us break through them.

The three of us — a language-centre lecturer, a literature professor, and a PhD student in English at Hong Kong Baptist University — wanted to explore how different AI configurations shape creativity when students co-write poems with chatbots. We could have pointed our participants at ChatGPT and called it a day. But generic chatbots offer no flexibility over the parameters that drive AI behaviour, no conversation logging, and no way to set up experimental conditions. We needed a custom platform. Off-the-shelf tools could not give us that.

The problem was that, although some of us understood how programming works in principle, none of us had the hands-on coding experience to build something like this.

**[Word count: 137]**

---

## How vibe coding broke the programming barrier

Vibe coding means building software by describing what you want in natural language, rather than writing the code yourself. Using a platform called Lovable, we typed out our requirements in plain English: four chat rooms with different AI temperature and top-p settings, a clean interface for students, conversation logging, and toggles for our experimental conditions. Lovable generated the application. We connected it to theenRouter API for access to Claude Sonnet 4 as our language model and configured each room ourselves.

The result — a fully functional research platform at poetry.aitutor.ink — was deployed in days. Before vibe coding, we would have spent weeks explaining our needs to a professional programmer, hoping the output matched our vision. Instead, we described what we knew and the AI built it.

**[Word count: 136]**

---

## A humanities scholar's learning curve

As a humanities-trained researcher with essentially zero prior coding experience, I faced two practical frictions. First, when I proposed AI prototypes to colleagues in the humanities, they often questioned the motivation: Were we commodifying creativity? Were we privileging technical spectacle over interpretive depth? Those conversations forced me to clarify the pedagogical and ethical aims in plain terms, which ultimately improved the project — but they also consumed time and emotional labor.

Second, translating those aims into working software was initially painful. I had to explain what I wanted to a professional programmer, interpret API documentation, and sit through iterations that felt opaque. Small misunderstandings about data formats or conversational turns would stretch into weeks of back-and-forth. Learning to write even simple scripts, understand token costs, or manage a deployment pipeline felt intimidating and slow.

Low-code platforms changed that calculus. They removed much of the plumbing so I could prototype and test interactions directly, which meant faster research cycles and closer alignment between the pedagogy I imagined and the tools participants actually used.

**[Word count: 183]**

---

## The human roles that AI cannot fill

Vibe coding removed the programming barrier, but it did not remove us. As research designers, we defined the experimental structure — two AI creativity levels crossed with two awareness conditions — and chose the specific parameter values for each room. As prompt authors, we shaped the chatbot's behaviour: not a ghostwriter, but a writing coach that suggests vocabulary, offers rhyme patterns, and nudges students toward creative risk. As quality controllers, we piloted the platform and discovered that the AI was sometimes over-scaffolding — providing so much help that students had little room to create. Fixing that required understanding poetry and learning, not debugging code. Vibe coding did not shrink our roles. It sharpened them.

**[Word count: 114]**

---

## The platform revealed what off-the-shelf tools could not

The platform works. Participants in rooms with higher AI temperature settings interacted with the chatbot in fundamentally different ways from those in lower-temperature rooms — exactly the kind of variation our study was designed to detect. Had we used ChatGPT, these differences would have been invisible.

Building the tool also deepened our understanding. Configuring temperature and top-p values forced us to grasp what those parameters actually do — not as abstract concepts, but as settings that visibly change how the AI responds. That practical knowledge made us sharper researchers.

**[Word count: 90]**

---

## AI as a one-stop research partner

The barriers AI helped us cross did not stop at platform building. A third barrier stood between us and the wider research community: we are novice academic writers working in a second language, with limited experience navigating large bodies of literature in an unfamiliar field.

Here, AI stepped in again — not as a single tool, but as an integrated research environment. Using an AI-powered IDE, we access the literature, the codebase, and our collected data in one workspace. The AI agent operates within our project folders, aware of the full context — research design documents, conversation logs, analysis scripts. When we ask it to help draft a section or trace how a finding connects to the literature, it draws on everything in the project, not just a generic training set.

This context-aware workflow turned AI from a collection of separate tools into a one-stop research partner — one that dramatically lowers the barriers for researchers who might otherwise be shut out by language, technical skill, or unfamiliarity with a field's conventions.

**[Word count: 170]**

---

## Why building beats borrowing

The real argument for building your own tools is not convenience — it is control. Off-the-shelf platforms are designed for general use. They hide the settings that matter most to researchers: the parameters that shape AI behaviour, the logs that capture interaction data, the design choices that turn a conversation into an experiment. When you build your own platform — even through vibe coding, without traditional programming — you decide what the AI does, what it records, and how it behaves.

AI's bridging role is what makes this possible. It translates domain expertise — knowledge of teaching, research design, literary analysis — into functional tools, without requiring a programming language first. The barrier between an idea and a working prototype drops from months to hours.

This is not a shortcut. It is a shift in who controls the research instrument. For scholars in the humanities and social sciences, where custom tools have traditionally been out of reach, that shift matters.

**[Word count: 157]**

---

## Three barriers, one scaffold

Our project began with a question about poetry and ended with a lesson about barriers. AI helped us give language learners a space to write creatively. It helped us build the research platform we needed. And it helped us navigate the literature, data, and writing that bring a study to life. Three barriers, one recurring solution: AI as scaffold, with humans in the driver's seat.

You do not need to learn to code. You need to know what to build — and why.

**[Word count: 75]**

---

## Total Word Count: ~1,062

| Section                                                  | Draft 03   | Revised    | Change     |
| -------------------------------------------------------- | ---------- | ---------- | ---------- |
| Opening hook                                             | 137        | 137        | 0          |
| How vibe coding broke the programming barrier            | 136        | 136        | 0          |
| **A humanities scholar's learning curve (NEW)**          | **0**  | **183**    | **+183**   |
| The human roles that AI cannot fill                      | 114        | 114        | 0          |
| The platform revealed what off-the-shelf tools could not | 90         | 90         | 0          |
| AI as a one-stop research partner                        | 170        | 170        | 0          |
| Why building beats borrowing                             | 157        | 157        | 0          |
| Closing                                                  | 75         | 75         | 0          |
| **Total**                                          | **879**    | **1,062**  | **+183**   |

**Note:** The personal experience section has been integrated as a new section (Section 3) after "How vibe coding broke the programming barrier." This adds 183 words, bringing the total to ~1,062 words — slightly over the 1,000-word target but well within the acceptable range for Nature Careers columns. The personal narrative adds concrete texture and emotional resonance to the abstract discussion of technical barriers. If further trimming is needed, the new section could be condensed by removing some of the detail about interactions with colleagues or the technical learning curve.

---

## Revision Comments for Next Draft

**1. Reduce technical jargon:** The draft currently contains many technical terms (e.g., "temperature," "top-p," "parameters") that ordinary researchers and general audiences might not understand. In the next revision, replace most specific mentions of "temperature" and "top-p" with more accessible language such as "AI settings" or "AI configurations" to improve readability for non-technical readers.

**2. Remove redundant IDE references:** The mention of "AI-powered IDE" and "VS Code" in the "AI as a one-stop research partner" section is somewhat redundant since the entire passage focuses on vibe-coding and low-code/no-code platforms. This section should be streamlined to maintain focus on the core message about accessible AI tools rather than introducing additional technical concepts.

**3. Add paragraph describing initial difficulties:** A new paragraph should be added to describe the specific difficulties the team faced initially before discovering vibe coding. This could include challenges such as:
   - Communication breakdowns with professional developers
   - Budget or time constraints
   - Technical knowledge gaps that made it hard to articulate requirements
   - Multiple failed attempts with different approaches before finding a solution
   
   This addition would strengthen the narrative arc from problem to solution and make the value of vibe coding more concrete and relatable.
