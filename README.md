# 🔐 Protocole SET - Démonstration Pédagogique

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.2-green?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![SET Protocol](https://img.shields.io/badge/Protocole-SET-orange)](https://en.wikipedia.org/wiki/Secure_Electronic_Transaction)

**Implémentation complète du protocole SET avec cryptographie réelle et interface web interactive**

[Présentation](#-présentation) • [Installation](#️-installation-rapide) • [Fonctionnalités](#-fonctionnalités) • [Utilisation](#-utilisation) • [Contribuer](#-contribuer)

</div>

## 📖 Présentation

Ce projet est une **démonstration pédagogique complète** du protocole **SET (Secure Electronic Transaction)**, un standard historique de paiement sécurisé développé par Visa et MasterCard. L'application illustre les 11 étapes du protocole avec une implémentation cryptographique réelle (RSA 2048, SHA256).

### 🎯 Objectifs
- 🧠 **Comprendre** les mécanismes de sécurité des paiements électroniques
- 🔐 **Expérimenter** avec la cryptographie asymétrique
- 🖥️ **Visualiser** le flux complet d'une transaction SET
- 📚 **Apprendre** les concepts de sécurité par la pratique

## 🚀 Installation Rapide

### Prérequis
- Python 3.8+
- pip (gestionnaire de paquets)
- Navigateur web moderne

### Installation en 3 commandes
```bash
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
pip install Flask==2.3.2 pycryptodome==3.18.0
