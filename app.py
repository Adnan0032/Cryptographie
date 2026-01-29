# app.py - Application SET complète et simplifiée
from flask import Flask, render_template, request, jsonify, session
import json
import uuid
from datetime import datetime
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
import hashlib

app = Flask(__name__)
app.secret_key = 'set-protocol-simple-key-2024'

# ==================== FONCTIONS CRYPTO ====================
def generate_keys():
    """Génère une paire de clés RSA 2048 bits"""
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key.decode(), public_key.decode()

def encrypt_pan(pan, public_key):
    """Chiffre le PAN avec RSA PKCS1 OAEP"""
    key = RSA.import_key(public_key.encode())
    cipher = PKCS1_OAEP.new(key)
    encrypted = cipher.encrypt(pan.encode())
    return base64.b64encode(encrypted).decode()

def decrypt_pan(encrypted_pan, private_key):
    """Déchiffre le PAN avec RSA PKCS1 OAEP"""
    key = RSA.import_key(private_key.encode())
    cipher = PKCS1_OAEP.new(key)
    decrypted = cipher.decrypt(base64.b64decode(encrypted_pan))
    return decrypted.decode()

def sign_data(data, private_key):
    """Signe des données avec clé privée RSA"""
    key = RSA.import_key(private_key.encode())
    
    # Convertir le dictionnaire en string JSON triée pour une signature cohérente
    if isinstance(data, dict):
        data_str = json.dumps(data, sort_keys=True)
    else:
        data_str = str(data)
    
    h = SHA256.new(data_str.encode())
    signature = pkcs1_15.new(key).sign(h)
    return base64.b64encode(signature).decode()

def verify_signature(data, signature, public_key):
    """Vérifie une signature RSA"""
    try:
        key = RSA.import_key(public_key.encode())
        
        # Convertir le dictionnaire en string JSON triée
        if isinstance(data, dict):
            data_str = json.dumps(data, sort_keys=True)
        else:
            data_str = str(data)
        
        h = SHA256.new(data_str.encode())
        pkcs1_15.new(key).verify(h, base64.b64decode(signature))
        return True
    except Exception as e:
        print(f"Erreur vérification signature: {e}")
        return False

def hash_data(data):
    """Calcule le hash SHA256 des données"""
    if isinstance(data, dict):
        data_str = json.dumps(data, sort_keys=True)
    else:
        data_str = str(data)
    
    return hashlib.sha256(data_str.encode()).hexdigest()

# ==================== ROUTES PRINCIPALES ====================
@app.route('/')
def index():
    """Page principale avec toutes les étapes"""
    # Initialiser session si nécessaire
    if 'client_id' not in session:
        session['client_id'] = str(uuid.uuid4())[:8]
        session['transaction_id'] = f"TXN-{uuid.uuid4().hex[:8].upper()}"
        session['timestamp'] = datetime.now().isoformat()
    
    return render_template('index.html')

@app.route('/reset')
def reset():
    """Réinitialiser toute la session"""
    session.clear()
    return '<script>alert("Session réinitialisée!"); window.location="/";</script>'

# ==================== ÉTAPE 1 ====================
@app.route('/etape1')
def etape1():
    """Étape 1: Demande de certificat"""
    # Générer les clés RSA pour le client
    private_key, public_key = generate_keys()
    
    # Sauvegarder dans la session
    session['client_private_key'] = private_key
    session['client_public_key'] = public_key
    
    # Créer la demande de certificat
    demande_certificat = {
        'client_id': session.get('client_id', str(uuid.uuid4())[:8]),
        'public_key': public_key,
        'timestamp': datetime.now().isoformat(),
        'type': 'SET_CLIENT_CERTIFICATE',
        'version': 'SET-1.0'
    }
    
    # Signer la demande
    demande_certificat['signature'] = sign_data(demande_certificat, private_key)
    
    session['demande_certificat'] = demande_certificat
    
    return render_template('etape1.html', 
                          demande=demande_certificat,
                          client_id=demande_certificat['client_id'])

# ==================== ÉTAPE 2 ====================
@app.route('/etape2')
def etape2():
    """Étape 2: Certificat émis par CA"""
    demande = session.get('demande_certificat', {})
    
    # CA émet le certificat (simulation)
    certificat = {
        'cert_id': f"CERT-{uuid.uuid4().hex[:8].upper()}",
        'client_id': demande.get('client_id', 'UNKNOWN'),
        'public_key': demande.get('public_key', ''),
        'emission': datetime.now().isoformat(),
        'expiration': '2024-12-31T23:59:59',
        'ca_name': 'SET_ROOT_CA_V1',
        'algorithm': 'RSA-2048-SHA256',
        'purpose': 'SET_TRANSACTION_SIGNING'
    }
    
    # CA signe le certificat (simulation avec hash)
    ca_signature = hash_data({
        'cert_id': certificat['cert_id'],
        'public_key': certificat['public_key'][:100] + '...',
        'timestamp': certificat['emission']
    })
    
    certificat['ca_signature'] = f"CA-SIG-{ca_signature[:32].upper()}"
    
    session['certificat'] = certificat
    
    return render_template('etape2.html', 
                          certificat=certificat,
                          ca_signature=certificat['ca_signature'])

# ==================== ÉTAPE 3 ====================
@app.route('/etape3')
def etape3():
    """Étape 3: Création opérateur SET"""
    certificat = session.get('certificat', {})
    return render_template('etape3.html', 
                          certificat=certificat)

@app.route('/api/creer_operateur', methods=['POST'])
def creer_operateur():
    """API pour créer l'opérateur SET (OT + PC chiffré + signature)"""
    try:
        data = request.json
        
        # Récupérer les données de la session
        certificat = session.get('certificat', {})
        private_key = session.get('client_private_key', '')
        
        if not private_key:
            return jsonify({
                'success': False,
                'error': 'Clé privée non trouvée'
            }), 400
        
        # 1. Créer l'OT (Order Transcript)
        ot = {
            'transaction_id': session.get('transaction_id', f"TXN-{uuid.uuid4().hex[:8].upper()}"),
            'montant': float(data['montant']),
            'marchand': data['marchand'],
            'devise': 'EUR',
            'date': datetime.now().isoformat(),
            'type_transaction': 'ACHAT_EN_LIGNE',
            'client_id': session.get('client_id', 'UNKNOWN')
        }
        
        # 2. Chiffrer le PAN (Primary Account Number)
        pan_chiffre = encrypt_pan(data['pan'], certificat.get('public_key', ''))
        
        # 3. Signer l'OT avec la clé privée du client
        signature_ot = sign_data(ot, private_key)
        
        # 4. Créer l'opérateur SET complet
        set_operator = {
            'ot': ot,
            'pc_chiffre': pan_chiffre,
            'signature': signature_ot,
            'certificat': certificat,
            'hash_ot': hash_data(ot),
            'timestamp': datetime.now().isoformat()
        }
        
        # Sauvegarder dans la session
        session['set_operator'] = set_operator
        session['ot'] = ot
        session['pan_chiffre'] = pan_chiffre
        session['signature'] = signature_ot
        
        # Simuler le déchiffrement (pour démonstration)
        try:
            pan_dechiffre = decrypt_pan(pan_chiffre, private_key)
            session['pan_dechiffre'] = pan_dechiffre
        except:
            session['pan_dechiffre'] = "Erreur déchiffrement"
        
        return jsonify({
            'success': True,
            'set_operator': {
                'ot': ot,
                'pc_chiffre_preview': pan_chiffre[:50] + '...' + pan_chiffre[-20:],
                'signature_preview': signature_ot[:50] + '...' + signature_ot[-20:],
                'hash_ot': set_operator['hash_ot'],
                'certificat_id': certificat.get('cert_id', 'UNKNOWN')
            },
            'message': 'Opérateur SET créé avec succès'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# ==================== ÉTAPE 4 ====================
@app.route('/etape4')
def etape4():
    """Étape 4: Envoi à la banque"""
    set_operator = session.get('set_operator', {})
    return render_template('etape4.html', 
                          set_operator=set_operator)

@app.route('/api/envoyer_banque', methods=['POST'])
def envoyer_banque():
    """API pour envoyer l'opérateur SET à la banque"""
    set_operator = session.get('set_operator', {})
    
    if not set_operator:
        return jsonify({
            'success': False,
            'error': 'Opérateur SET non trouvé'
        }), 400
    
    # Simuler l'envoi et la vérification par la banque
    ot = set_operator.get('ot', {})
    signature = set_operator.get('signature', '')
    certificat = set_operator.get('certificat', {})
    public_key = certificat.get('public_key', '')
    
    # Vérifications effectuées par la banque
    verifications = {
        'structure': True,  # Structure SET valide
        'certificat': True,  # Certificat valide et non expiré
        'signature': verify_signature(ot, signature, public_key),  # Signature valide
        'hash_integrity': hash_data(ot) == set_operator.get('hash_ot', ''),  # Intégrité OT
        'timestamp_valide': True,  # Transaction récente
        'format_pc': True  # Format PC chiffré valide
    }
    
    # Toutes les vérifications doivent passer
    toutes_ok = all(verifications.values())
    
    session['verifications'] = verifications
    session['toutes_verifications_ok'] = toutes_ok
    
    return jsonify({
        'success': True,
        'verifications': verifications,
        'toutes_ok': toutes_ok,
        'message': 'Requête SET envoyée et vérifiée par la banque'
    })

# ==================== ÉTAPE 5 ====================
@app.route('/etape5')
def etape5():
    """Étape 5 & 6: Vérifications par la banque"""
    verifications = session.get('verifications', {})
    toutes_ok = session.get('toutes_verifications_ok', False)
    
    return render_template('etape5.html', 
                          verifications=verifications,
                          toutes_ok=toutes_ok)

# ==================== ÉTAPE 7 ====================
@app.route('/etape7')
def etape7():
    """Étape 7: Demande d'achat avec PC chiffré"""
    return render_template('etape7.html')

@app.route('/api/demander_achat', methods=['POST'])
def demander_achat():
    """API pour demande d'achat"""
    # Récupérer les données nécessaires
    set_operator = session.get('set_operator', {})
    ot = set_operator.get('ot', {})
    pan_chiffre = set_operator.get('pc_chiffre', '')
    
    if not ot or not pan_chiffre:
        return jsonify({
            'success': False,
            'error': 'Données transaction manquantes'
        }), 400
    
    # Simuler l'achat en 2 phases
    
    # Phase 1: Autorisation
    autorisation = {
        'autorise': True,
        'code_autorisation': f"AUTH-{uuid.uuid4().hex[:6].upper()}",
        'date_autorisation': datetime.now().isoformat(),
        'montant': ot.get('montant', 0),
        'marchand': ot.get('marchand', ''),
        'transaction_id': ot.get('transaction_id', '')
    }
    
    # Phase 2: Capture (si autorisation réussie)
    if autorisation['autorise']:
        capture = {
            'capture': True,
            'code_capture': f"CAPT-{uuid.uuid4().hex[:6].upper()}",
            'date_capture': datetime.now().isoformat(),
            'montant_capture': ot.get('montant', 0),
            'status': 'COMPLETED'
        }
    else:
        capture = {
            'capture': False,
            'status': 'FAILED',
            'raison': 'Autorisation refusée'
        }
    
    # Sauvegarder dans la session
    session['autorisation'] = autorisation
    session['capture'] = capture
    
    # Simuler le déchiffrement du PAN par la banque (pour log)
    try:
        # En réalité, la banque utiliserait sa propre clé privée
        # Pour la démo, on utilise la clé du client
        private_key = session.get('client_private_key', '')
        if private_key:
            pan_dechiffre = decrypt_pan(pan_chiffre, private_key)
            session['pan_banque'] = f"PAN déchiffré: {pan_dechiffre[:6]}******{pan_dechiffre[-4:]}"
    except:
        session['pan_banque'] = "Déchiffrement simulé"
    
    return jsonify({
        'success': True,
        'autorisation': autorisation,
        'capture': capture,
        'message': 'Achat traité en 2 phases'
    })

# ==================== ÉTAPE 8 ====================
@app.route('/etape8')
def etape8():
    """Étape 8: Achats en 2 phases"""
    autorisation = session.get('autorisation', {})
    capture = session.get('capture', {})
    pan_banque = session.get('pan_banque', 'PAN non disponible')
    
    return render_template('etape8.html', 
                          autorisation=autorisation,
                          capture=capture,
                          pan_banque=pan_banque)

# ==================== ÉTAPE 9 ====================
@app.route('/etape9')
def etape9():
    """Étape 9: Aide solidaire + MEC"""
    # Données pour la simulation MEC
    transaction_data = {
        'id': session.get('transaction_id', 'TXN-XXXXXX'),
        'montant': session.get('ot', {}).get('montant', 0),
        'marchand': session.get('ot', {}).get('marchand', ''),
        'timestamp': session.get('timestamp', datetime.now().isoformat()),
        'status': 'PROCESSING'
    }
    
    session['mec_data'] = transaction_data
    
    return render_template('etape9.html', 
                          transaction_data=transaction_data)

# ==================== ÉTAPE 10 ====================
@app.route('/etape10')
def etape10():
    """Étape 10: Enquête de crise"""
    # Données pour l'enquête
    investigation_data = {
        'transaction_id': session.get('transaction_id', 'TXN-XXXXXX'),
        'client_id': session.get('client_id', 'UNKNOWN'),
        'montant': session.get('ot', {}).get('montant', 0),
        'timestamp': session.get('timestamp', datetime.now().isoformat()),
        'risk_score': 15,  # Score de risque bas par défaut
        'anomalies': 0
    }
    
    # Calculer un score de risque aléatoire pour la démonstration
    import random
    investigation_data['risk_score'] = random.randint(10, 40)
    investigation_data['anomalies'] = random.randint(0, 2)
    
    session['investigation_data'] = investigation_data
    
    return render_template('etape10.html', 
                          investigation_data=investigation_data)

# ==================== ÉTAPE 11 ====================
@app.route('/etape11')
def etape11():
    """Étape 11: Confirmation finale"""
    # Récupérer toutes les données de la transaction
    transaction_id = session.get('transaction_id', '')
    ot = session.get('ot', {})
    autorisation = session.get('autorisation', {})
    capture = session.get('capture', {})
    certificat = session.get('certificat', {})
    
    # Préparer la confirmation finale
    confirmation_data = {
        'transaction_id': transaction_id,
        'montant': ot.get('montant', 0),
        'marchand': ot.get('marchand', ''),
        'date_transaction': ot.get('date', ''),
        'autorisation_code': autorisation.get('code_autorisation', ''),
        'capture_code': capture.get('code_capture', ''),
        'certificat_id': certificat.get('cert_id', ''),
        'status_final': 'COMPLETED',
        'date_confirmation': datetime.now().isoformat(),
        'message': 'Transaction SET complétée avec succès'
    }
    
    session['confirmation'] = confirmation_data
    
    return render_template('etape11.html', 
                          confirmation=confirmation_data,
                          transaction_id=transaction_id)

@app.route('/api/confirmer', methods=['POST'])
def confirmer():
    """API pour confirmation finale"""
    confirmation = session.get('confirmation', {})
    
    if not confirmation:
        confirmation = {
            'transaction_id': session.get('transaction_id', ''),
            'status': 'COMPLETED',
            'date': datetime.now().isoformat(),
            'message': 'Transaction SET confirmée'
        }
    
    # Générer une signature finale (simulée)
    confirmation['signature_finale'] = f"SIG-{hashlib.sha256(str(confirmation).encode()).hexdigest()[:16].upper()}"
    
    return jsonify({
        'success': True,
        'confirmation': confirmation,
        'message': 'Transaction SET confirmée avec succès'
    })

# ==================== API DE DIAGNOSTIC ====================
@app.route('/api/status')
def api_status():
    """API pour voir le statut de la session"""
    return jsonify({
        'session': dict(session),
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/generer_certificat', methods=['POST'])
def generer_certificat():
    """API pour générer un nouveau certificat"""
    # Générer nouvelles clés
    private_key, public_key = generate_keys()
    
    # Créer certificat
    certificat = {
        'cert_id': f"CERT-{uuid.uuid4().hex[:8].upper()}",
        'client_id': session.get('client_id', str(uuid.uuid4())[:8]),
        'public_key': public_key,
        'emission': datetime.now().isoformat(),
        'expiration': '2024-12-31',
        'ca_signature': f"CA-SIG-{hashlib.sha256(public_key.encode()).hexdigest()[:32].upper()}"
    }
    
    session['client_private_key'] = private_key
    session['client_public_key'] = public_key
    session['certificat'] = certificat
    
    return jsonify({
        'success': True,
        'certificat': certificat
    })

# ==================== GESTION D'ERREURS ====================
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# ==================== MIDDLEWARE ====================
@app.before_request
def before_request():
    """Initialise les variables de session si nécessaire"""
    if 'client_id' not in session:
        session['client_id'] = f"CLIENT-{uuid.uuid4().hex[:6].upper()}"
    if 'transaction_id' not in session:
        session['transaction_id'] = f"TXN-{uuid.uuid4().hex[:8].upper()}"
    if 'timestamp' not in session:
        session['timestamp'] = datetime.now().isoformat()

# ==================== LANCEMENT ====================
if __name__ == '__main__':
    print("=" * 60)
    print("PROTOCOLE SET - APPLICATION SIMPLIFIÉE")
    print("=" * 60)
    print("Serveur démarré sur : http://localhost:5000")
    print("Accédez à l'application pour tester le protocole SET")
    print("=" * 60)
    
    app.run(
        debug=True,
        port=5000,
        host='0.0.0.0'
    )