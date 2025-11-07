# Pilot Study Export

**Export Date:** November 7, 2025  
**Source Repository:** dialog-analyze-engine (tesolchina/dialog-analyze-engine)  
**Source Branch:** main  
**Export Purpose:** Separate pilot testing materials into dedicated repository

---

## Contents

This folder contains all pilot testing documentation and participant materials for the Human-AI Collaborative Poetry Writing research platform pilot study (November 2025, 4 participants, 2×2 factorial design).

### Files Exported (12 total)

#### Core Pilot Documentation (7 files)
1. **PILOT_TESTING_SCHEME.md** - Complete research design, 2×2 factorial conditions, room configurations, participant recruitment, data collection methods, and analysis plan
2. **PILOT_TESTING_MANUAL.md** - Facilitator handbook with detailed session protocols, scripts, and procedures
3. **PILOT_TESTING_TIMELINE.md** - Week-by-week schedule, day-level checklists, and timeline for 4-week pilot
4. **PILOT_TESTING_README.md** - Overview and introduction to pilot testing materials
5. **PILOT_TESTING_QUICKSTART.md** - Quick reference guide for facilitators
6. **PILOT_DATA_ANALYSIS_TEMPLATE.md** - Framework and template for analyzing pilot data
7. **TWO_SESSION_APPROACH_SUMMARY.md** - Rationale and details for the two-session study design (Session 1: Login Testing; Session 2: Poetry Writing)

#### Participant Materials (5 files)
8. **PARTICIPANT_INFORMATION_FORM_TEMPLATE.md** - Complete Google Form template for pre-session questionnaire (demographics, prior experience, creative confidence)
9. **MANUAL_P1_STRUCTURED_AWARE.md** - Participant 1 manual (Structured AI, Parameter Aware, Room 1)
10. **MANUAL_P2_STRUCTURED_UNAWARE.md** - Participant 2 manual (Structured AI, Parameter Unaware, Room 2)
11. **MANUAL_P3_EXPLORATORY_AWARE.md** - Participant 3 manual (Exploratory AI, Parameter Aware, Room 3)
12. **MANUAL_P4_EXPLORATORY_UNAWARE.md** - Participant 4 manual (Exploratory AI, Parameter Unaware, Room 4)

---

## Study Design Summary

**Research Questions:**
- How do different AI parameter settings (structured vs. exploratory) affect collaborative poetry writing?
- Does parameter awareness influence participant trust, engagement, and creative output?
- What interaction patterns emerge in human-AI poetry collaboration?

**Design:** 2×2 factorial (Structured vs Exploratory × Aware vs Unaware)

**Participants:** 4 total
- P1: Structured-Aware (Temp 0.25, Top-P 0.35)
- P2: Structured-Unaware (Temp 0.30, Top-P 0.40)
- P3: Exploratory-Aware (Temp 0.75, Top-P 0.85)
- P4: Exploratory-Unaware (Temp 0.80, Top-P 0.90)

**Two-Session Structure:**
- **Session 1:** Login & Setup Testing (10 minutes) - verify authentication, collect demographics, build familiarity
- **Session 2:** Poetry Writing Session (25 minutes) - collaborative poetry creation, post-session interview

**Timeline:** 4 weeks
- Week 1: Preparation and recruitment
- Week 2: Session 1 (login tests for all 4 participants)
- Week 3: Session 2 (poetry writing for all 4 participants)
- Week 4: Data analysis and reporting

---

## Data Collection

**Automatic Platform Logging:**
- All conversation messages (user & AI)
- Poetry form selections
- Session timestamps and duration
- Interaction type classifications
- Room configuration data

**Manual Data Collection:**
- Pre-session questionnaire (Google Form)
- Post-session interview (5 minutes, audio recorded with consent)
- Facilitator observational notes

**Export Formats:**
- Conversation JSON: `P#_[Date]_Export.json`
- Interview audio: `P#_[Date]_Interview.mp3`
- Observational notes: per session

---

## Provenance & Version Control

**Original Location:** `c:\Users\ruobin Yu\.vscode\dialog-analyze-engine-2\` (root directory)

**Files remain in original repository:** Yes (this is a copy, originals preserved for now)

**Git History:** These files can be moved to a new repository while preserving or discarding commit history depending on need:
- **Preserve history:** Use `git filter-branch` or `git subtree split` to extract files with full commit history
- **Fresh start:** Copy files to new repo as initial commit (recommended for clean separation)

**Related Code/Platform Files NOT Included:**
- Source code (`src/` directory)
- Database schemas (`supabase/migrations/`)
- Configuration files (`vite.config.ts`, `package.json`, etc.)
- Admin dashboard components
- Poetry AI integration code

These pilot materials focus on **research protocols and participant documentation only**, not technical implementation.

---

## Next Steps

### Option A: Create New GitHub Repository (Recommended)

1. **Create new repository on GitHub:**
   - Name suggestion: `poetry-ai-pilot-study` or `dialog-analyze-pilot-testing`
   - Visibility: Private (contains participant protocols)
   - Initialize: No (you'll push existing files)

2. **Initialize local git repository in this folder:**
   ```powershell
   cd "c:\Users\ruobin Yu\.vscode\dialog-analyze-engine-2\pilot_study_export"
   git init
   git add .
   git commit -m "Initial commit: Pilot testing materials for Human-AI Poetry Writing study (Nov 2025)"
   ```

3. **Add GitHub remote and push:**
   ```powershell
   git remote add origin https://github.com/tesolchina/[NEW-REPO-NAME].git
   git branch -M main
   git push -u origin main
   ```

4. **Optional: Remove originals from main repository**
   After verifying successful push to new repository:
   ```powershell
   cd "c:\Users\ruobin Yu\.vscode\dialog-analyze-engine-2"
   git rm PILOT_TESTING_*.md TWO_SESSION_APPROACH_SUMMARY.md PILOT_DATA_ANALYSIS_TEMPLATE.md MANUAL_P*.md PARTICIPANT_INFORMATION_FORM_TEMPLATE.md
   git commit -m "Move pilot testing materials to dedicated repository"
   git push origin main
   ```

### Option B: Keep in Current Repository (Not Recommended)
- Files remain in `dialog-analyze-engine` repository
- Increases repository size with non-code documentation
- Mixes research protocols with platform codebase

---

## Safety & Privacy Notes

⚠️ **Before pushing to any remote repository:**
1. Verify no participant identifying information is present in files
2. Ensure consent forms and actual data are NOT included (templates only)
3. Check that no API keys, credentials, or tokens are embedded
4. Consider repository visibility (recommend: Private)

✅ **Current state:** All files contain templates, protocols, and procedures only. No actual participant data included.

---

## File Integrity Verification

**Total files:** 12  
**Total size:** Run `Get-ChildItem -Recurse | Measure-Object -Property Length -Sum` to calculate

**Checksum verification (optional):**
```powershell
Get-FileHash -Path *.md -Algorithm SHA256 | Format-Table -AutoSize
```

---

## Contact & Ownership

**Principal Investigator:** [To be added]  
**Repository Maintainer:** ruobin Yu (tesolchina)  
**Study Period:** November 2025  
**Platform:** Human-AI Collaborative Poetry Writing Research Platform

---

## Version History

**v1.0** (November 7, 2025)
- Initial export from `dialog-analyze-engine` repository
- 12 files: 7 core pilot docs + 5 participant materials
- Includes two-session approach (login testing + poetry writing)
- Ready for independent repository creation

---

**End of README**
