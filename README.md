# 🚇 Projet Métro Parisien

Bienvenue dans le projet qui modélise le réseau du métro parisien à l'aide de Neo4j et d'un script Python pour le calcul d'itinéraires.

---

## 🛠️ Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- **Docker** : Pour exécuter Neo4j dans un conteneur.
- **Python 3.x** : Pour exécuter le script Python.
- **Pip** : Pour gérer les bibliothèques Python.

---

## 🚀 Installation de Docker

1. **Téléchargez Docker** :

   - Visitez [Docker Desktop](https://www.docker.com/products/docker-desktop).

2. **Installation** :

   - Suivez les instructions d'installation adaptées à votre système d'exploitation.

3. **Vérification de l'installation** :

   - Exécutez la commande suivante dans un terminal :

     ```bash
     docker --version
     ```

---

## 🖥️ Installation de Neo4j via Docker

1. **Lancer Neo4j** :

   - Dans un terminal, exécutez :

     ```bash
     docker run \
       --name neo4j \
       -p 7474:7474 -p 7687:7687 \
       -e NEO4J_AUTH=neo4j/password \
       -d neo4j:latest
     ```

2. **Accéder à Neo4j** :
   - Ouvrez votre navigateur et allez à [http://localhost:7474](http://localhost:7474).
   - Connectez-vous avec :
     - **Nom d'utilisateur** : `neo4j`
     - **Mot de passe** : `password`

---

## 📁 Préparation des Données

1. **Téléchargement des fichiers** :

   - Récupérez les fichiers :
     - [stations.csv](https://github.com/pauldechorgnat/cool-datasets/raw/master/ratp/stations.csv)
     - [liaisons.csv](https://github.com/pauldechorgnat/cool-datasets/raw/master/ratp/liaisons.csv)

2. **Placement des fichiers** :
   - Placez-les dans un dossier nommé `data`.

---

## 📊 Chargement des Données dans Neo4j

1. **Charger `build_graph.txt`** :

   - Dans Neo4j Browser, exécutez :

     ```cypher
     :source /data/build_graph.txt
     ```

---

## 🔍 Exécution des Requêtes d'Exploration

1. **Charger `data_exploration.txt`** :

   - Dans Neo4j Browser, exécutez :

     ```cypher
     :source /data/data_exploration.txt
     ```

2. **Exécution des requêtes** :
   - Exécutez chaque requête pour voir les résultats, en vérifiant les commentaires pour explications.

---

## 🐍 Installation de Python et des Bibliothèques

1. **Télécharger Python** :

   - Si nécessaire, téléchargez-le depuis [python.org](https://www.python.org/downloads/).

2. **Installer la bibliothèque `neo4j`** :

   - Dans un terminal, exécutez :

     ```bash
     pip install neo4j
     ```

---

## ✈️ Exécution du Script Python pour Trouver un Itinéraire

1. **Lancer le script** :

   - Dans le terminal, exécutez :

     ```bash
     python itinerary.py
     ```

   - Modifiez les coordonnées dans le script pour les stations désirées.

---

## 👤 Développeur

- **S-DEV**

Merci et bonne exploration du réseau parisien ! 🚆
