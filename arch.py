# diagram_architecture.py

from graphviz import Digraph
import os

def create_system_architecture_diagram():
    """Crée un diagramme d'architecture du système SET"""
    
    # Créer le graphe
    dot = Digraph(comment='Architecture SET Banking', format='png')
    dot.attr(rankdir='LR', size='12,8')
    dot.attr('node', shape='box', style='filled', fillcolor='lightblue')
    
    # Définir les clusters (groupes)
    with dot.subgraph(name='cluster_frontend') as c:
        c.attr(label='Frontend Web', style='filled', fillcolor='lightgrey', color='black')
        c.node('UI_Client', 'Interface Client\n(React/HTML/JS)')
        c.node('UI_Banque', 'Interface Banque\n(Dashboard)')
        c.node('UI_CA', 'Interface Certification\n(Admin)')
        c.attr(color='invis')
    
    with dot.subgraph(name='cluster_backend') as c:
        c.attr(label='Backend Flask', style='filled', fillcolor='lightyellow', color='black')
        c.node('Flask_App', 'Application Flask\n(Gestion API)')
        c.node('API_SET', 'API SET Protocol\n(Endpoints REST)')
        c.node('Auth_Service', 'Service d\'Authentification')
        c.attr(color='invis')
    
    with dot.subgraph(name='cluster_modules') as c:
        c.attr(label='Modules SET', style='filled', fillcolor='lightgreen', color='black')
        c.node('Crypto_Module', 'Module Cryptographique\n(RSA, Signatures)')
        c.node('SET_Protocol', 'Module SET Protocol\n(Logique Métier)')
        c.node('Models', 'Modèles de Données\n(Client, Banque, CA)')
        c.attr(color='invis')
    
    with dot.subgraph(name='cluster_database') as c:
        c.attr(label='Stockage', style='filled', fillcolor='pink', color='black')
        c.node('Session_Store', 'Session Store\n(Flask Session)')
        c.node('Key_Store', 'Key Store\n(Clés RSA)')
        c.node('Cert_Store', 'Certificat Store\n(Base de Certificats)')
        c.attr(color='invis')
    
    # Définir les connexions
    dot.edge('UI_Client', 'API_SET', label='HTTP/HTTPS\n(JSON)')
    dot.edge('UI_Banque', 'API_SET', label='WebSocket/HTTP')
    dot.edge('UI_CA', 'API_SET', label='REST API')
    
    dot.edge('API_SET', 'Flask_App', label='Routing')
    dot.edge('Flask_App', 'Crypto_Module', label='Appel Cryptographique')
    dot.edge('Flask_App', 'SET_Protocol', label='Logique SET')
    dot.edge('Flask_App', 'Models', label='ORM/Manipulation')
    
    dot.edge('Crypto_Module', 'Key_Store', label='Stockage Clés')
    dot.edge('SET_Protocol', 'Cert_Store', label='Gestion Certificats')
    dot.edge('Flask_App', 'Session_Store', label='Session Management')
    dot.edge('Models', 'Session_Store', label='Persistance')
    
    # Ajouter les services externes
    dot.node('Web_Browser', 'Navigateur Web\n(HTTPS/TLS)', shape='ellipse', fillcolor='orange')
    dot.node('Bank_API', 'API Bancaire Réelle\n(Système Externe)', shape='ellipse', fillcolor='red', style='filled')
    
    dot.edge('Web_Browser', 'UI_Client', label='Interface Utilisateur')
    dot.edge('API_SET', 'Bank_API', label='Intégration\n(Paiements Réels)', style='dashed')
    
    # Titre et métadonnées
    dot.attr(label='\n\nArchitecture Application SET Banking\n(Protocole SET Complet)')
    dot.attr(fontsize='20')
    
    # Sauvegarder et afficher
    dot.render('diagrams/set_architecture', view=True, cleanup=True)
    print("✓ Diagramme d'architecture généré: set_architecture.png")
    
    return dot

if __name__ == '__main__':
    # Créer le dossier pour les diagrammes
    os.makedirs('diagrams', exist_ok=True)
    
    # Générer le diagramme
    create_system_architecture_diagram()