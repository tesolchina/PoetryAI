"""
Generate research figures for the PoetryAI preliminary results essay
Using matplotlib to create publication-quality charts
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import matplotlib.patches as mpatches

# Set style for academic publications
plt.style.use('seaborn-v0_8-paper')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['figure.dpi'] = 300

# Create output directory
output_dir = Path("Manuscript/graphies")
output_dir.mkdir(exist_ok=True)

def figure1_interaction_distribution():
    """Figure 1: Interaction Type Distribution by Parameter Configuration"""
    
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Data
    categories = ['Type A\nConstraint Repair', 'Type B\nExemplar Giving', 'Type C\nSurprise Harvest']
    low_temp = [60, 35, 5]
    high_temp = [20, 45, 35]
    
    x = np.arange(len(categories))
    width = 0.35
    
    # Create bars
    bars1 = ax.bar(x - width/2, low_temp, width, label='Low Temperature (0.3/0.4)', 
                   color='#4472C4', alpha=0.8)
    bars2 = ax.bar(x + width/2, high_temp, width, label='High Temperature (0.8/0.9)', 
                   color='#ED7D31', alpha=0.8)
    
    # Add value labels on bars
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height)}%',
                   ha='center', va='bottom', fontsize=9)
    
    # Highlight the 7x difference in Type C
    ax.annotate('', xy=(2.17, 35), xytext=(2.17, 5),
                arrowprops=dict(arrowstyle='<->', color='red', lw=2))
    ax.text(2.5, 20, '7× difference', color='red', fontsize=9, 
            rotation=90, va='center')
    
    ax.set_ylabel('Percentage of Interactions (%)', fontweight='bold')
    ax.set_title('Interaction Type Distribution by Parameter Configuration', 
                 fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend(loc='upper left', frameon=True)
    ax.set_ylim(0, 70)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    plt.savefig(output_dir / 'fig1_interaction_distribution.png', dpi=300, bbox_inches='tight')
    plt.savefig(output_dir / 'fig1_interaction_distribution.pdf', bbox_inches='tight')
    print("✓ Generated Figure 1: Interaction Type Distribution")
    plt.close()


def figure2_authorship_satisfaction():
    """Figure 2: Authorship Perception and Satisfaction by Parameter Configuration"""
    
    fig, ax1 = plt.subplots(figsize=(8, 5))
    
    # Data
    conditions = ['Low Temperature\n(0.3/0.4)', 'High Temperature\n(0.8/0.9)']
    authorship = [15, 62.5]  # Using midpoint for low temp range (10-20%)
    satisfaction = [2.0, 4.75]
    
    x = np.arange(len(conditions))
    width = 0.35
    
    # Authorship bars (left y-axis)
    color1 = '#5B9BD5'
    bars = ax1.bar(x - width/2, authorship, width, label='Self-Authorship', 
                   color=color1, alpha=0.8)
    ax1.set_ylabel('Self-Authorship Perception (%)', color=color1, fontweight='bold')
    ax1.set_ylim(0, 80)
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.set_xticks(x)
    ax1.set_xticklabels(conditions)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}%',
                ha='center', va='bottom', fontsize=9)
    
    # Satisfaction line (right y-axis)
    ax2 = ax1.twinx()
    color2 = '#ED7D31'
    line = ax2.plot(x + width/2, satisfaction, marker='o', markersize=8, 
                    linewidth=2.5, color=color2, label='Satisfaction Rating')
    ax2.set_ylabel('Satisfaction Rating (out of 5)', color=color2, fontweight='bold')
    ax2.set_ylim(0, 5.5)
    ax2.tick_params(axis='y', labelcolor=color2)
    
    # Add value labels on line points
    for i, (xi, yi) in enumerate(zip(x + width/2, satisfaction)):
        ax2.text(xi, yi + 0.2, f'{yi:.2f}/5', ha='center', fontsize=9, color=color2)
    
    # Add annotations for key differences
    ax1.annotate('', xy=(-0.17, 62.5), xytext=(-0.17, 15),
                arrowprops=dict(arrowstyle='<->', color='darkblue', lw=1.5))
    ax1.text(-0.5, 38, '6× higher', color='darkblue', fontsize=8, 
            rotation=90, va='center')
    
    ax2.annotate('', xy=(1.32, 4.75), xytext=(1.32, 2.0),
                arrowprops=dict(arrowstyle='<->', color='darkred', lw=1.5))
    ax2.text(1.65, 3.4, '90% gap', color='darkred', fontsize=8, 
            rotation=90, va='center')
    
    ax1.set_title('Authorship Perception and Satisfaction by Parameter Configuration',
                  fontweight='bold', pad=15)
    ax1.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Combined legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', frameon=True)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'fig2_authorship_satisfaction.png', dpi=300, bbox_inches='tight')
    plt.savefig(output_dir / 'fig2_authorship_satisfaction.pdf', bbox_inches='tight')
    print("✓ Generated Figure 2: Authorship and Satisfaction")
    plt.close()


def figure3_three_types_framework():
    """Figure 3: Three Interaction Types Framework (Conceptual Diagram)"""
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Define boxes
    boxes = [
        {
            'pos': (0.5, 5.5), 'width': 2.8, 'height': 1.8,
            'title': 'Type A:\nConstraint Repair',
            'text': 'AI identifies structural/\nlinguistic issues,\nprovides corrections',
            'theory': '(Lyster & Ranta, 1997)',
            'color': '#C5E0B4'
        },
        {
            'pos': (3.6, 5.5), 'width': 2.8, 'height': 1.8,
            'title': 'Type B:\nExemplar Giving',
            'text': 'AI provides model texts,\nline options for\nselection/adaptation',
            'theory': '(Hanauer, 2010)',
            'color': '#FFE699'
        },
        {
            'pos': (6.7, 5.5), 'width': 2.8, 'height': 1.8,
            'title': 'Type C:\nSurprise Harvest',
            'text': 'AI generates unexpected\npossibilities, inspires\nnew creative directions',
            'theory': '(Coenen et al., 2022)',
            'color': '#F4B084'
        }
    ]
    
    # Draw boxes
    for box in boxes:
        rect = mpatches.FancyBboxPatch(box['pos'], box['width'], box['height'],
                                       boxstyle="round,pad=0.1", 
                                       edgecolor='black', facecolor=box['color'],
                                       linewidth=1.5, alpha=0.7)
        ax.add_patch(rect)
        
        # Add text
        center_x = box['pos'][0] + box['width']/2
        center_y = box['pos'][1] + box['height']/2
        
        ax.text(center_x, center_y + 0.5, box['title'], 
               ha='center', va='center', fontsize=11, fontweight='bold')
        ax.text(center_x, center_y - 0.15, box['text'], 
               ha='center', va='center', fontsize=8)
        ax.text(center_x, box['pos'][1] + 0.15, box['theory'], 
               ha='center', va='bottom', fontsize=7, style='italic')
    
    # Add parameter influence arrows
    ax.arrow(2.0, 4.8, 0, -1.2, head_width=0.2, head_length=0.15, 
            fc='#4472C4', ec='#4472C4', linewidth=2)
    ax.text(2.0, 3.3, 'Dominant at\nLow Temp\n(60%)', ha='center', fontsize=8, 
           color='#4472C4', fontweight='bold')
    
    ax.arrow(8.0, 4.8, 0, -1.2, head_width=0.2, head_length=0.15, 
            fc='#ED7D31', ec='#ED7D31', linewidth=2)
    ax.text(8.0, 3.3, 'Dominant at\nHigh Temp\n(35%)', ha='center', fontsize=8, 
           color='#ED7D31', fontweight='bold')
    
    # Title
    ax.text(5.0, 7.5, 'Three Interaction Types in AI-Assisted L2 Poetry Writing',
           ha='center', fontsize=13, fontweight='bold')
    
    # Add legend for parameter influence
    ax.text(5.0, 2.0, 'Parameter Configuration Influences Interaction Type Distribution',
           ha='center', fontsize=9, style='italic', 
           bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))
    
    plt.tight_layout()
    plt.savefig(output_dir / 'fig3_three_types_framework.png', dpi=300, bbox_inches='tight')
    plt.savefig(output_dir / 'fig3_three_types_framework.pdf', bbox_inches='tight')
    print("✓ Generated Figure 3: Three Types Framework")
    plt.close()


def figure4_type_c_prediction():
    """Figure 4: Type C Presence Predicts Authorship and Satisfaction"""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Data points
    type_c = [5, 35]
    authorship = [15, 62.5]
    satisfaction = [2.0, 4.75]
    labels = ['Low Temp\n(Rooms A, B)', 'High Temp\n(Rooms C, D)']
    colors = ['#4472C4', '#ED7D31']
    
    # Left plot: Type C vs Authorship
    for i, (x, y, label, color) in enumerate(zip(type_c, authorship, labels, colors)):
        ax1.scatter(x, y, s=300, alpha=0.7, color=color, edgecolors='black', linewidth=1.5)
        ax1.annotate(label, xy=(x, y), xytext=(10, 10), textcoords='offset points',
                    fontsize=8, ha='left')
    
    # Add trend line
    z = np.polyfit(type_c, authorship, 1)
    p = np.poly1d(z)
    x_line = np.linspace(0, 40, 100)
    ax1.plot(x_line, p(x_line), "--", color='gray', linewidth=1.5, alpha=0.5)
    
    ax1.set_xlabel('Type C Interaction Percentage (%)', fontweight='bold')
    ax1.set_ylabel('Self-Authorship Perception (%)', fontweight='bold')
    ax1.set_title('Type C Predicts Authorship', fontweight='bold')
    ax1.grid(alpha=0.3, linestyle='--')
    ax1.set_xlim(-5, 45)
    ax1.set_ylim(0, 75)
    
    # Add correlation annotation
    ax1.text(20, 10, 'Positive correlation:\n4-6× higher authorship\nwith increased Type C',
            ha='center', fontsize=8, bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.3))
    
    # Right plot: Type C vs Satisfaction
    for i, (x, y, label, color) in enumerate(zip(type_c, satisfaction, labels, colors)):
        ax2.scatter(x, y, s=300, alpha=0.7, color=color, edgecolors='black', linewidth=1.5)
        ax2.annotate(label, xy=(x, y), xytext=(10, 10), textcoords='offset points',
                    fontsize=8, ha='left')
    
    # Add trend line
    z2 = np.polyfit(type_c, satisfaction, 1)
    p2 = np.poly1d(z2)
    ax2.plot(x_line, p2(x_line), "--", color='gray', linewidth=1.5, alpha=0.5)
    
    ax2.set_xlabel('Type C Interaction Percentage (%)', fontweight='bold')
    ax2.set_ylabel('Satisfaction Rating (out of 5)', fontweight='bold')
    ax2.set_title('Type C Predicts Satisfaction', fontweight='bold')
    ax2.grid(alpha=0.3, linestyle='--')
    ax2.set_xlim(-5, 45)
    ax2.set_ylim(0, 5.5)
    
    # Add correlation annotation
    ax2.text(20, 0.5, 'Positive correlation:\n>2× higher satisfaction\nwith increased Type C',
            ha='center', fontsize=8, bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.3))
    
    plt.suptitle('Type C Presence Predicts Authorship and Satisfaction Outcomes',
                fontsize=13, fontweight='bold', y=1.02)
    
    plt.tight_layout()
    plt.savefig(output_dir / 'fig4_type_c_prediction.png', dpi=300, bbox_inches='tight')
    plt.savefig(output_dir / 'fig4_type_c_prediction.pdf', bbox_inches='tight')
    print("✓ Generated Figure 4: Type C Prediction")
    plt.close()


def main():
    """Generate all four figures"""
    print("=== Generating Research Figures for PoetryAI Study ===\n")
    
    try:
        figure1_interaction_distribution()
        figure2_authorship_satisfaction()
        figure3_three_types_framework()
        figure4_type_c_prediction()
        
        print(f"\n✓ All figures generated successfully!")
        print(f"✓ Saved to: {output_dir.absolute()}")
        print(f"✓ Formats: PNG (300 DPI) and PDF")
        
    except Exception as e:
        print(f"✗ Error generating figures: {e}")
        raise


if __name__ == "__main__":
    main()
