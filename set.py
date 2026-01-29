# diagram_state_machine.py

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, FancyBboxPatch, ArrowStyle

def create_state_machine_diagram():
    """Crée un diagramme d'état du protocole SET"""
    
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    # Titre
    ax.text(50, 98, 'Machine à États - Protocole SET Banking', 
            fontsize=16, fontweight='bold', ha='center')
    
    # États principaux
    states = {
        'INIT': {'pos': (10, 50), 'color': 'lightgray', 'final': False},
        'CERT_REQUEST': {'pos': (25, 75), 'color': 'lightblue', 'final': False},
        'CERT_ACTIVE': {'pos': (40, 75), 'color': 'lightgreen', 'final': False},
        'SET_CREATED': {'pos': (25, 50), 'color': 'yellow', 'final': False},
        'REQUEST_SENT': {'pos': (40, 50), 'color': 'orange', 'final': False},
        'VERIFIED': {'pos': (55, 50), 'color': 'lightgreen', 'final': False},
        'PAYMENT_REQUEST': {'pos': (55, 25), 'color': 'pink', 'final': False},
        'AUTH_PHASE1': {'pos': (70, 25), 'color': 'lightcoral', 'final': False},
        'AUTH_PHASE2': {'pos': (70, 40), 'color': 'violet', 'final': False},
        'SYSTEM_PROCESS': {'pos': (85, 40), 'color': 'cyan', 'final': False},
        'COMPLETED': {'pos': (90, 50), 'color': 'darkgreen', 'final': True},
        'ERROR': {'pos': (50, 10), 'color': 'red', 'final': True},
        'REVOKED': {'pos': (25, 25), 'color': 'darkred', 'final': True}
    }
    
    # Dessiner les états
    for state_name, state_info in states.items():
        x, y = state_info['pos']
        color = state_info['color']
        
        if state_info['final']:
            # État final - double cercle
            circle_outer = Circle((x, y), 8, 
                                 facecolor=color, 
                                 edgecolor='black',
                                 linewidth=2, alpha=0.8)
            circle_inner = Circle((x, y), 6.5, 
                                 facecolor='white', 
                                 edgecolor='black',
                                 linewidth=1, alpha=0.9)
            ax.add_patch(circle_outer)
            ax.add_patch(circle_inner)
        else:
            # État normal - cercle simple
            circle = Circle((x, y), 8, 
                           facecolor=color, 
                           edgecolor='black',
                           linewidth=2, alpha=0.8)
            ax.add_patch(circle)
        
        # Nom de l'état
        ax.text(x, y, state_name.replace('_', '\n'), 
               ha='center', va='center', 
               fontsize=9, fontweight='bold')
        
        # Description courte
        descriptions = {
            'INIT': 'Initialisation',
            'CERT_REQUEST': 'Demande\nCertificat',
            'CERT_ACTIVE': 'Certificat\nActif',
            'SET_CREATED': 'Opérateur\nSET Créé',
            'REQUEST_SENT': 'Requête\nEnvoyée',
            'VERIFIED': 'Vérifié\npar Banque',
            'PAYMENT_REQUEST': 'Demande\nPaiement',
            'AUTH_PHASE1': 'Autorisation\nPhase 1',
            'AUTH_PHASE2': 'Capture\nPhase 2',
            'SYSTEM_PROCESS': 'Traitement\nSystème',
            'COMPLETED': 'Transaction\nTerminée',
            'ERROR': 'Erreur\nTransaction',
            'REVOKED': 'Certificat\nRévoqué'
        }
        
        if state_name in descriptions:
            ax.text(x, y - 10, descriptions[state_name], 
                   ha='center', va='top', fontsize=7)
    
    # Transitions
    transitions = [
        # Flux principal
        ('INIT', 'CERT_REQUEST', '1. Demande\nCertificat'),
        ('CERT_REQUEST', 'CERT_ACTIVE', '2. Certificat\nÉmis'),
        ('CERT_ACTIVE', 'SET_CREATED', '3. Création\nOpérateur SET'),
        ('SET_CREATED', 'REQUEST_SENT', '4. Envoi\nRequête'),
        ('REQUEST_SENT', 'VERIFIED', '5. Vérification\nBanque'),
        ('VERIFIED', 'PAYMENT_REQUEST', '7. Demande\nPaiement'),
        ('PAYMENT_REQUEST', 'AUTH_PHASE1', '8. Phase 1\nAutorisation'),
        ('AUTH_PHASE1', 'AUTH_PHASE2', '8. Phase 2\nCapture'),
        ('AUTH_PHASE2', 'SYSTEM_PROCESS', '9. Traitement\nSystème'),
        ('SYSTEM_PROCESS', 'COMPLETED', '11. Confirmation\nFinale'),
        
        # Transitions d'erreur
        ('CERT_REQUEST', 'ERROR', 'Échec\nCertification'),
        ('VERIFIED', 'ERROR', 'Vérification\nÉchouée'),
        ('PAYMENT_REQUEST', 'ERROR', 'Paiement\nRefusé'),
        ('AUTH_PHASE1', 'ERROR', 'Autorisation\nRefusée'),
        ('AUTH_PHASE2', 'ERROR', 'Capture\nÉchouée'),
        
        # Transitions de révocation
        ('CERT_ACTIVE', 'REVOKED', 'Certificat\nRévoqué'),
        ('SET_CREATED', 'REVOKED', 'Certificat\nExpiré'),
        
        # Boucles et retours
        ('ERROR', 'INIT', 'Nouvelle\nTentative'),
        ('REVOKED', 'CERT_REQUEST', 'Nouvelle\nDemande'),
        
        # Traitement système (étape 10)
        ('SYSTEM_PROCESS', 'SYSTEM_PROCESS', '10. Enquête\nCrise', 'loop'),
    ]
    
    # Dessiner les transitions
    for trans in transitions:
        if len(trans) == 4:
            src, dst, label, trans_type = trans
        else:
            src, dst, label = trans
            trans_type = 'normal'
        
        src_x, src_y = states[src]['pos']
        dst_x, dst_y = states[dst]['pos']
        
        if trans_type == 'loop':
            # Transition en boucle
            loop_radius = 15
            loop_x, loop_y = src_x, src_y + loop_radius
            
            # Dessiner la boucle
            arc = mpatches.Arc((src_x, src_y + loop_radius/2), 
                              loop_radius*2, loop_radius, 
                              angle=0, theta1=180, theta2=360,
                              linewidth=2, color='blue', 
                              fill=False)
            ax.add_patch(arc)
            
            # Flèche
            arrow_x, arrow_y = src_x, src_y + loop_radius
            ax.annotate('', xy=(src_x + 3, src_y + loop_radius - 3),
                       xytext=(src_x - 3, src_y + loop_radius - 3),
                       arrowprops=dict(arrowstyle='->', color='blue', lw=2))
            
            # Label
            ax.text(src_x, src_y + loop_radius + 5, label,
                   ha='center', va='bottom', fontsize=7,
                   bbox=dict(boxstyle="round,pad=0.3", 
                            facecolor="white", 
                            edgecolor="blue", 
                            alpha=0.8))
            
        else:
            # Transition normale
            # Calculer l'angle et ajuster le point de départ/arrivée
            dx, dy = dst_x - src_x, dst_y - src_y
            dist = (dx**2 + dy**2)**0.5
            
            if dist > 0:
                # Ajuster pour le rayon des cercles (8)
                adjust = 8 / dist
                start_x = src_x + dx * adjust
                start_y = src_y + dy * adjust
                end_x = dst_x - dx * adjust
                end_y = dst_y - dy * adjust
            else:
                start_x, start_y = src_x, src_y
                end_x, end_y = dst_x, dst_y
            
            # Dessiner la flèche
            arrow_color = 'green' if 'ERROR' not in label and 'REVOKED' not in label else 'red'
            
            ax.annotate('', xy=(end_x, end_y), 
                       xytext=(start_x, start_y),
                       arrowprops=dict(arrowstyle='->', 
                                     color=arrow_color, 
                                     lw=2,
                                     alpha=0.7))
            
            # Label au milieu
            mid_x, mid_y = (start_x + end_x) / 2, (start_y + end_y) / 2
            
            # Ajuster la position du label pour éviter les chevauchements
            if dy > 0:  # Vers le haut
                label_x, label_y = mid_x, mid_y + 5
            else:  # Vers le bas
                label_x, label_y = mid_x, mid_y - 5
            
            ax.text(label_x, label_y, label,
                   ha='center', va='center', fontsize=7,
                   bbox=dict(boxstyle="round,pad=0.3", 
                            facecolor="white", 
                            edgecolor=arrow_color, 
                            alpha=0.8))
    
    # Légende
    legend_elements = [
        Circle((0, 0), 0.5, facecolor='lightgray', label='État Initial'),
        Circle((0, 0), 0.5, facecolor='lightgreen', label='État Normal'),
        Circle((0, 0), 0.5, facecolor='darkgreen', label='État Final (Succès)'),
        Circle((0, 0), 0.5, facecolor='red', label='État Final (Erreur)'),
        mpatches.FancyArrow(0, 0, 1, 0, color='green', label='Transition Normale'),
        mpatches.FancyArrow(0, 0, 1, 0, color='red', label='Transition d\'Erreur'),
        mpatches.FancyArrow(0, 0, 1, 0, color='blue', label='Transition en Boucle'),
    ]
    
    ax.legend(handles=legend_elements, loc='lower center', 
              bbox_to_anchor=(0.5, 0.02), ncol=4, fontsize=8)
    
    # Zone d'information
    info_box = FancyBboxPatch((5, 85), 90, 10,
                             boxstyle="round,pad=0.5",
                             facecolor='lightyellow',
                             edgecolor='orange',
                             linewidth=2,
                             alpha=0.9)
    ax.add_patch(info_box)
    
    info_text = "Protocole SET - 11 États Principaux\n" \
               "Flux normal: INIT → CERT_REQUEST → CERT_ACTIVE → SET_CREATED → REQUEST_SENT → " \
               "VERIFIED → PAYMENT_REQUEST → AUTH_PHASE1 → AUTH_PHASE2 → SYSTEM_PROCESS → COMPLETED"
    ax.text(50, 90, info_text, ha='center', va='center', fontsize=9)
    
    plt.tight_layout()
    plt.savefig('diagrams/set_state_machine.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("✓ Diagramme d'état généré: set_state_machine.png")

if __name__ == '__main__':
    create_state_machine_diagram()