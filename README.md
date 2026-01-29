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

1. Génération des clés
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

print("Clé publique générée avec succès.")

2. Simulation de chiffrement d'un PAN (Numéro de carte)
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

## Ressources et References sur le Protocole SET

### 1. Documentations de Référence (Standards)
* **SET Specifications (MasterCard & VISA)** :
    * *Book 1: Business Description* : Présentation des objectifs commerciaux et du modèle de confiance.
    * *Book 2: Technical Specification* : Détails des protocoles de messages et des formats de données.
    * *Book 3: Formal Protocol Definition* : Définition rigoureuse des échanges cryptographiques.
* **RFC 2828** : "Internet Security Glossary" – Pour comprendre le rôle des autorités de certification (CA) dans SET.
* **IETF RFC 3537** : "Wrapping Mechanisms for SET" – Détails sur l'encapsulation des clés.

### 2. Études Académiques et Analyses
* **"The SET Standard & E-Commerce Security"** : Analyse de la structure de la "Double Signature", l'innovation majeure de SET.
* **Applied Cryptography (Bruce Schneier)** : Section sur les protocoles de paiement électronique pour comprendre pourquoi SET a été conçu comme une alternative plus robuste que SSL/TLS pour le secteur bancaire.
* **"Analysis of the SET Purchase Protocol"** (Bella, Giampaolo, et al.) : Une étude formelle sur la vérification de la sécurité du protocole.

### 3. Ressources en Ligne
* **Archives Visa/MasterCard** : Historique du développement du standard (disponible via les archives du Web).
* **Documentation PyCryptodome** : Pour comprendre l'implémentation pratique des primitives RSA et SHA utilisées dans ce projet.

---

## Focus Technique : Les 11 Etapes du Protocole SET

Le protocole SET est conçu pour garantir qu'aucune information sensible n'est exposée à une partie qui n'en a pas besoin. Voici le détail des phases simulées dans ce projet :



### Phase d'Initialisation
1. **Demande de certificat** : Le titulaire de la carte génère ses clés et demande un certificat numérique.
2. **Émission** : L'Autorité de Certification (CA) valide l'identité et signe le certificat.
3. **Opérateur SET** : Le portefeuille électronique (Wallet) du client est activé.

### Phase de Transaction
4. **Envoi Banque** : Le client transmet ses certificats au marchand, qui les relaie à la banque.
5. **Vérification** : La banque acquéreuse authentifie le client et le marchand via leurs signatures.
6. **Certification OK** : La banque confirme que toutes les parties sont de confiance.

### Phase de Paiement (L'innovation de la Double Signature)
7. **Demande d'achat** : Le client envoie au marchand deux informations liées :
    * Le détail de la commande (lisible par le marchand, mais pas par la banque).
    * Les informations de paiement (chiffrées pour la banque, invisibles pour le marchand).
    * *La Double Signature lie ces deux éléments sans en révéler le contenu.*
8. **Achat 2 phases** : 
    * *Autorisation* : La banque vérifie les fonds et bloque le montant.
    * *Capture* : Le transfert réel des fonds est effectué après validation du marchand.

### Phase de Clôture et Support
9. **Gestion MEC (Message Error Check)** : Protocole de gestion des erreurs de transmission.
10. **Enquête de Crise** : Procédures de détection de fraude et de gestion des litiges.
11. **Confirmation** : Envoi du reçu final signé numériquement au client.

---

## Comparaison Technique : SET vs SSL/TLS

| Caracteristique | Protocole SSL/TLS (Standard actuel) | Protocole SET (Ce projet) |
| :--- | :--- | :--- |
| **Authentification** | Client optionnel, Serveur obligatoire | Client, Marchand et Banque obligatoires |
| **Confidentialite** | Le marchand voit le numero de carte | Le marchand ne voit jamais le numero de carte |
| **Complexite** | Faible a moderee | Elevee (multiples signatures) |
| **Non-repudiation** | Non garantie nativement | Garantie par signatures numeriques fortes |



---

## Glossaire pour le Notebook
* **Dual Signature (Double Signature)** : Technique permettant de prouver que le paiement est lié à une commande spécifique sans que le marchand voie le numéro de carte, ni que la banque voie le détail des articles achetés.
* **Merchant Certificate** : Preuve numérique que le marchand est autorisé par une banque à accepter les paiements SET.
* **Payment Gateway** : L'interface gérée par l'acquéreur qui déchiffre les instructions de paiement du client. 
