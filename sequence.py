# diagram_sequence.py

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

def create_protocol_sequence_diagram():
    """Crée un diagramme de séquence du protocole SET"""
    
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 120)
    ax.axis('off')
    
    # Définir les participants
    participants = ['Client', 'CA\n(Autorité Certification)', 'Banque', 'Système\nSET']
    participant_x = [10, 35, 60, 85]
    participant_y = 110
    
    # Dessiner les lignes de vie
    for i, (part, x) in enumerate(zip(participants, participant_x)):
        # Boîte du participant
        rect = FancyBboxPatch((x-5, participant_y-15), 10, 15, 
                              boxstyle="round,pad=0.1", 
                              facecolor='lightblue', 
                              edgecolor='black',
                              linewidth=2)
        ax.add_patch(rect)
        
        # Nom du participant
        ax.text(x, participant_y-7, part, ha='center', va='center', 
                fontsize=10, fontweight='bold')
        
        # Ligne de vie
        ax.plot([x, x], [participant_y-15, 10], 'k-', linewidth=1, alpha=0.5)
    
    # Étape 1: Demande de certification
    y = 100
    ax.annotate('1. Demande Certification', 
                xy=(participant_x[0], y), 
                xytext=(participant_x[1], y),
                arrowprops=dict(arrowstyle='->', color='blue', lw=2),
                fontsize=9, ha='center', va='center')
    
    # Étape 2: Certificat émis
    y = 90
    ax.annotate('2. Certificat Émis', 
                xy=(participant_x[1], y), 
                xytext=(participant_x[0], y),
                arrowprops=dict(arrowstyle='->', color='green', lw=2),
                fontsize=9, ha='center', va='center')
    
    # Étape 3: Création opérateur SET
    y = 80
    rect = patches.Rectangle((participant_x[0]-8, y-3), 16, 6, 
                             linewidth=1, edgecolor='purple', 
                             facecolor='yellow', alpha=0.3)
    ax.add_patch(rect)
    ax.text(participant_x[0], y, '3. Création Opérateur SET\n(OT + PC + Signature)', 
            ha='center', va='center', fontsize=8)
    
    # Étape 4: Envoi requête
    y = 70
    ax.annotate('4. Envoi Requête SET', 
                xy=(participant_x[0], y), 
                xytext=(participant_x[2], y),
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=9, ha='center', va='center')
    
    # Étape 5: Vérification
    y = 60
    rect = patches.Rectangle((participant_x[2]-8, y-3), 16, 6, 
                             linewidth=1, edgecolor='orange', 
                             facecolor='lightgreen', alpha=0.3)
    ax.add_patch(rect)
    ax.text(participant_x[2], y, '5. Vérification\n(Structure + Chiffrement)', 
            ha='center', va='center', fontsize=8)
    
    # Étape 6: Certification OK
    y = 50
    ax.text(participant_x[2], y, '6. Certification OK ✓', 
            ha='center', va='center', fontsize=9, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.3", facecolor="green", alpha=0.3))
    
    # Étape 7: Demande achat
    y = 40
    ax.annotate('7. Demande Achat\n(PC chiffré)', 
                xy=(participant_x[0], y), 
                xytext=(participant_x[2], y),
                arrowprops=dict(arrowstyle='->', color='brown', lw=2),
                fontsize=9, ha='center', va='center')
    
    # Étape 8: Achat 2 phases
    y = 30
    rect = patches.Rectangle((participant_x[2]-8, y-4), 16, 8, 
                             linewidth=1, edgecolor='purple', 
                             facecolor='pink', alpha=0.3)
    ax.add_patch(rect)
    ax.text(participant_x[2], y, '8. Achat 2 Phases\n(Autorisation + Capture)', 
            ha='center', va='center', fontsize=8)
    
    # Étape 9: Aide solidaire
    y = 25
    ax.annotate('9. Aide Solidaire + MEC', 
                xy=(participant_x[2], y), 
                xytext=(participant_x[3], y),
                arrowprops=dict(arrowstyle='->', color='gray', lw=1.5),
                fontsize=8, ha='center', va='center')
    
    # Étape 10: Enquête crise
    y = 20
    rect = patches.Rectangle((participant_x[3]-8, y-3), 16, 6, 
                             linewidth=1, edgecolor='red', 
                             facecolor='lightgray', alpha=0.3)
    ax.add_patch(rect)
    ax.text(participant_x[3], y, '10. Enquête Crise\n(Surveillance)', 
            ha='center', va='center', fontsize=8)
    
    # Étape 11: Confirmation
    y = 15
    ax.annotate('11. Confirmation Finale', 
                xy=(participant_x[2], y), 
                xytext=(participant_x[0], y),
                arrowprops=dict(arrowstyle='->', color='darkgreen', lw=3),
                fontsize=9, ha='center', va='center')
    
    # Ajouter une légende
    legend_elements = [
        patches.Patch(facecolor='lightblue', edgecolor='black', label='Participants'),
        patches.Patch(facecolor='yellow', alpha=0.3, edgecolor='purple', label='Traitement Local'),
        patches.Patch(facecolor='lightgreen', alpha=0.3, edgecolor='orange', label='Vérification'),
        patches.Patch(facecolor='green', alpha=0.3, label='Validation OK'),
        patches.Patch(facecolor='pink', alpha=0.3, edgecolor='purple', label='Processus Complexe')
    ]
    
    ax.legend(handles=legend_elements, loc='lower center', 
              bbox_to_anchor=(0.5, 0.02), ncol=3, fontsize=9)
    
    # Titre
    ax.set_title('Diagramme de Séquence - Protocole SET Complet', 
                 fontsize=16, fontweight='bold', pad=20)
    
    # Sous-titre
    ax.text(50, 115, 'Flux des 11 étapes du protocole SET', 
            ha='center', fontsize=12, style='italic')
    
    plt.tight_layout()
    plt.savefig('diagrams/set_sequence_diagram.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("✓ Diagramme de séquence généré: set_sequence_diagram.png")

if __name__ == '__main__':
    create_protocol_sequence_diagram()