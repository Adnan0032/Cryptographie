# Documentation du Projet : Simulateur du Protocole SET (Secure Electronic Transaction)

Ce notebook détaille le fonctionnement, l'architecture et les étapes de l'implémentation pédagogique du protocole SET. Ce projet utilise **Flask** pour l'interface web et **PyCryptodome** pour la couche cryptographique réelle.

## Objectif
L'objectif est de démontrer comment les certificats numériques et le chiffrement asymétrique (RSA) sécurisent une transaction entre un client, un marchand et une banque sans jamais exposer le numéro de carte bancaire au marchand.

## 1. Prérequis et Installation

Pour faire fonctionner ce projet, vous devez disposer d'un environnement Python 3.8+ avec les dépendances suivantes :

* **Flask** : Serveur web.
* **PyCryptodome** : Bibliothèque pour les opérations RSA et SHA-256.

### Installation via terminal
pip install Flask==2.3.2 pycryptodome==3.18.0


## 2. Les 11 Étapes du Protocole SET

Le projet suit rigoureusement le flux standardisé du protocole :

1.  **Demande de certificat** : Le client génère une paire de clés RSA 2048.
2.  **Émission** : L'Autorité de Certification (CA) signe et renvoie le certificat.
3.  **Opérateur SET** : Initialisation du logiciel de paiement côté client.
4.  **Envoi Banque** : Le client envoie ses informations d'identité à la banque pour vérification.
5.  **Vérification** : La banque vérifie les signatures numériques reçues.
6.  **Certification OK** : La banque confirme la validité du certificat client.
7.  **Demande d'achat** : Le client chiffre son PAN (numéro de carte) avec la clé publique de la banque (Enveloppe numérique).
8.  **Achat 2 phases** : Autorisation (blocage des fonds) puis Capture (transfert réel).
9.  **Gestion MEC** : Traitement des messages d'erreurs sécurisés.
10. **Enquête de crise** : Simulation de la détection de fraude.
11. **Confirmation** : Reçu final de la transaction.

## 3. Aperçu de la logique cryptographique utilisée

Voici comment le projet gère le chiffrement RSA pour sécuriser les données sensibles :

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# 1. Génération des clés
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

print("Clé publique générée avec succès.")

# 2. Simulation de chiffrement d'un PAN (Numéro de carte)
donnees = b"4242-4242-4242-4242"
chiffreur = PKCS1_OAEP.new(RSA.import_key(public_key))
message_chiffre = chiffreur.encrypt(donnees)

print(f"Message chiffré (hex) : {message_chiffre.hex()[:50]}...")


## 4. Comment utiliser le projet

1. **Lancer le serveur** : Exécutez `python app.py` dans votre terminal.
2. **Accéder à l'interface** : Allez sur `http://localhost:5000`.
3. **Suivre le workflow** :
    * Cliquez sur "Démarrer la transaction".
    * À chaque étape, observez les logs dans le terminal : vous verrez les certificats s'échanger et les signatures se vérifier.
    * Utilisez les données de test pré-remplies dans le formulaire d'achat.
4. **Analyse** : À l'étape 7, notez que le marchand reçoit une preuve de paiement mais ne peut pas voir votre numéro de carte, car celui-ci est chiffré pour la banque uniquement.

## Ressources et References

Pour approfondir la compréhension du protocole SET et des mécanismes de cryptographie appliquée, les ressources suivantes sont recommandées.

### 1. Documentations Officielles et Standards
* **SET Specification (Book 1-3)** : Les documents originaux de Visa et MasterCard décrivant les spécifications techniques, les protocoles de messages et les architectures de certificats.
* **RFC 2828** : Glossaire de la sécurité Internet pour comprendre la terminologie des PKI (Public Key Infrastructure).
* **RFC 3447** : Public-Key Cryptography Standards (PKCS) #1: RSA Cryptography Specifications.

### 2. Litterature Academique
* **Applied Cryptography** (Bruce Schneier) : La référence pour comprendre l'implémentation des algorithmes RSA et la gestion des clés.
* **Cryptography and Network Security** (William Stallings) : Analyse détaillée des protocoles de paiement et des couches de transport sécurisées.
* **The SET Standard & E-Commerce Security** : Articles de recherche sur l'évolution de SET vers 3-D Secure.

### 3. Outils et Bibliotheques
* **PyCryptodome Documentation** : [https://pycryptodome.readthedocs.io/](https://pycryptodome.readthedocs.io/) - Documentation officielle pour comprendre les implémentations de `PKCS1_OAEP` et `RSA`.
* **Flask Documentation** : [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/) - Pour la gestion des sessions et du routage HTTP.
* **OpenSSL Guide** : Pour comparer l'implémentation Python avec les outils de ligne de commande standard de l'industrie.

---

## Comparaison Technique : SET vs SSL/TLS

| Caracteristique | Protocole SSL/TLS (Standard actuel) | Protocole SET (Ce projet) |
| :--- | :--- | :--- |
| **Authentification** | Client optionnel, Serveur obligatoire | Client, Marchand et Banque obligatoires |
| **Confidentialite** | Le marchand voit le numero de carte | Le marchand ne voit jamais le numero de carte |
| **Complexite** | Faible a moderee | Elevee (multiples signatures) |
| **Non-repudiation** | Non garantie nativement | Garantie par signatures numeriques fortes |



---

## Glossaire Technique pour le Projet

* **PAN (Primary Account Number)** : Le numéro de la carte bancaire, ici chiffré via RSA.
* **Double Signature** : Concept clé de SET liant les informations de commande et les informations de paiement sans les révéler à la mauvaise partie.
* **Enveloppe Numerique** : Combinaison de données chiffrées avec une clé symétrique, elle-même chiffrée par une clé publique.
* **Acquereur** : L'institution financière (banque) qui traite les paiements pour le marchand.

---

## Comment Contribuer
Si vous souhaitez améliorer ce projet pédagogique :
1. Examinez les issues pour les améliorations de l'interface.
2. Proposez des implémentations pour la gestion des **Certificats X.509** réels.
3. Ajoutez des tests unitaires pour valider les échanges de signatures.
