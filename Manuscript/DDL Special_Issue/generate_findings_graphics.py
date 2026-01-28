"""
Generate visualizations for Three-Phase Findings Report
Parameter-Configured AI Scaffolding in L2 Creative Writing
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.patches import Rectangle
import pandas as pd

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'sans-serif'

# Create output directory if it doesn't exist
import os
output_dir = 'figures'
os.makedirs(output_dir, exist_ok=True)

# ============================================================================
# Figure 1: Parameter Configuration Effect on Interaction Type Distribution
# ============================================================================

fig, ax = plt.subplots(figsize=(14, 8))

# Data
categories = ['Type A\n(Constraint Repair)', 'Type B\n(Exemplar Giving)', 'Type C\n(Surprise Harvest)']
structured = [60, 35, 5]
exploratory = [20, 45, 35]

x = np.arange(len(categories))
width = 0.35

# Create bars
bars1 = ax.bar(x - width/2, structured, width, label='Structured (T=0.3, Top-p=0.4)\n"Patient Tutor"', 
               color='#3498db', alpha=0.8, edgecolor='black', linewidth=1.5)
bars2 = ax.bar(x + width/2, exploratory, width, label='Exploratory (T=0.8, Top-p=0.9)\n"Creative Catalyst"', 
               color='#e74c3c', alpha=0.8, edgecolor='black', linewidth=1.5)

# Add value labels on bars
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}%',
                ha='center', va='bottom', fontweight='bold', fontsize=12)

# Add 7× annotation for Type C
ax.annotate('7× increase', xy=(2 + width/2, 35), xytext=(2 + width/2 + 0.5, 45),
            arrowprops=dict(arrowstyle='->', lw=2, color='red'),
            fontsize=13, fontweight='bold', color='red')

# Formatting
ax.set_ylabel('Percentage of Interactions (%)', fontsize=13, fontweight='bold')
ax.set_xlabel('Interaction Type', fontsize=13, fontweight='bold')
ax.set_title('Figure 1: Parameter Configuration Dramatically Reshapes Interaction Ecology\n' + 
             'χ²=24.3, p<.001, Cramér\'s V=.38', fontsize=15, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=12)
ax.legend(loc='upper left', fontsize=11, framealpha=0.9)
ax.set_ylim(0, 70)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig(f'{output_dir}/figure1_interaction_distribution.png', dpi=300, bbox_inches='tight')
print("✓ Figure 1 saved: Interaction Type Distribution")
plt.close()

# ============================================================================
# Figure 2: The Type B Paradox - Metrics Across Autonomy Gradient
# ============================================================================

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 12))

phases = ['Phase 1\n(Imposed)', 'Phase 2\n(Voluntary)', 'Phase 3\n(Autonomous)']
x_pos = np.arange(len(phases))

# Subplot 1: "Most Helpful" Rating
helpful_ratings = [75, 50, 33]
bars1 = ax1.barh(x_pos, helpful_ratings, color=['#e74c3c', '#f39c12', '#3498db'], 
                 alpha=0.8, edgecolor='black', linewidth=1.5)
ax1.set_yticks(x_pos)
ax1.set_yticklabels(phases, fontsize=11)
ax1.set_xlabel('Percentage Rating Type B "Most Helpful" (%)', fontsize=12, fontweight='bold')
ax1.set_title('"MOST HELPFUL" RATING (declining as autonomy increases)', 
              fontsize=12, fontweight='bold', loc='left')
ax1.set_xlim(0, 100)
for i, (bar, val) in enumerate(zip(bars1, helpful_ratings)):
    ax1.text(val + 2, bar.get_y() + bar.get_height()/2, f'{val}%', 
             va='center', fontweight='bold', fontsize=11)
ax1.grid(axis='x', alpha=0.3)

# Subplot 2: Authorship Perception
authorship_ranges = [(10, 35), (40, 40), (30, 50)]
authorship_means = [22.5, 40, 40]
bars2 = ax2.barh(x_pos, authorship_means, color=['#e74c3c', '#f39c12', '#3498db'], 
                 alpha=0.8, edgecolor='black', linewidth=1.5)
ax2.set_yticks(x_pos)
ax2.set_yticklabels(phases, fontsize=11)
ax2.set_xlabel('Authorship Perception (%)', fontsize=12, fontweight='bold')
ax2.set_title('AUTHORSHIP PERCEPTION (modest recovery when chosen)', 
              fontsize=12, fontweight='bold', loc='left')
ax2.set_xlim(0, 100)
# Add range annotations
for i, ((low, high), mean) in enumerate(zip(authorship_ranges, authorship_means)):
    if low != high:
        ax2.text(mean + 2, i, f'{low}-{high}%', va='center', fontweight='bold', fontsize=11)
    else:
        ax2.text(mean + 2, i, f'{mean:.0f}%', va='center', fontweight='bold', fontsize=11)
ax2.grid(axis='x', alpha=0.3)

# Subplot 3: Creative Satisfaction
satisfaction_scores = [3.6, 4.75, 4.75]
satisfaction_scaled = [s/5*100 for s in satisfaction_scores]
bars3 = ax2.barh(x_pos, satisfaction_scaled, color=['#e74c3c', '#f39c12', '#3498db'], 
                 alpha=0.8, edgecolor='black', linewidth=1.5)
colors_sat = ['#e74c3c', '#27ae60', '#27ae60']
bars3 = ax3.barh(x_pos, satisfaction_scaled, color=colors_sat, 
                 alpha=0.8, edgecolor='black', linewidth=1.5)
ax3.set_yticks(x_pos)
ax3.set_yticklabels(phases, fontsize=11)
ax3.set_xlabel('Creative Satisfaction (scaled to 100%)', fontsize=12, fontweight='bold')
ax3.set_title('CREATIVE SATISFACTION (dramatic jump with voluntary context)', 
              fontsize=12, fontweight='bold', loc='left')
ax3.set_xlim(0, 100)
emojis = ['😐', '😊', '😊']
for i, (bar, val, score, emoji) in enumerate(zip(bars3, satisfaction_scaled, satisfaction_scores, emojis)):
    ax3.text(val + 2, bar.get_y() + bar.get_height()/2, f'{score:.2f}/5  {emoji}', 
             va='center', fontweight='bold', fontsize=11)
# Add +0.75pts annotation
ax3.annotate('+0.75pts', xy=(95, 1), xytext=(85, 1.5),
            arrowprops=dict(arrowstyle='->', lw=2, color='green'),
            fontsize=11, fontweight='bold', color='green')
ax3.grid(axis='x', alpha=0.3)

fig.suptitle('Figure 2: The Type B Paradox—Helpful Yet Alienating Across Contexts\n' + 
             'THE PARADOX: Usefulness ⬆ yet Ownership ⬇  |  THE RESOLUTION: Autonomy transforms experience',
             fontsize=15, fontweight='bold', y=0.995)

plt.tight_layout()
plt.savefig(f'{output_dir}/figure2_type_b_paradox.png', dpi=300, bbox_inches='tight')
print("✓ Figure 2 saved: Type B Paradox")
plt.close()

# ============================================================================
# Figure 3: Authorship vs. AI Word Contribution (Mediated by Interaction Type)
# ============================================================================

fig, ax = plt.subplots(figsize=(14, 10))

# Data for Type C (high authorship despite high AI contribution)
type_c_participants = ['P 09', 'P 12', 'P 16', 'P 20', 'P 21']
type_c_ai_contrib = [40, 20, 50, 15, 4]
type_c_authorship = [80, 90, 50, 85, 96]

# Data for Type B (low authorship despite similar AI contribution)
type_b_participants = ['P 05/06', 'P 14', 'P 22']
type_b_ai_contrib = [40, 20, 80]
type_b_authorship = [15, 10, 20]

# Create scatter plot
scatter_c = ax.scatter(type_c_ai_contrib, type_c_authorship, s=300, alpha=0.7, 
                       c='#27ae60', edgecolors='black', linewidth=2, 
                       label='Type C: Iterative Reciprocity', marker='o', zorder=3)
scatter_b = ax.scatter(type_b_ai_contrib, type_b_authorship, s=300, alpha=0.7, 
                       c='#e74c3c', edgecolors='black', linewidth=2,
                       label='Type B: Passive Selection', marker='s', zorder=3)

# Add participant labels (using numbers only)
for i, (x, y) in enumerate(zip(type_c_ai_contrib, type_c_authorship)):
    participant_num = type_c_participants[i].replace('P ', '')
    ax.annotate(f'P{participant_num}\n({y}%)', xy=(x, y), xytext=(5, 5), 
                textcoords='offset points', fontsize=9, fontweight='bold')

for i, (x, y) in enumerate(zip(type_b_ai_contrib, type_b_authorship)):
    participant_num = type_b_participants[i].replace('P ', '')
    ax.annotate(f'P{participant_num}\n({y}%)', xy=(x, y), xytext=(5, -15), 
                textcoords='offset points', fontsize=9, fontweight='bold')

# Add zone labels
ax.text(15, 85, 'HIGH AUTHORSHIP\nDESPITE HIGH AI CONTRIBUTION', 
        fontsize=12, fontweight='bold', color='#27ae60', 
        bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.3))
ax.text(45, 15, 'LOW AUTHORSHIP\nDESPITE SIMILAR AI CONTRIBUTION', 
        fontsize=12, fontweight='bold', color='#e74c3c',
        bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.3))

# Formatting
ax.set_xlabel('AI Word Contribution (%)', fontsize=13, fontweight='bold')
ax.set_ylabel('Self-Attribution of Authorship (%)', fontsize=13, fontweight='bold')
ax.set_title('Figure 3: Authorship Perception Decoupled from Word Contribution\n' + 
             'KEY INSIGHT: Ownership = Procedural Control, NOT Word Count',
             fontsize=15, fontweight='bold', pad=20)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.legend(loc='upper right', fontsize=12, framealpha=0.9)
ax.grid(True, alpha=0.3)

# Add diagonal reference line (if word contribution = authorship)
ax.plot([0, 100], [100, 0], 'k--', alpha=0.3, linewidth=1, label='Expected if word count = authorship')

plt.tight_layout()
plt.savefig(f'{output_dir}/figure3_authorship_vs_contribution.png', dpi=300, bbox_inches='tight')
print("✓ Figure 3 saved: Authorship vs. Word Contribution")
plt.close()

# ============================================================================
# Figure 4: Dimensional Structure of Human-AI Creative Collaboration
# ============================================================================

fig, ax = plt.subplots(figsize=(14, 10))

dimensions = [
    'Concept/Theme',
    'Emotional Direction', 
    'Form/Structure',
    'Language/Words',
    'Final Decision'
]

human_control = [100, 80, 50, 30, 100]
ai_support = [0, 20, 50, 70, 0]

y_pos = np.arange(len(dimensions))
bar_height = 0.6

# Create stacked horizontal bars
bars_human = ax.barh(y_pos, human_control, bar_height, 
                     label='Human Control', color='#3498db', alpha=0.8,
                     edgecolor='black', linewidth=1.5)
bars_ai = ax.barh(y_pos, ai_support, bar_height, left=human_control,
                  label='AI Support', color='#e74c3c', alpha=0.8,
                  edgecolor='black', linewidth=1.5)

# Add value labels
for i, (human, ai) in enumerate(zip(human_control, ai_support)):
    # Human control label
    if human > 0:
        ax.text(human/2, i, f'{human}%', ha='center', va='center', 
                fontweight='bold', fontsize=12, color='white')
    # AI support label
    if ai > 0:
        ax.text(human + ai/2, i, f'{ai}%', ha='center', va='center',
                fontweight='bold', fontsize=12, color='white')

# Add dimension descriptions
descriptions = [
    'Universal human control',
    'Mostly human-directed',
    'Diverse individual preferences',
    'Minimal human (L2 contexts)',
    'Universal human authority'
]

for i, desc in enumerate(descriptions):
    ax.text(102, i, desc, va='center', fontsize=10, style='italic', color='gray')

# Formatting
ax.set_yticks(y_pos)
ax.set_yticklabels(dimensions, fontsize=12, fontweight='bold')
ax.set_xlabel('Control Distribution (%)', fontsize=13, fontweight='bold')
ax.set_title('Figure 4: Dimensional Structure of Human-AI Creative Collaboration\n' + 
             'CRITICAL INSIGHT: Single metrics like "60% self, 40% AI" collapse multi-dimensional reality',
             fontsize=15, fontweight='bold', pad=20)
ax.set_xlim(0, 120)
ax.legend(loc='lower right', fontsize=12, framealpha=0.9)
ax.grid(axis='x', alpha=0.3)

# Add key insight box
ax.text(60, -1.2, 'Authentic creative voice emerges from directional control over\nconceptual/emotional dimensions, not from generating every word',
        ha='center', fontsize=11, fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8, edgecolor='orange', linewidth=2))

plt.tight_layout()
plt.savefig(f'{output_dir}/figure4_dimensional_authorship.png', dpi=300, bbox_inches='tight')
print("✓ Figure 4 saved: Dimensional Authorship Structure")
plt.close()

# ============================================================================
# Bonus Figure: Cross-Phase Preference Evolution
# ============================================================================

fig, ax = plt.subplots(figsize=(14, 8))

phases = ['Phase 1\n(Imposed)', 'Phase 2\n(Voluntary)', 'Phase 3\n(Autonomous)']
exploratory_pref = [50, 75, 66.7]  # % choosing exploratory for personal writing
structured_pref = [50, 50, 58.3]   # % choosing structured for academic writing

x = np.arange(len(phases))
width = 0.35

bars1 = ax.bar(x - width/2, exploratory_pref, width, 
               label='Exploratory Atelier\n(Personal Creative Writing)', 
               color='#e74c3c', alpha=0.8, edgecolor='black', linewidth=1.5)
bars2 = ax.bar(x + width/2, structured_pref, width,
               label='Structured Studio\n(Academic Writing)',
               color='#3498db', alpha=0.8, edgecolor='black', linewidth=1.5)

# Add value labels
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{height:.1f}%',
                ha='center', va='bottom', fontweight='bold', fontsize=11)

# Formatting
ax.set_ylabel('Percentage of Participants (%)', fontsize=13, fontweight='bold')
ax.set_xlabel('Study Phase', fontsize=13, fontweight='bold')
ax.set_title('Bonus Figure: Strategic Parameter Preference Across Contexts\n' + 
             'Context-Sensitive Adaptation is Normative Learner Behavior',
             fontsize=15, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(phases, fontsize=12)
ax.legend(loc='upper left', fontsize=11, framealpha=0.9)
ax.set_ylim(0, 100)
ax.grid(axis='y', alpha=0.3)

# Add annotation about strategic switching
ax.annotate('62-75% demonstrate\ncontext-sensitive adaptation', 
            xy=(2, 66.7), xytext=(1.5, 85),
            arrowprops=dict(arrowstyle='->', lw=2, color='purple'),
            fontsize=11, fontweight='bold', color='purple',
            bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.8))

plt.tight_layout()
plt.savefig(f'{output_dir}/figure5_preference_evolution.png', dpi=300, bbox_inches='tight')
print("✓ Bonus Figure saved: Parameter Preference Evolution")
plt.close()

print("\n" + "="*60)
print("All figures generated successfully!")
print(f"Figures saved in: {os.path.abspath(output_dir)}/")
print("="*60)
