# AIED Conference Paper - Figures Documentation

This folder contains publication-quality visualizations for the AIED conference paper on **Parameter Configuration as Pedagogical Design Lever in AI-Assisted L2 Creative Writing**.

## Generated Figures

All figures are high-resolution PNG format (300 DPI) suitable for academic publication.

### Figure 1: Interaction Type Distribution Across Parameter Conditions
**File:** `figure1_interaction_distribution.png`  
**Size:** ~196 KB

**Description:** Bar chart comparing the distribution of three scaffolding interaction types (Repairing/Fixing, Exemplar Giving, Creative Divergence) across Structured Studio (T=0.25, P=0.35) and Exploratory Atelier (T=0.75, P=0.85) parameter conditions.

**Key Finding:** Demonstrates the **7-fold increase** in Type 3 (Creative Divergence) interactions in Exploratory vs. Structured conditions (35% vs 5%), with χ²=24.3, p<.001, Cramér's V=.38.

**Usage:** RQ1 - Parameter effects on interaction type distribution

---

### Figure 2: The Type 2 Paradox Across Three Phases
**File:** `figure2_type2_paradox.png`  
**Size:** ~212 KB

**Description:** Three-panel chart showing how Type 2 (Exemplar Giving) interactions manifest differently across Phase 1 (Imposed), Phase 2 (Voluntary), and Phase 3 (Autonomous) contexts, tracking:
- Perceived helpfulness (% rating "most helpful")
- Mean self-attribution/authorship (%)
- Creative satisfaction (1-5 scale)

**Key Finding:** Reveals the "helpful-but-alienating paradox" - Type 2 rated most helpful yet associated with lowest authorship. Shows transformation from frustration (Phase 1) to pragmatic acceptance (Phase 2-3) when learner autonomy increases.

**Usage:** RQ2 - Interaction type effects on authorship and satisfaction; Discussion of autonomy as meta-variable

---

### Figure 3: Type 3 Authorship Through Directional Control
**File:** `figure3_type3_authorship_scatter.png`  
**Size:** ~320 KB

**Description:** Scatter plot showing the relationship between AI word contribution (%) and self-attributed authorship (%) for five Type 3 (Creative Divergence) participants across all three phases. Bubble size represents satisfaction level; color intensity indicates number of rejection-refinement cycles.

**Key Finding:** Demonstrates **decoupling of authorship from word contribution**. Participants claim 50-96% authorship despite 4-50% AI word contribution. Includes diagonal reference line showing what proportional (word-based) authorship would look like, highlighting the gap.

**Usage:** RQ2 - Type 3 authorship mechanism; Discussion of directional control vs. proportional contribution

---

### Figure 4: Multi-Dimensional Authorship Structure
**File:** `figure4_dimensional_authorship.png`  
**Size:** ~247 KB

**Description:** Stacked bar chart disaggregating authorship across five creative dimensions:
- Concept/Theme (97.5% human, 2.5% AI)
- Emotional Direction (87.5% human, 12.5% AI)
- Form/Structure (55% human, 45% AI)
- Language/Words (35% human, 65% AI)
- Final Decision (100% human, 0% AI)

**Key Finding:** Shows that single authorship percentages collapse multi-dimensional reality. Learners maintain near-total control over conceptual/emotional dimensions (creative identity) while accepting substantial AI support for linguistic realization.

**Usage:** Discussion of why Type 3 preserves authorship despite AI involvement; Implications for assessment and AI detection

---

### Figure 5: Cross-Phase Progression of Key Metrics
**File:** `figure5_phase_progression.png`  
**Size:** ~252 KB

**Description:** Grouped bar chart tracking three metrics across Phase 1 (Experimental/Imposed), Phase 2 (Workshop/Voluntary), and Phase 3 (Autonomous):
- Satisfaction (scaled from 1-5 to 0-100% for comparison)
- Mean authorship claims (%)
- Exploratory parameter preference (%)

**Key Finding:** Demonstrates dramatic context effects:
- +0.75 point (+19%) satisfaction jump from imposed to voluntary contexts
- +39.8% increase in authorship claims from Phase 1 to Phase 3
- Sustained 66-75% preference for Exploratory parameters in voluntary contexts

**Usage:** Cross-phase synthesis; Discussion of autonomy effects and stable vs. context-dependent findings

---

### Figure 6: Strategic Parameter Selection Across Contexts
**File:** `figure6_parameter_preference_heatmap.png`  
**Size:** ~255 KB

**Description:** Heatmap showing percentage preferring Exploratory Atelier (vs. Structured Studio) across four writing contexts and three study phases:
- Personal Creative Writing
- Academic/Learning Tasks
- Grammar Confidence Building
- Creative Breakthrough

**Key Finding:** Reveals **context-sensitive strategic adaptation**. Learners prefer Exploratory for creative tasks (75-85%) but strategically switch to Structured for grammar support (20-30%), demonstrating metacognitive awareness of parameter effects.

**Usage:** Discussion of parameter literacy; Pedagogical recommendations for dual-mode architectures

---

## Regenerating Figures

To regenerate or modify figures, run:

```bash
python generate_figures.py
```

**Requirements:**
- Python 3.7+
- matplotlib
- numpy
- seaborn
- pandas

Install dependencies:
```bash
pip install matplotlib numpy seaborn pandas
```

## Data Sources

All visualizations are based on empirical data from:
- **N=30 participants** across three phases
- **900+ coded interactions**
- **20 feedback surveys** (67% response rate)
- **Chat log analysis** (quantitative coding)
- **Panel discussion transcripts** (qualitative themes)

Data sources referenced in `methodology_findings_discussion.md`.

## Figure Style Guidelines

- **Resolution:** 300 DPI (publication quality)
- **Format:** PNG (easily convertible to EPS/PDF if needed)
- **Color scheme:** Husl palette (color-blind friendly)
- **Font:** Serif (publication standard)
- **Annotations:** Included for key findings (effect sizes, statistical significance)

## Usage in Paper

Recommended figure placement in manuscript:

1. **Figure 1** → Section 4.1 (RQ1 findings)
2. **Figure 2** → Section 4.2 (Type 2 paradox)
3. **Figure 3** → Section 4.2 (Type 3 mechanism)
4. **Figure 4** → Section 4.2 (Dimensional authorship)
5. **Figure 5** → Section 4.3 (Cross-phase synthesis)
6. **Figure 6** → Section 5.3 (Pedagogical recommendations) or Appendix

**Note:** For 14-page conference limit, consider selecting 3-4 most critical figures (1, 3, 4, 5 recommended) and moving others to supplementary materials.

## Contact

For questions about figure generation or data visualization:
- See `generate_figures.py` for code details
- Modify plotting parameters to adjust aesthetics
- All data hardcoded in script based on findings analysis

---

**Last Updated:** January 29, 2026  
**Generated by:** generate_figures.py  
**Paper:** Parameter Configuration as Pedagogical Design Lever in AI-Assisted L2 Creative Writing
