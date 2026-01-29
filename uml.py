# diagram_class_uml.py

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
import matplotlib.patches as mpatches

def create_class_diagram():
    """Crée un diagramme de classe UML de l'application"""
    
    fig, ax = plt.subplots(figsize=(16, 12))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    # Titre
    ax.text(50, 98, 'Diagramme de Classe UML - Application SET Banking', 
            fontsize=16, fontweight='bold', ha='center')
    ax.text(50, 94, 'Structure des principales classes et leurs relations', 
            fontsize=12, ha='center', style='italic')
    
    # Classe CryptoManager
    crypto_x, crypto_y = 10, 80
    crypto_width, crypto_height = 25, 15
    
    # Header de la classe
    crypto_header = Rectangle((crypto_x, crypto_y + crypto_height - 5), 
                             crypto_width, 5, 
                             facecolor='lightblue', edgecolor='black')
    ax.add_patch(crypto_header)
    ax.text(crypto_x + crypto_width/2, crypto_y + crypto_height - 2.5, 
            'CryptoManager', fontweight='bold', ha='center', va='center')
    
    # Corps de la classe
    crypto_body = Rectangle((crypto_x, crypto_y), 
                           crypto_width, crypto_height - 5, 
                           facecolor='white', edgecolor='black')
    ax.add_patch(crypto_body)
    
    # Attributs
    crypto_attrs = [
        '- key_size: int = 2048',
        '- private_key: bytes',
        '- public_key: bytes'
    ]
    for i, attr in enumerate(crypto_attrs):
        ax.text(crypto_x + 2, crypto_y + crypto_height - 10 - i*3, 
                attr, fontsize=9, va='top')
    
    # Méthodes
    crypto_methods = [
        '+ generate_rsa_keys(): dict',
        '+ rsa_encrypt(data, key): bytes',
        '+ rsa_decrypt(data, key): bytes',
        '+ sign_data(data, key): str',
        '+ verify_signature(data, sig, key): bool',
        '+ hash_data(data): str'
    ]
    for i, method in enumerate(crypto_methods):
        ax.text(crypto_x + 2, crypto_y + crypto_height - 25 - i*3, 
                method, fontsize=9, va='top')
    
    # Classe SETProtocol
    set_x, set_y = 40, 80
    set_width, set_height = 25, 12
    
    set_header = Rectangle((set_x, set_y + set_height - 5), 
                          set_width, 5, 
                          facecolor='lightgreen', edgecolor='black')
    ax.add_patch(set_header)
    ax.text(set_x + set_width/2, set_y + set_height - 2.5, 
            'SETProtocol', fontweight='bold', ha='center', va='center')
    
    set_body = Rectangle((set_x, set_y), 
                        set_width, set_height - 5, 
                        facecolor='white', edgecolor='black')
    ax.add_patch(set_body)
    
    set_attrs = ['- transactions: dict']
    ax.text(set_x + 2, set_y + set_height - 10, set_attrs[0], fontsize=9, va='top')
    
    set_methods = [
        '+ verify_structure(set_op): bool',
        '+ process_request(set_op): dict',
        '+ process_payment(set_op, montant): dict',
        '+ authorize_payment(data): dict',
        '+ capture_payment(auth): dict'
    ]
    for i, method in enumerate(set_methods):
        ax.text(set_x + 2, set_y + set_height - 15 - i*3, 
                method, fontsize=9, va='top')
    
    # Classe Client
    client_x, client_y = 70, 80
    client_width, client_height = 25, 10
    
    client_header = Rectangle((client_x, client_y + client_height - 5), 
                             client_width, 5, 
                             facecolor='lightcoral', edgecolor='black')
    ax.add_patch(client_header)
    ax.text(client_x + client_width/2, client_y + client_height - 2.5, 
            'Client', fontweight='bold', ha='center', va='center')
    
    client_body = Rectangle((client_x, client_y), 
                           client_width, client_height - 5, 
                           facecolor='white', edgecolor='black')
    ax.add_patch(client_body)
    
    client_attrs = [
        '- client_id: str',
        '- nom: str',
        '- certificats: list',
        '- transactions: list'
    ]
    for i, attr in enumerate(client_attrs):
        ax.text(client_x + 2, client_y + client_height - 10 - i*3, 
                attr, fontsize=9, va='top')
    
    # Classe Banque
    banque_x, banque_y = 10, 50
    banque_width, banque_height = 25, 10
    
    banque_header = Rectangle((banque_x, banque_y + banque_height - 5), 
                             banque_width, 5, 
                             facecolor='gold', edgecolor='black')
    ax.add_patch(banque_header)
    ax.text(banque_x + banque_width/2, banque_y + banque_height - 2.5, 
            'Banque', fontweight='bold', ha='center', va='center')
    
    banque_body = Rectangle((banque_x, banque_y), 
                           banque_width, banque_height - 5, 
                           facecolor='white', edgecolor='black')
    ax.add_patch(banque_body)
    
    banque_attrs = [
        '- nom: str',
        '- code: str',
        '- clients: dict',
        '- transactions: dict'
    ]
    for i, attr in enumerate(banque_attrs):
        ax.text(banque_x + 2, banque_y + banque_height - 10 - i*3, 
                attr, fontsize=9, va='top')
    
    banque_methods = [
        '+ verifier_certificat(cert): bool',
        '+ traiter_paiement(set_op): dict'
    ]
    for i, method in enumerate(banque_methods):
        ax.text(banque_x + 2, banque_y + banque_height - 22 - i*3, 
                method, fontsize=9, va='top')
    
    # Classe CertificationAuthority
    ca_x, ca_y = 40, 50
    ca_width, ca_height = 30, 12
    
    ca_header = Rectangle((ca_x, ca_y + ca_height - 5), 
                         ca_width, 5, 
                         facecolor='violet', edgecolor='black')
    ax.add_patch(ca_header)
    ax.text(ca_x + ca_width/2, ca_y + ca_height - 2.5, 
            'CertificationAuthority', fontweight='bold', ha='center', va='center')
    
    ca_body = Rectangle((ca_x, ca_y), 
                       ca_width, ca_height - 5, 
                       facecolor='white', edgecolor='black')
    ax.add_patch(ca_body)
    
    ca_attrs = [
        '- certificats_emis: dict',
        '- ca_private_key: str',
        '- ca_public_key: str'
    ]
    for i, attr in enumerate(ca_attrs):
        ax.text(ca_x + 2, ca_y + ca_height - 10 - i*3, 
                attr, fontsize=9, va='top')
    
    ca_methods = [
        '+ emit_certificate(client_id, pub_key): dict',
        '+ verify_certificate(cert): bool',
        '+ revoke_certificate(cert_id): bool'
    ]
    for i, method in enumerate(ca_methods):
        ax.text(ca_x + 2, ca_y + ca_height - 25 - i*3, 
                method, fontsize=9, va='top')
    
    # Classe FlaskApp (Singleton)
    app_x, app_y = 75, 50
    app_width, app_height = 20, 15
    
    app_header = Rectangle((app_x, app_y + app_height - 5), 
                          app_width, 5, 
                          facecolor='cyan', edgecolor='black')
    ax.add_patch(app_header)
    ax.text(app_x + app_width/2, app_y + app_height - 2.5, 
            'FlaskApp', fontweight='bold', ha='center', va='center')
    
    app_body = Rectangle((app_x, app_y), 
                        app_width, app_height - 5, 
                        facecolor='white', edgecolor='black')
    ax.add_patch(app_body)
    
    app_attrs = [
        '- app: Flask',
        '- crypto: CryptoManager',
        '- protocol: SETProtocol',
        '- ca: CertificationAuthority'
    ]
    for i, attr in enumerate(app_attrs):
        ax.text(app_x + 2, app_y + app_height - 10 - i*3, 
                attr, fontsize=9, va='top')
    
    app_methods = [
        '+ setup_routes()',
        '+ api_demande_certificat()',
        '+ api_emission_certificat()',
        '+ api_creation_operator()',
        '+ api_verification()'
    ]
    for i, method in enumerate(app_methods):
        ax.text(app_x + 2, app_y + app_height - 30 - i*3, 
                method, fontsize=9, va='top')
    
    # Relations entre classes
    
    # Héritage/Utilisation
    relations = [
        # FlaskApp utilise CryptoManager
        (app_x, app_y + app_height/2, crypto_x + crypto_width, crypto_y + crypto_height/2, 
         'utilise', 'dashed'),
        
        # FlaskApp utilise SETProtocol
        (app_x, app_y + app_height/3, set_x + set_width, set_y + set_height/2, 
         'utilise', 'dashed'),
        
        # FlaskApp utilise CertificationAuthority
        (app_x, app_y + app_height*2/3, ca_x + ca_width, ca_y + ca_height/2, 
         'utilise', 'dashed'),
        
        # Client interagit avec CertificationAuthority
        (client_x, client_y, ca_x + ca_width/2, ca_y + ca_height, 
         'demande certificat', 'solid'),
        
        # Client interagit avec Banque
        (client_x, client_y - 5, banque_x + banque_width/2, banque_y + banque_height, 
         'envoie requête', 'solid'),
        
        # Banque utilise SETProtocol
        (banque_x + banque_width, banque_y + banque_height/2, set_x, set_y + set_height/2, 
         'vérifie via', 'dashed'),
        
        # CertificationAuthority fournit à Client
        (ca_x + ca_width/2, ca_y, client_x + client_width/2, client_y + client_height, 
         'fournit certificat', 'solid')
    ]
    
    for x1, y1, x2, y2, label, style in relations:
        # Dessiner la flèche
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                   arrowprops=dict(arrowstyle='->', 
                                 color='black', 
                                 linewidth=1.5,
                                 linestyle=style,
                                 alpha=0.7))
        
        # Ajouter le label
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        ax.text(mid_x, mid_y, label, fontsize=8, 
               ha='center', va='center',
               bbox=dict(boxstyle="round,pad=0.2", 
                        facecolor="white", 
                        edgecolor="gray", 
                        alpha=0.8))
    
    # Légende UML
    legend_y = 20
    legend_elements = [
        Rectangle((0, 0), 1, 0.6, facecolor='lightblue', edgecolor='black', label='Classe Utilitaire'),
        Rectangle((0, 0), 1, 0.6, facecolor='lightgreen', edgecolor='black', label='Classe Protocole'),
        Rectangle((0, 0), 1, 0.6, facecolor='lightcoral', edgecolor='black', label='Classe Métier'),
        Rectangle((0, 0), 1, 0.6, facecolor='gold', edgecolor='black', label='Classe Institution'),
        Rectangle((0, 0), 1, 0.6, facecolor='violet', edgecolor='black', label='Classe Autorité'),
        Rectangle((0, 0), 1, 0.6, facecolor='cyan', edgecolor='black', label='Classe Application'),
    ]
    
    ax.legend(handles=legend_elements, loc='lower center', 
              bbox_to_anchor=(0.5, 0.05), ncol=3, fontsize=9)
    
    plt.tight_layout()
    plt.savefig('diagrams/set_class_diagram.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("✓ Diagramme de classe UML généré: set_class_diagram.png")

if __name__ == '__main__':
    create_class_diagram()