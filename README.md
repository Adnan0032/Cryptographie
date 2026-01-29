#  Protocole SET - Démonstration Pédagogique

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.2-green?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![SET Protocol](https://img.shields.io/badge/Protocole-SET-orange)](https://en.wikipedia.org/wiki/Secure_Electronic_Transaction)

**Implémentation complète du protocole SET avec cryptographie réelle et interface web interactive**

[Présentation](#-présentation) • [Installation](#️-installation-rapide) • [Fonctionnalités](#-fonctionnalités) • [Utilisation](#-utilisation) • [Contribuer](#-contribuer)
## Présentation du Projet

Ce projet est une implémentation logicielle à visée éducative du protocole **Secure Electronic Transaction (SET)**. Développé initialement par Visa et MasterCard, le protocole SET est un standard de sécurité conçu pour protéger les transactions par carte de paiement sur les réseaux ouverts comme Internet.

L'application simule les interactions entre le détenteur de carte (Client), le commerçant (Merchant) et la banque (Acquirer) en utilisant des algorithmes de cryptographie asymétrique réels.

## Objectifs Pédagogiques

* **Compréhension des Flux** : Visualiser les 11 étapes clés du processus de paiement sécurisé.
* **Cryptographie Pratique** : Manipulation de clés RSA 2048 bits, de signatures numériques et de fonctions de hachage SHA-256.
* **Concepts de Sécurité** : Étude de l'enveloppe numérique, de la double signature et de l'infrastructure à clés publiques (PKI).

## Architecture Technique

### Technologies Employées

* **Backend** : Python 3.8+ avec le framework Flask pour l'orchestration des requêtes.
* **Sécurité** : PyCryptodome pour la gestion des opérations cryptographiques.
* **Frontend** : HTML5 et Bootstrap 5 pour une interface utilisateur structurée.

### Structure du Répertoire
set-protocol-demo/
├── app.py                    # Logique serveur et moteur cryptographique
├── requirements.txt          # Dépendances logicielles
├── templates/                # Interface utilisateur
│   ├── index.html            # Menu principal
│   └── etape[1-11].html      # Vues détaillées de chaque phase
└── static/                   # Ressources statiques (CSS/JS)
I
nstallation et Mise en Route
Prérequis
Python version 3.8 ou supérieure.

Gestionnaire de paquets pip.

Procédure d'installation
Clonage du dépôt

git clone https://github.com/votre-username/set-protocol-demo.git
cd set-protocol-demo
Configuration de l'environnement

python -m venv venv
# Activation (Windows)
venv\Scripts\activate
# Activation (Linux/Mac)
source venv/bin/activate
Installation des bibliothèques

pip install Flask==2.3.2 pycryptodome==3.18.0
Lancement de l'application

python app.py
L'application sera disponible à l'adresse : http://localhost:5000

Fonctionnalités Implémentées
Workflow SET (11 Étapes)

Demande de certificat : Génération de la paire de clés RSA.

Émission : Signature du certificat par l'Autorité de Certification (CA).

Initialisation : Paramétrage de l'opérateur de transaction.

Envoi Banque : Transmission de la demande d'autorisation à l'acquéreur.

Vérification : Contrôle de l'intégrité des messages et des certificats.

Certification : Validation de l'identité des intervenants.

Demande d'achat : Chiffrement du PAN et des données de commande.

Phase d'Achat : Processus d'autorisation et de capture des fonds.

Gestion MEC : Traitement des messages d'erreur et aide solidaire.

Enquête de Crise : Surveillance anti-fraude et monitoring des risques.

Confirmation : Clôture de la transaction et archivage des preuves.

Spécifications de l'API
Méthode	Endpoint	Action
POST	/api/creer_operateur	Initialise les paramètres de session SET
POST	/api/envoyer_banque	Transmet l'enveloppe numérique à l'acquéreur
POST	/api/demander_achat	Soumet la requête d'autorisation finale
GET	/api/status	Récupère l'état actuel du workflow
Sécurité et Confidentialité
Cryptographie Réelle
Contrairement à une simple simulation visuelle, ce projet utilise des primitives cryptographiques standards :

RSA 2048 : Pour l'échange de clés et la signature.

PKCS1 OAEP : Pour le remplissage (padding) lors du chiffrement.

SHA-256 : Pour garantir l'intégrité des messages.

Avertissements
Environnement de Test : Ce code est destiné à un usage local uniquement.

Données Sensibles : Ne saisissez jamais de vrais numéros de carte bancaire. Utilisez les données de test fournies dans l'interface.

Production : Le serveur Flask intégré n'est pas sécurisé pour une exposition publique.

Licence
Ce projet est distribué sous la licence MIT.

Contact
Développement initial par Adnane Ammi Douah- adnanammidouah@gmail.com
