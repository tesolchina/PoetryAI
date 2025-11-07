# Pilot Testing Quick Start Guide
## 4-Participant Study Overview

---

## 📋 At a Glance

**Study Purpose:** Test human-AI collaborative poetry writing with different AI configurations  
**Participants:** 4 people  
**Duration:** Session 1 (10 min login test) + Session 2 (25 min poetry chat)  
**Timeline:** 1 week preparation + 2 sessions per participant  
**Budget:** ~$130 ($100 incentives + $30 supplies)

---

## 🎯 Participant-Room Assignment

| ID | Name | Room | AI Style | Awareness | Date/Time |
|----|------|------|----------|-----------|-----------|
| P1 | ________ | Room 1 | Structured | Aware | ________ |
| P2 | ________ | Room 2 | Structured | Unaware | ________ |
| P3 | ________ | Room 3 | Exploratory | Aware | ________ |
| P4 | ________ | Room 4 | Exploratory | Unaware | ________ |

---

## ⏱️ Two-Session Flow

### SESSION 1: Login & Setup (10 minutes)
```
[3 min]  Welcome & Consent → Get participant comfortable, explain study, sign forms
    ↓
[3 min]  Questionnaire → Demographics, prior experience, attitudes
    ↓
[3 min]  Login Test → Practice logging in, verify account, test authentication
    ↓
[1 min]  Schedule Session 2 → Confirm time for poetry writing session
```

### SESSION 2: Poetry Writing (25 minutes)
```
[2 min]  Welcome Back → Brief recap, login to assigned room
    ↓
[2 min]  Tutorial → Show interface, explain poetry forms, answer questions
    ↓
[15 min] Poetry Writing → Participant works with AI (YOU OBSERVE)
    ↓
[5 min]  Interview → Ask about experience, challenges, insights
    ↓
[1 min]  Debrief → Explain conditions, thank, provide incentive
```

---

## ✅ Before Each Session Checklist

### SESSION 1 (Login Test) - 1 Hour Before:
- [ ] Test internet connection
- [ ] Verify authentication system working
- [ ] Print consent forms and questionnaires
- [ ] Prepare login test accounts (test phone numbers)
- [ ] Have Session 2 scheduling calendar ready

### SESSION 1 - 15 Minutes Before:
- [ ] Clean/organize testing space
- [ ] Put up "Testing in Progress" sign
- [ ] Set out water, tissues
- [ ] Silence your phone
- [ ] Have login instructions ready

### SESSION 2 (Poetry Chat) - 1 Hour Before:
- [ ] Test internet connection
- [ ] Open platform and verify assigned room loads
- [ ] Check OpenRouter API status and credits
- [ ] Set up recording device (if using)
- [ ] Prepare incentive ($25 gift card)

### SESSION 2 - 15 Minutes Before:
- [ ] Clean/organize testing space
- [ ] Put up "Testing in Progress" sign
- [ ] Set out water, tissues
- [ ] Open observation sheet
- [ ] Silence your phone
- [ ] Review participant's assigned room condition

---

## 🎤 Key Scripts

### SESSION 1 Scripts

**Welcome Script (Session 1)**
> "Hello [Name], welcome! Thank you for coming. This is the first of two short sessions. Today we'll just get you set up with the login system—it should only take 10 minutes. Then we'll schedule a second session where you'll actually create poetry with the AI. Sound good?"

**Login Test Script**
> "Let me show you how to log in. You'll use your phone number to authenticate. Let's try that now... [guide through login process]. Great! Now you know how to access the system. For our next session, you'll use this same login to access your poetry workspace."

**Session 2 Scheduling**
> "Perfect! You're all set up. Now let's schedule your poetry writing session. It will take about 25 minutes. When works best for you in the next few days?"

### SESSION 2 Scripts

**Welcome Back Script (Session 2)**
> "Welcome back [Name]! Ready to create some poetry? Let's log you in and get started."

**Tutorial - Aware Conditions (P1, P3)**
> "This is a chat interface where you'll talk with your AI poetry partner. You'll choose a poetry form and create together. **You'll see technical information about the AI's settings here**—feel free to ask about it if you're curious. I'll observe quietly. Questions?"

**Tutorial - Unaware Conditions (P2, P4)**
> "This is a chat interface where you'll talk with your AI poetry partner. You'll choose a poetry form and create together. I'll observe quietly. Questions?"

**Midpoint Check (7-8 min mark)**
> "You're doing great. Feel free to continue or try a different form if you'd like."

**Transition to Interview**
> "That's our time for writing—thank you! Let's talk about your experience. There are no wrong answers."

---

## 📝 Core Interview Questions (5 minutes - Session 2 only)

**Quick Interview (Session 2):**

1. **"How would you describe your experience working with the AI?"** → [Listen, probe]

2. **"What worked well? What was challenging?"** → [Identify pain points]

3. **"Did the AI help or hinder your creativity?"** → [Get examples]

4. **[AWARE ONLY] "You could see the parameter settings. Did that affect how you worked?"**

5. **"Would you use this again for creative writing?"** → [Future intent]

---

## 🔧 Common Tech Issues & Quick Fixes

| Problem | Solution |
|---------|----------|
| Can't log in | Check phone format: +1-555-0101 |
| Wrong room loaded | Immediately navigate to correct URL |
| AI not responding | Check internet → Refresh page → Check API status |
| Platform crashes | Refresh → Re-login → Note interruption time |
| Participant stuck | "Feel free to ask the AI for help" |

**Emergency contact:** [Your number]

---

## 📊 Data Collection Points

**Automatically Logged (by system):**
- All messages
- Session duration
- Poetry forms selected
- Timestamps

**You Must Collect:**
- Pre-session questionnaire (5 min)
- Observation notes (during session)
- Post-session interview (10 min, recorded if consent)

**Immediately After Session:**
- Export data from admin dashboard: `/admin`
- Save as: `P#_Date_Export.json`
- Back up to cloud
- Transfer handwritten notes to digital

---

## 🎯 Your Role During Sessions

### SESSION 1 (Login Test):
- Guide through authentication process
- Verify they can successfully log in
- Answer technical questions only
- Don't discuss poetry or AI yet
- Schedule Session 2 before they leave

### SESSION 2 (Poetry Writing - 15 min observation):

**✅ DO:**
- Sit nearby quietly
- Take observational notes
- Note engagement changes
- Document spontaneous comments
- Help ONLY with technical issues

**❌ DON'T:**
- Comment on their poetry
- Suggest topics or words
- Explain AI behavior (unless asked)
- Hover or distract
- Rush them

**If they seem stuck:** "Take your time. Feel free to ask the AI for ideas."

---

## 💾 Post-Session Tasks

### After SESSION 1 (Login Test):
1. **Verify login worked:**
   - Check participant account created
   - Note any authentication issues
   - Confirm Session 2 scheduled

2. **Quick notes:**
   - Any technical difficulties
   - Participant comfort with technology
   - Save questionnaire data

### After SESSION 2 (Poetry Writing):
1. **Export data:**
   - Log into admin dashboard
   - Navigate to "Participants" → Find P# → "View Chat" → "Export"
   - Save as: `P#_Date_Export.json`

2. **Transfer notes:**
   - Type up observation sheet
   - Type up interview notes (or transcribe recording)
   - Write session summary

3. **Backup:**
   - Local folder: `/PilotData/P#/`
   - Cloud storage

4. **Provide incentive:**
   - Give $25 gift card after Session 2 complete
   - Get receipt if needed

5. **Prepare for next:**
   - Review any issues
   - Restock materials
   - Update facilitator notes

---

## 📈 Success Indicators

**Session 1 Success:**
- ✅ Participant successfully logs in
- ✅ Authentication system works smoothly
- ✅ Participant comfortable with process
- ✅ Session 2 scheduled

**Session 2 Success:**
- ✅ Participant completes poetry session without major issues
- ✅ Data saved to database
- ✅ Export works
- ✅ Participant creates at least one poem or substantial writing
- ✅ Observable differences between room conditions

**Overall Success:**
- ✅ Participant reports positive experience (>3/5)
- ✅ No major frustrations
- ✅ Willing to recommend to others
- ✅ Rich insights from brief interview

---

## 🚨 When to Intervene

**ONLY intervene if:**
- Technical malfunction (screen freeze, no AI response)
- Participant explicitly asks for help
- Participant shows signs of distress (offer to pause/stop)
- Time management (5-minute warning)

**Otherwise:** Let them work naturally with AI

---

## 📞 Important Contacts

**Tech Support:** _______________  
**Principal Investigator:** _______________  
**IRB/Ethics:** _______________

---

## 🎁 Don't Forget

- [ ] Provide incentive at end (even if they quit early)
- [ ] Get email if they want findings summary
- [ ] Thank them warmly
- [ ] Remind them not to discuss with other potential participants

---

## 📚 Full Documentation

For detailed procedures, scripts, and forms, see:
- **`PILOT_TESTING_SCHEME.md`** - Complete research design
- **`PILOT_TESTING_MANUAL.md`** - Facilitator handbook with all forms

---

## 🎉 Quick Motivation

**Remember:**
- You're gathering valuable research data
- There are no "bad" sessions—every participant provides insights
- Technical issues happen—document and move forward
- Your neutrality is crucial—stay curious, not judgmental
- Each completed session is an achievement!

**You've got this! 💪**

---

**Version 1.0 | Last Updated: November 3, 2025**
