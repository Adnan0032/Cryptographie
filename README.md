#  Protocole SET - Démonstration Pédagogique

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.2-green?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![SET Protocol](https://img.shields.io/badge/Protocole-SET-orange)](https://en.wikipedia.org/wiki/Secure_Electronic_Transaction)

**Implémentation complète du protocole SET avec cryptographie réelle et interface web interactive**

[Présentation](#-présentation) • [Installation](#️-installation-rapide) • [Fonctionnalités](#-fonctionnalités) • [Utilisation](#-utilisation) • [Contribuer](#-contribuer)

# Protocole SET - Demonstration Pedagogique

## Presentation

Ce projet propose une implementation complete et pedagogique du protocole **Secure Electronic Transaction (SET)**. Ce standard, developpe par Visa et MasterCard, constitue une reference historique dans la securisation des transactions de paiement electronique via une infrastructure a cles publiques (PKI).

L'application demontre les 11 etapes du protocole, en integrant une couche cryptographique reelle (RSA 2048 bits et SHA-256) pour illustrer les echanges entre le client, le marchand et l'acquereur.

## Objectifs de l'Application

* **Analyse de Flux** : Visualiser les echanges de donnees entre les trois parties prenantes du modele SET.
* **Mise en Pratique Cryptographique** : Experimenter le chiffrement asymetrique, les signatures numeriques et le hachage.
* **Securite des Donnees** : Comprendre le principe de l'enveloppe numerique et du chiffrement du numero de carte (PAN).

## Architecture Technique

### Pile Logicielle
* **Serveur Applicatif** : Python 3.8+ utilisant le micro-framework Flask.
* **Moteur Cryptographique** : Bibliotheque PyCryptodome (RSA 2048, PKCS1 OAEP, SHA-256).
* **Interface Utilisateur** : HTML5 / Bootstrap 5 pour une navigation etape par etape.

### Structure du Projet
```text
set-protocol-demo/
├── app.py                # Logique serveur et orchestration des 11 etapes
├── requirements.txt      # Dependances Python (Flask, PyCryptodome)
├── templates/            # Interface utilisateur (12 fichiers HTML)
│   ├── index.html        # Tableau de bord principal
│   └── etape1_11.html    # Vues detaillees par etape
└── static/               # Fichiers CSS et JavaScript
Installation et LancementPrerequisEnvironnement Python 3.8 ou superieur.Gestionnaire de paquets pip.Procedure d'installationClonage du depotBashgit clone [https://github.com/votre-username/set-protocol-demo.git](https://github.com/votre-username/set-protocol-demo.git)
cd set-protocol-demo
Configuration de l'environnement virtuelBashpython -m venv venv
# Sous Windows
venv\Scripts\activate
# Sous Linux/Mac
source venv/bin/activate
Installation des dependancesBashpip install Flask==2.3.2 pycryptodome==3.18.0
ExecutionBashpython app.py
L'interface est accessible via l'adresse locale : http://localhost:5000Fonctionnalites et Etapes du ProtocoleWorkflow des 11 EtapesL'application decompose le protocole SET selon l'ordre officiel :Demande de certificat : Generation des cles RSA 2048.Emission : Signature du certificat par l'Autorite de Certification.Initialisation : Configuration de l'operateur SET.Envoi Banque : Transmission de l'enveloppe numerique.Verification : Controle de l'integrite et des signatures.Certification : Validation de l'identite du porteur.Demande d'achat : Chiffrement du PAN et des donnees de commande.Phase d'Achat : Processus d'autorisation et de capture.Gestion MEC : Traitement des messages d'erreur et aide solidaire.Enquete de Crise : Surveillance anti-fraude et monitoring.Confirmation : Cloture de la transaction et archivage.Exemple d'Implementation CryptographiquePythonfrom Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Exemple de chiffrement utilise dans le module
key = RSA.generate(2048)
cipher = PKCS1_OAEP.new(key.publickey())
encrypted_data = cipher.encrypt(b"Donnees Sensibles")
Specifications de l'APIEndpointMethodeAction/api/creer_operateurPOSTInitialise les parametres de session SET./api/envoyer_banquePOSTTransmet les donnees a l'entite acquereur./api/demander_achatPOSTExecute la demande d'autorisation d'achat./api/statusGETRecupere l'etat actuel du workflow.Avertissements de SecuriteUsage Pedagogique Uniquement : Ce projet est une simulation. Il ne doit en aucun cas etre utilise pour traiter de veritables paiements.Donnees de Test : N'utilisez jamais de vrais numeros de carte bancaire (PAN) ou donnees personnelles lors des tests.Production : Le serveur de developpement Flask n'est pas adapte pour une exposition sur un reseau public.LicenceCe projet est sous licence MIT.Contact et ContributionAuteur : Votre Nom / @votre-usernameContributions : Les Pull Requests sont les bienvenues pour l'ajout de tests unitaires ou l'amelioration de l'interface.
