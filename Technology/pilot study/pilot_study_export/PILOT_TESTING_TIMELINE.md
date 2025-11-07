# Pilot Testing Timeline & Preparation Guide
## Week-by-Week Implementation Plan

---

## 📅 Complete Timeline Overview

```
Week 1: PREPARATION (Nov 4-8)
├── Days 1-2: Recruitment & Scheduling
├── Days 3-4: System Testing & Materials Prep
└── Day 5: Facilitator Training

Week 2: SESSION 1 - LOGIN TESTS (Nov 11-12)
├── Can schedule multiple per day (10 min each)
├── P1, P2, P3, P4: Login & setup
└── Schedule Session 2 for each participant

Week 3: SESSION 2 - POETRY WRITING (Nov 18-21)
├── Day 1 (Mon): P1 Session 2 - Room 1 (Structured-Aware) - 25 min
├── Day 2 (Tue): P2 Session 2 - Room 2 (Structured-Unaware) - 25 min
├── Day 3 (Wed): P3 Session 2 - Room 3 (Exploratory-Aware) - 25 min
└── Day 4 (Thu): P4 Session 2 - Room 4 (Exploratory-Unaware) - 25 min

Week 4: ANALYSIS & REPORTING (Nov 25-29)
├── Days 1-2: Data compilation and initial analysis
├── Days 3-4: Deep dive analysis and coding
└── Day 5: Report writing and recommendations
```

---

## WEEK 1: PREPARATION

### Day 1 (Monday) - Recruitment & Scheduling

**Morning (2 hours)**
- [ ] Finalize participant criteria
- [ ] Prepare recruitment materials
  - [ ] Create recruitment flyer/poster
  - [ ] Draft recruitment email/message
  - [ ] Prepare screening questions
- [ ] Identify recruitment channels
  - [ ] Email lists
  - [ ] Social media groups
  - [ ] Campus bulletin boards
  - [ ] Personal networks

**Afternoon (3 hours)**
- [ ] Begin outreach
  - [ ] Send recruitment emails
  - [ ] Post to social media
  - [ ] Put up physical flyers
- [ ] Create scheduling system
  - [ ] Set up Calendly or similar
  - [ ] Define available time slots
  - [ ] Prepare confirmation email template
- [ ] Screen responses
  - [ ] Apply inclusion/exclusion criteria
  - [ ] Aim to recruit 5-6 (account for dropouts)

**Evening**
- [ ] Follow up with interested individuals
- [ ] Aim to have 4 confirmed by end of day

**Deliverable:** 4 participants confirmed and scheduled

---

### Day 2 (Tuesday) - Recruitment Completion & Materials

**Morning (2 hours)**
- [ ] Finalize participant schedule
  - [ ] P1: __________ [Date/Time]
  - [ ] P2: __________ [Date/Time]
  - [ ] P3: __________ [Date/Time]
  - [ ] P4: __________ [Date/Time]
- [ ] Send confirmation emails with:
  - [ ] Date, time, location
  - [ ] Duration (60 min)
  - [ ] Compensation details
  - [ ] What to bring (nothing specific, just themselves!)
  - [ ] Contact info if they need to reschedule

**Afternoon (4 hours)**
- [ ] Print all materials (4 copies each):
  - [ ] Consent forms (8 copies - 2 per participant)
  - [ ] Pre-session questionnaires (6 copies)
  - [ ] Post-session interview guides (6 copies)
  - [ ] Observation sheets (6 copies)
- [ ] Prepare digital versions (backups)
- [ ] Create folder system:
  ```
  /PilotStudy/
  ├── Materials/
  ├── PilotData/
  │   ├── P1/
  │   ├── P2/
  │   ├── P3/
  │   └── P4/
  └── Analysis/
  ```
- [ ] Acquire incentives
  - [ ] 4 × $25 gift cards
  - [ ] Receipt book (if needed)
  - [ ] Envelopes for gift cards

**Deliverable:** All materials ready, schedule confirmed

---

### Day 3 (Wednesday) - Technical Testing

**Morning (3 hours) - Platform Testing**
- [ ] Test internet connection at testing location
  - [ ] Speed test (minimum 10 Mbps recommended)
  - [ ] Test on actual device to be used
- [ ] Access platform: [Your URL]
- [ ] Test all 4 rooms:
  - [ ] Room 1 (Structured-Aware) loads correctly
  - [ ] Room 2 (Structured-Unaware) loads correctly
  - [ ] Room 3 (Exploratory-Aware) loads correctly
  - [ ] Room 4 (Exploratory-Unaware) loads correctly
- [ ] Verify room configurations:
  - [ ] Parameter displays visible in Rooms 1 & 3 only
  - [ ] No parameter displays in Rooms 2 & 4
  - [ ] AI behavior matches configuration
- [ ] Test complete session flow:
  - [ ] Login with test account
  - [ ] Select poetry form
  - [ ] Send several messages
  - [ ] Verify AI responds appropriately
  - [ ] End session
- [ ] Check data logging:
  - [ ] Messages saved to database
  - [ ] Session appears in admin dashboard
  - [ ] Export function works

**Afternoon (2 hours) - API & Admin Dashboard**
- [ ] Check OpenRouter API:
  - [ ] Account active: https://openrouter.ai/
  - [ ] Sufficient credits (estimate: $2.50/session × 4 = $10)
  - [ ] API key configured in Supabase
  - [ ] Test API call from platform
- [ ] Admin Dashboard testing:
  - [ ] Login to `/admin`
  - [ ] Navigate all tabs
  - [ ] Test export functions:
    - [ ] Export single conversation (JSON)
    - [ ] Export all data (JSON)
    - [ ] Export messages (CSV)
  - [ ] Verify analytics display
- [ ] Backup systems:
  - [ ] Prepare backup device
  - [ ] Install necessary software/browsers
  - [ ] Bookmark platform URL
  - [ ] Test login on backup device

**Evening (1 hour) - Documentation**
- [ ] Create testing log template
- [ ] Document any issues found today
- [ ] Create issue resolution list
- [ ] Update contact list (tech support, etc.)

**Deliverable:** Platform fully tested and verified working

---

### Day 4 (Thursday) - Environment & Recording Setup

**Morning (2 hours) - Physical Space**
- [ ] Secure testing room
  - [ ] Private, quiet location
  - [ ] Comfortable seating
  - [ ] Good lighting
  - [ ] Temperature control
- [ ] Set up workstation:
  - [ ] Computer/laptop positioned comfortably
  - [ ] External mouse (optional)
  - [ ] Large screen if available
  - [ ] Backup device nearby
  - [ ] Chargers plugged in
- [ ] Prepare facilitator station:
  - [ ] Chair positioned for observation (not hovering)
  - [ ] Small table for materials
  - [ ] Clipboard ready
- [ ] Prepare comfort items:
  - [ ] Water bottles
  - [ ] Tissues
  - [ ] Hand sanitizer
  - [ ] Snacks (optional, for longer sessions)
- [ ] Signage:
  - [ ] "Testing in Progress - Do Not Disturb"
  - [ ] Directional signs if needed

**Afternoon (3 hours) - Recording & Data Systems**
- [ ] If using audio recording:
  - [ ] Test recording device
  - [ ] Check audio quality
  - [ ] Test backup recording (phone app)
  - [ ] Prepare consent for recording
  - [ ] Create naming convention: `P#_Date_Interview.mp3`
- [ ] If using video/screen recording:
  - [ ] Test screen capture software
  - [ ] Check storage capacity
  - [ ] Ensure participant consent updated
- [ ] Data management:
  - [ ] Set up automatic backup (OneDrive, Dropbox, etc.)
  - [ ] Test backup timing
  - [ ] Create export templates
  - [ ] Prepare USB drive for manual backup
- [ ] Communication systems:
  - [ ] Test reminder system (calendar, email)
  - [ ] Prepare day-before reminder messages
  - [ ] Have participant contact info accessible

**Evening (1 hour) - Dry Run**
- [ ] Complete practice session:
  - [ ] Time each phase
  - [ ] Practice scripts out loud
  - [ ] Test observation note-taking
  - [ ] Test data export process
- [ ] Adjust timing if needed

**Deliverable:** Testing environment ready, recording systems functional

---

### Day 5 (Friday) - Facilitator Training & Final Prep

**Morning (3 hours) - Facilitator Training**
- [ ] Read all documentation thoroughly:
  - [ ] PILOT_TESTING_SCHEME.md
  - [ ] PILOT_TESTING_MANUAL.md
  - [ ] PILOT_TESTING_QUICKSTART.md
- [ ] Complete self-assessment (see Manual Section 2.3)
- [ ] Role-play scenarios:
  - [ ] Welcoming participant
  - [ ] Delivering tutorial (both Aware and Unaware versions)
  - [ ] Handling frustrated participant
  - [ ] Conducting interview
- [ ] Practice neutrality:
  - [ ] No judgment on poetry quality
  - [ ] No creative input
  - [ ] Non-leading interview questions
- [ ] Review ethical protocols:
  - [ ] Informed consent process
  - [ ] Right to withdraw
  - [ ] Data confidentiality
  - [ ] Mandatory reporting (if applicable)

**Afternoon (2 hours) - Final Systems Check**
- [ ] Re-test platform (quick check)
- [ ] Verify all 4 rooms one more time
- [ ] Check API credits
- [ ] Test admin dashboard
- [ ] Ensure all materials printed and organized
- [ ] Verify incentives ready
- [ ] Create session-day bag:
  - [ ] All printed materials
  - [ ] Pens (at least 3)
  - [ ] Clipboard
  - [ ] Recording device + batteries
  - [ ] Chargers
  - [ ] Water bottles
  - [ ] Timer/stopwatch
  - [ ] Business cards
  - [ ] This manual (printed or on tablet)

**Evening (1 hour) - Preparation**
- [ ] Send 24-hour reminder to P1:
  > "Hi [Name]! This is a friendly reminder about your participation in the poetry AI study tomorrow at [time] at [location]. Should take ~60 minutes. Looking forward to seeing you! Let me know if you have any questions. [Your name]"
- [ ] Review P1's assigned condition (Room 1 - Structured-Aware)
- [ ] Print P1's specific materials
- [ ] Mental preparation: Get good sleep!

**Deliverable:** Facilitator trained, all systems go for Monday

---

## WEEK 2: DATA COLLECTION

### Day 1 (Monday) - P1 Session

**2 Hours Before Session**
- [ ] Send reminder (if not sent day before)
- [ ] Set up testing room
- [ ] Boot up computer, open platform
- [ ] Navigate to Room 1 URL
- [ ] Test quick message
- [ ] Organize materials for P1
- [ ] Self-prep: restroom, water, focus

**1 Hour Before**
- [ ] Complete pre-session checklist (see Quick Start)
- [ ] Review Room 1 script (Structured-Aware)
- [ ] Silence phone
- [ ] Final environment check

**Session Hour**
- [ ] Welcome participant
- [ ] Follow 60-minute protocol:
  - 0-10: Welcome & consent
  - 10-15: Questionnaire
  - 15-20: Tutorial
  - 20-45: Writing session (OBSERVE)
  - 45-55: Interview
  - 55-60: Debrief
- [ ] Take detailed notes
- [ ] Stay neutral and supportive

**Immediately After**
- [ ] Thank participant warmly
- [ ] Export session data
- [ ] Transfer notes to digital
- [ ] Complete session summary
- [ ] Backup data
- [ ] Debrief: What went well? What to improve?

**Evening**
- [ ] Review day's data
- [ ] Send thank-you email to P1 (optional)
- [ ] Send reminder to P2 for tomorrow
- [ ] Review Room 2 script (Structured-Unaware)
- [ ] Rest!

---

### Day 2 (Tuesday) - P2 Session

**Follow same protocol as Day 1**

**Key differences:**
- [ ] P2 is in Room 2 (Structured-Unaware)
- [ ] Use Unaware tutorial script (no mention of parameters)
- [ ] Skip awareness-specific interview questions

**Evening reflection:**
- [ ] Compare P1 and P2 (both structured)
- [ ] Note differences between Aware/Unaware
- [ ] Prepare for Exploratory rooms (P3, P4)
- [ ] Send reminder to P3

---

### Day 3 (Wednesday) - P3 Session

**Follow same protocol**

**Key differences:**
- [ ] P3 is in Room 3 (Exploratory-Aware)
- [ ] Use Aware tutorial script (mention parameters)
- [ ] Expect more varied AI responses
- [ ] Include awareness questions in interview

**Evening reflection:**
- [ ] Compare Structured (P1, P2) vs. Exploratory (P3)
- [ ] Compare Aware conditions (P1 vs. P3)
- [ ] Prepare for final session
- [ ] Send reminder to P4

---

### Day 4 (Thursday) - P4 Session

**Follow same protocol**

**Key differences:**
- [ ] P4 is in Room 4 (Exploratory-Unaware)
- [ ] Use Unaware tutorial script
- [ ] Last session - celebrate completing data collection!

**Immediately After P4**
- [ ] Complete all post-session tasks
- [ ] Export ALL data from admin dashboard
- [ ] Create comprehensive backup
- [ ] Verify data integrity for all 4 participants
- [ ] Begin preliminary analysis

**Evening - Data Collection Complete! 🎉**
- [ ] Organize all materials
- [ ] Back up data to 3 locations
- [ ] Send thank-you emails to all participants
- [ ] Celebrate completion of data collection
- [ ] Plan analysis week

---

### Day 1 (Monday) - Data Compilation

**Morning (4 hours) - Data Organization**
- [ ] Verify all data collected:
  - [ ] All 4 consent forms
  - [ ] All 4 questionnaires
  - [ ] All 4 interview notes/recordings
  - [ ] All 4 observation sheets
  - [ ] All 4 conversation exports
- [ ] Transcribe interviews (if audio recorded)
- [ ] Digitize all handwritten notes
- [ ] Organize in folder structure
- [ ] Create master spreadsheet for quantitative data

**Afternoon (3 hours) - Quantitative Entry**
- [ ] Enter all metrics into analysis template:
  - [ ] Demographics (Section 1)
  - [ ] Session metrics (Section 2)
  - [ ] Poetry forms (Section 2)
  - [ ] Satisfaction ratings (Section 7)
- [ ] Calculate basic statistics:
  - [ ] Means, medians
  - [ ] Ranges
  - [ ] Percentages
- [ ] Create initial visualizations

**Deliverable:** All data digitized and organized

---

### Day 2 (Tuesday) - Initial Analysis

**Morning (3 hours) - Conversation Analysis**
- [ ] Read all 4 conversations completely
- [ ] Code interaction types (Type A/B/C)
- [ ] Identify critical moments
- [ ] Select representative excerpts
- [ ] Document patterns observed

**Afternoon (3 hours) - Qualitative Coding**
- [ ] Review all interview transcripts
- [ ] Apply theme coding (Section 5)
- [ ] Identify quotes for each theme
- [ ] Note emerging patterns
- [ ] Compare across conditions

**Evening**
- [ ] Preliminary observations document
- [ ] List initial insights

**Deliverable:** Coding complete, patterns identified

---

### Day 3 (Wednesday) - Deep Dive Analysis

**Morning (3 hours) - Condition Comparisons**
- [ ] Structured vs. Exploratory analysis (Section 6)
- [ ] Aware vs. Unaware analysis (Section 6)
- [ ] Create comparison tables
- [ ] Test initial hypotheses (Section 10)
- [ ] Document unexpected findings

**Afternoon (3 hours) - User Experience Analysis**
- [ ] Synthesize satisfaction data
- [ ] Identify what worked well
- [ ] Identify pain points
- [ ] Technical performance review
- [ ] Usability assessment

**Deliverable:** Comprehensive analysis complete

---

### Day 4 (Thursday) - Recommendations & Reporting

**Morning (3 hours) - Recommendations**
- [ ] System improvements (Section 11)
- [ ] Protocol adjustments
- [ ] Measures to add/remove
- [ ] AI prompt refinements
- [ ] Full study design recommendations

**Afternoon (4 hours) - Report Writing**
- [ ] Executive summary (Section 12)
- [ ] Write findings narrative
- [ ] Create final visualizations
- [ ] Format tables and figures
- [ ] Prepare appendices

**Deliverable:** Draft pilot study report

---

### Day 5 (Friday) - Finalization

**Morning (2 hours) - Review & Revise**
- [ ] Proofread report
- [ ] Check all data references
- [ ] Verify all calculations
- [ ] Ensure anonymization complete
- [ ] Review visualizations for clarity

**Afternoon (2 hours) - Dissemination**
- [ ] Prepare presentation slides (if needed)
- [ ] Share report with PI/team
- [ ] Schedule debrief meeting
- [ ] Archive all materials
- [ ] Final backup of everything

**Evening - Reflect & Celebrate! 🎉**
- [ ] What did you learn?
- [ ] What surprised you?
- [ ] What will you do differently in full study?
- [ ] Celebrate completing your pilot!

**Deliverable:** Final pilot study report, recommendations for full study

---

## MASTER CHECKLIST: Are You Ready?

### Before Starting Week 1

**Documentation:**
- [ ] IRB approval obtained (if required)
- [ ] Consent forms approved
- [ ] Data management plan finalized
- [ ] Research questions clearly defined

**Resources:**
- [ ] Budget allocated ($130+)
- [ ] Time blocked on calendar (3 weeks)
- [ ] Testing space secured
- [ ] Equipment available

**Knowledge:**
- [ ] Read all pilot testing documents
- [ ] Understand research design
- [ ] Know how to use platform
- [ ] Trained in ethical protocols

**Support:**
- [ ] PI/supervisor aware and supportive
- [ ] Technical support identified
- [ ] Backup facilitator available (optional)
- [ ] Participant pool identified

---

## Risk Mitigation

### What If...

**...you can't recruit 4 participants?**
- Extend recruitment period
- Expand inclusion criteria slightly
- Increase incentive
- Use convenience sample (but note limitation)

**...a participant no-shows?**
- Have backup participants on waitlist
- Reschedule if possible
- Continue with 3 participants (note in analysis)

**...technical issues prevent data collection?**
- Document thoroughly
- Reschedule session
- Use backup device
- Consider extending timeline

**...you get sick during data collection week?**
- Have backup facilitator trained
- Or: Reschedule all remaining sessions
- Communicate promptly with participants

**...data is lost?**
- This is why we backup immediately and frequently!
- Check all 3 backup locations
- Re-export from database if possible
- Document any data loss for analysis

---

## Success Tracking

### Weekly Goals

**Week 1:**
- [ ] 4 participants recruited and scheduled
- [ ] All materials prepared
- [ ] Platform fully tested
- [ ] Facilitator trained

**Week 2:**
- [ ] 4 sessions completed
- [ ] All data collected
- [ ] Data backed up (3 locations)
- [ ] Initial observations documented

**Week 3:**
- [ ] All data analyzed
- [ ] Report written
- [ ] Recommendations documented
- [ ] Ready for full study design

---

## Contact Information for Timeline

**Principal Investigator:**  
Name: _______________  
Email: _______________  
Phone: _______________

**Technical Support:**  
Name: _______________  
Email: _______________  
Phone: _______________

**Facilities/Room Booking:**  
Contact: _______________  
Phone: _______________

**Emergency Contact:**  
Name: _______________  
Phone: _______________

---

## Notes & Adjustments

**Timeline modifications:**
_________________________________________________________________
_________________________________________________________________

**Lessons learned during preparation:**
_________________________________________________________________
_________________________________________________________________

**Things to remember for next phase:**
_________________________________________________________________
_________________________________________________________________

---

**Good luck with your pilot study! Follow this timeline, stay organized, and you'll generate valuable insights for your research. You've got this! 💪🎉📊**

---

**Version 1.0 | Created: November 3, 2025**
