Protocole SET - Démonstration Pédagogique
<div align="center">
https://img.shields.io/badge/Python-3.8%252B-blue?logo=python&logoColor=white
https://img.shields.io/badge/Flask-2.3.2-green?logo=flask&logoColor=white
https://img.shields.io/badge/License-MIT-yellow
https://img.shields.io/badge/Protocole-SET-orange

Implémentation complète du protocole SET avec cryptographie réelle et interface web interactive

Présentation • Installation • Fonctionnalités • Démo • Contribuer

</div>
📖 Présentation
Ce projet est une démonstration pédagogique complète du protocole SET (Secure Electronic Transaction), un standard historique de paiement sécurisé développé par Visa et MasterCard. L'application illustre les 11 étapes du protocole avec une implémentation cryptographique réelle (RSA 2048, SHA256).

🎯 Objectifs
🧠 Comprendre les mécanismes de sécurité des paiements électroniques

🔐 Expérimenter avec la cryptographie asymétrique

🖥️ Visualiser le flux complet d'une transaction SET

📚 Apprendre les concepts de sécurité par la pratique

<div align="center"> <img src="https://img.shields.io/badge/Étapes-11-blue" alt="11 étapes"> <img src="https://img.shields.io/badge/Cryptographie-RSA%202048-red" alt="RSA 2048"> <img src="https://img.shields.io/badge/Interface-Web%20Interactive-green" alt="Web Interactive"> <img src="https://img.shields.io/badge/Licence-MIT-lightgrey" alt="MIT License"> </div>
🚀 Installation Rapide
Prérequis
Python 3.8+

pip (gestionnaire de paquets)

Navigateur web moderne

Installation en 3 commandes
bash
# 1. Cloner le projet
git clone https://github.com/votre-username/set-protocol-demo.git
cd set-protocol-demo

# 2. Créer environnement virtuel
python -m venv venv

# 3. Activer et installer
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
Lancer l'application
bash
python app.py
Accédez à : http://localhost:5000 🚀

🏗️ Architecture
text
┌─────────────────────────────────────────┐
│        Interface Web (Bootstrap 5)      │
├─────────────────────────────────────────┤
│          Application Flask              │
│  • Routes SET (11 étapes)              │
│  • Gestion sessions                    │
│  • API REST                            │
├─────────────────────────────────────────┤
│      Module Cryptographique            │
│  • RSA 2048 - Génération clés         │
│  • PKCS1 OAEP - Chiffrement           │
│  • SHA256 - Signatures digitales      │
│  • Hachage sécurisé                   │
└─────────────────────────────────────────┘
✨ Fonctionnalités
✅ Les 11 Étapes SET Implémentées
Demande de certificat - Génération RSA 2048 bits

Certificat émis - Signature par autorité de certification

Opérateur SET - OT + PC chiffré + Signature

Envoi banque - Transmission sécurisée

Vérification - Structure, certificat, signature

Certification OK - Validation réussie

Demande d'achat - PAN chiffré RSA

Achat 2 phases - Autorisation + Capture

Aide solidaire + MEC - Support et messages

Enquête de crise - Surveillance anti-fraude

Confirmation - Transaction terminée

🔐 Cryptographie Réelle
python
# Exemple de code cryptographique
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Génération clés RSA 2048
key = RSA.generate(2048)
public_key = key.publickey().export_key()

# Chiffrement PKCS1 OAEP
cipher = PKCS1_OAEP.new(key.publickey())
encrypted_data = cipher.encrypt(b"Données sensibles")
🌐 Interface Web Moderne
Bootstrap 5 pour le design responsive

JavaScript vanilla pour l'interactivité

Chart.js pour les visualisations

Navigation intuitive étape par étape

📡 API REST Complète
Endpoint	Méthode	Description
/api/creer_operateur	POST	Crée l'opérateur SET
/api/envoyer_banque	POST	Envoie à la banque
/api/demander_achat	POST	Demande d'achat
/api/confirmer	POST	Confirmation finale
/api/status	GET	Statut session
🎮 Démonstration
Page d'Accueil
https://via.placeholder.com/800x400.png?text=SET+Protocol+Homepage

Création Opérateur SET
https://via.placeholder.com/800x400.png?text=Cr%C3%A9ation+Op%C3%A9rateur+SET

Vérifications Banque
https://via.placeholder.com/800x400.png?text=V%C3%A9rifications+Banque

Comment utiliser
Accédez à http://localhost:5000

Cliquez sur chaque étape dans l'ordre

Expérimentez avec les données de test

Observez la cryptographie en action

📁 Structure du Projet
text
set-protocol-demo/
├── app.py                    # Application principale (500+ lignes)
├── requirements.txt          # Dépendances Python
├── README.md                # Cette documentation
├── .gitignore              # Fichiers ignorés Git
└── templates/               # Interface utilisateur
    ├── index.html          # Page d'accueil avec les 11 étapes
    ├── etape1.html         # Étape 1: Demande certificat
    ├── etape2.html         # Étape 2: Certificat émis
    ├── etape3.html         # Étape 3: Opérateur SET
    ├── etape4.html         # Étape 4: Envoi banque
    ├── etape5.html         # Étape 5: Vérifications
    ├── etape7.html         # Étape 7: Demande achat
    ├── etape8.html         # Étape 8: Achat 2 phases
    ├── etape9.html         # Étape 9: Aide solidaire + MEC
    ├── etape10.html        # Étape 10: Enquête crise
    └── etape11.html        # Étape 11: Confirmation
🧪 Tests
Vérification de l'installation
bash
# Tester Python
python --version

# Tester les dépendances
python -c "import Flask; import Crypto; print('✓ Installation réussie')"

# Lancer en mode développement
FLASK_ENV=development python app.py
Données de test
json
{
  "pan": "4242424242424242",
  "marchand": "Amazon FR",
  "montant": 150.00
}
🤝 Contribuer
Les contributions sont les bienvenues ! Voici comment participer :

Fork le projet

Créez une branche (git checkout -b feature/amelioration)

Commitez vos changements (git commit -m 'Ajout d'une fonctionnalité')

Pushez vers la branche (git push origin feature/amelioration)

Ouvrez une Pull Request

Améliorations souhaitées
Ajouter des tests unitaires

Implémenter HTTPS avec certificat auto-signé

Ajouter une base de données pour la persistance

Créer un dashboard administrateur

Internationalisation (multi-langues)

Documentation API Swagger/OpenAPI

Normes de code
Respecter PEP 8 pour le Python

Commenter le code en français ou anglais

Ajouter des docstrings aux fonctions

Tester avant de soumettre

📚 Ressources Pédagogiques
Références SET
SET Specification Book 1-3 - Documentation officielle

RFC 2960 - Spécifications techniques

Wikipedia - SET - Vue d'ensemble

Cryptographie
PyCryptodome Documentation - Documentation de la bibliothèque

Applied Cryptography - Bruce Schneier - Livre de référence

Crypto101 - Cours gratuit de cryptographie

Apprentissage
Flask Documentation - Documentation Flask

Bootstrap 5 Docs - Documentation Bootstrap

MDN Web Docs - Références web

⚠️ Avertissements Importants
⚠️ POUR DÉMONSTRATION UNIQUEMENT
Cette application est strictement pédagogique :

🚫 NE PAS utiliser pour des transactions réelles

🚫 NE PAS déployer en production

🚫 NE PAS utiliser de vraies données de carte

🚫 AUCUNE garantie de sécurité pour un usage réel

Sécurité en développement
🔒 Clés stockées en session Flask (mémoire)

🌐 Serveur HTTP uniquement (pas HTTPS)

👤 Aucune authentification utilisateur

📝 Logs limités au debug

📄 Licence
Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.

text
MIT License

Copyright (c) 2024 SET Protocol Demo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
👥 Auteurs
Votre Nom - Développement initial - @votre-username

Contributeurs - Liste des contributeurs

🌟 Support
Si ce projet vous a été utile :

⭐ Donnez une étoile au repository

🔄 Partagez-le avec vos collègues

🐛 Signalez les bugs via Issues

💡 Proposez des améliorations

🏗️ Contribuez au code

📞 Contact
GitHub Issues : Ouvrir un issue

Email : votre-email@example.com

Documentation : Ce README

<div align="center">
🚀 Prêt à explorer le protocole SET ?
https://img.shields.io/badge/D%C3%A9marrer-maintenant-blue?style=for-the-badge

"Comprendre la sécurité par la pratique"

</div>
📊 Statistiques
https://img.shields.io/tokei/lines/github/votre-username/set-protocol-demo
https://img.shields.io/github/repo-size/votre-username/set-protocol-demo
https://img.shields.io/github/last-commit/votre-username/set-protocol-demo

🎓 Pour les Éducateurs
Ce projet est idéal pour :

Cours de sécurité informatique

Ateliers cryptographie

Projets étudiants

Formations professionnelles

Suggestions d'utilisation pédagogique :

Demander aux étudiants de suivre les 11 étapes

Faire modifier le code pour ajouter des fonctionnalités

Comparer SET avec des protocoles modernes (3D-Secure, etc.)

Analyser les forces/faiblesses cryptographiques

<div align="center">
Merci d'utiliser cette démonstration du protocole SET ! 🎉

⬆ Retour en haut

</div>
