# diagram_data_flow.py

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, ArrowStyle

def create_data_flow_diagram():
    """Crée un diagramme de flux de données (DFD)"""
    
    fig, ax = plt.subplots(figsize=(14, 12))
    
    # Créer un graphe orienté
    G = nx.DiGraph()
    
    # Ajouter les nœuds avec leurs types
    nodes = {
        'Client': {'type': 'entity', 'pos': (0.1, 0.5), 'color': 'lightblue'},
        'CA': {'type': 'entity', 'pos': (0.5, 0.9), 'color': 'lightgreen'},
        'Banque': {'type': 'entity', 'pos': (0.9, 0.5), 'color': 'lightcoral'},
        'Système': {'type': 'entity', 'pos': (0.5, 0.1), 'color': 'lightgray'},
        
        'Demande_Cert': {'type': 'process', 'pos': (0.3, 0.7), 'color': 'yellow'},
        'Emettre_Cert': {'type': 'process', 'pos': (0.7, 0.7), 'color': 'yellow'},
        'Creer_OT': {'type': 'process', 'pos': (0.3, 0.5), 'color': 'yellow'},
        'Chiffrer_PC': {'type': 'process', 'pos': (0.3, 0.3), 'color': 'yellow'},
        'Verifier_SET': {'type': 'process', 'pos': (0.7, 0.5), 'color': 'yellow'},
        'Traiter_Paiement': {'type': 'process', 'pos': (0.7, 0.3), 'color': 'yellow'},
        
        'Certificat': {'type': 'data', 'pos': (0.5, 0.75), 'color': 'orange'},
        'OT_Data': {'type': 'data', 'pos': (0.2, 0.5), 'color': 'orange'},
        'PC_Chiffre': {'type': 'data', 'pos': (0.2, 0.3), 'color': 'orange'},
        'SET_Operator': {'type': 'data', 'pos': (0.5, 0.5), 'color': 'orange'},
        'Result_Paiement': {'type': 'data', 'pos': (0.5, 0.25), 'color': 'orange'},
    }
    
    # Ajouter les nœuds au graphe
    for node, attrs in nodes.items():
        G.add_node(node, **attrs)
    
    # Ajouter les arêtes avec leurs labels
    edges = [
        # Flux de certification
        ('Client', 'Demande_Cert', 'Demande_Certificat\n(Clé Publique)'),
        ('Demande_Cert', 'CA', 'Validation Demande'),
        ('CA', 'Emettre_Cert', 'Génération Certificat'),
        ('Emettre_Cert', 'Certificat', 'Stockage Certificat'),
        ('Certificat', 'Client', 'Envoi Certificat'),
        
        # Création OT
        ('Client', 'Creer_OT', 'Données Transaction\n(Montant, Marchand)'),
        ('Creer_OT', 'OT_Data', 'Order Transcript\n(OT)'),
        
        # Chiffrement PC
        ('Client', 'Chiffrer_PC', 'Numéro Carte\n(PAN)'),
        ('Chiffrer_PC', 'PC_Chiffre', 'PC Chiffré\n(RSA 2048)'),
        
        # Formation SET Operator
        ('OT_Data', 'SET_Operator', ''),
        ('PC_Chiffre', 'SET_Operator', ''),
        ('Certificat', 'SET_Operator', 'Certificat Client'),
        
        # Envoi à la banque
        ('SET_Operator', 'Verifier_SET', 'Requête SET'),
        
        # Vérifications banque
        ('Banque', 'Verifier_SET', 'Règles Validation'),
        ('Verifier_SET', 'SET_Operator', 'Vérification\nStructure & Signature'),
        
        # Traitement paiement
        ('SET_Operator', 'Traiter_Paiement', 'Demande Paiement'),
        ('Traiter_Paiement', 'Result_Paiement', 'Résultat\n(Autorisé/Refusé)'),
        
        # Système de surveillance
        ('Traiter_Paiement', 'Système', 'Notification\nTransaction'),
        ('Système', 'Traiter_Paiement', 'Résultat Enquête\nCrise'),
        
        # Retour au client
        ('Result_Paiement', 'Client', 'Confirmation\nTransaction'),
    ]
    
    for src, dst, label in edges:
        G.add_edge(src, dst, label=label)
    
    # Positionner les nœuds
    pos = {node: attrs['pos'] for node, attrs in nodes.items()}
    
    # Dessiner les nœuds selon leur type
    for node, attrs in nodes.items():
        x, y = pos[node]
        color = attrs['color']
        
        if attrs['type'] == 'entity':
            # Rectangle pour les entités externes
            rect = Rectangle((x-0.07, y-0.04), 0.14, 0.08,
                           facecolor=color, edgecolor='black',
                           linewidth=2, alpha=0.8)
            ax.add_patch(rect)
            ax.text(x, y, node, ha='center', va='center', 
                   fontsize=10, fontweight='bold')
            
        elif attrs['type'] == 'process':
            # Cercle pour les processus
            circle = Circle((x, y), 0.05,
                          facecolor=color, edgecolor='black',
                          linewidth=2, alpha=0.8)
            ax.add_patch(circle)
            ax.text(x, y, node.replace('_', '\n'), 
                   ha='center', va='center', fontsize=8)
            
        elif attrs['type'] == 'data':
            # Ovale pour les données
            from matplotlib.patches import Ellipse
            ellipse = Ellipse((x, y), 0.12, 0.06,
                            facecolor=color, edgecolor='black',
                            linewidth=2, alpha=0.8)
            ax.add_patch(ellipse)
            ax.text(x, y, node.replace('_', '\n'), 
                   ha='center', va='center', fontsize=8)
    
    # Dessiner les arêtes
    for edge in G.edges():
        src, dst = edge
        x1, y1 = pos[src]
        x2, y2 = pos[dst]
        
        # Calculer le point de départ et d'arrivée ajusté
        # Pour éviter de superposer aux nœuds
        dx, dy = x2 - x1, y2 - y1
        dist = (dx**2 + dy**2)**0.5
        
        if dist > 0:
            # Ajuster pour les cercles (processus)
            if nodes[src]['type'] == 'process':
                adjust = 0.05 / dist
                x1 += dx * adjust
                y1 += dy * adjust
            
            if nodes[dst]['type'] == 'process':
                adjust = 0.05 / dist
                x2 -= dx * adjust
                y2 -= dy * adjust
            elif nodes[dst]['type'] in ['entity', 'data']:
                # Ajustement pour rectangles/ellipses
                if abs(dx) > abs(dy):  # Horizontal
                    adjust = 0.07 / abs(dx) if dx != 0 else 0
                else:  # Vertical
                    adjust = 0.04 / abs(dy) if dy != 0 else 0
                
                if dx > 0:  # Vers la droite
                    x2 -= adjust
                elif dx < 0:  # Vers la gauche
                    x2 += adjust
                
                if dy > 0:  # Vers le haut
                    y2 -= adjust
                elif dy < 0:  # Vers le bas
                    y2 += adjust
        
        # Dessiner la flèche
        arrow = ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                          arrowprops=dict(arrowstyle='->', 
                                        color='black', 
                                        linewidth=1.5,
                                        alpha=0.7,
                                        connectionstyle="arc3,rad=0.1"))
        
        # Ajouter le label
        label_text = G.edges[edge]['label']
        if label_text:
            mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
            offset_x, offset_y = dy * 0.02, -dx * 0.02
            ax.text(mid_x + offset_x, mid_y + offset_y, label_text,
                   fontsize=7, ha='center', va='center',
                   bbox=dict(boxstyle="round,pad=0.3", 
                           facecolor="white", 
                           edgecolor="gray", 
                           alpha=0.8))
    
    # Légende
    legend_elements = [
        Rectangle((0, 0), 1, 1, facecolor='lightblue', edgecolor='black', label='Entité Externe'),
        Circle((0, 0), 0.5, facecolor='yellow', edgecolor='black', label='Processus'),
        plt.Rectangle((0, 0), 1, 0.5, facecolor='orange', edgecolor='black', label='Stockage Données')
    ]
    
    ax.legend(handles=legend_elements, loc='upper center', 
              bbox_to_anchor=(0.5, -0.05), ncol=3, fontsize=10)
    
    # Titre
    ax.set_title('Diagramme de Flux de Données (DFD) - Application SET Banking', 
                 fontsize=14, fontweight='bold', pad=20)
    
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-0.1, 1.1)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('diagrams/set_data_flow.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("✓ Diagramme de flux de données généré: set_data_flow.png")

if __name__ == '__main__':
    create_data_flow_diagram()