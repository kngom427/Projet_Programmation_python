# 🔎 Moteur de recherche

## 📌 Présentation

Ce projet a été réalisé dans le cadre du module **Programmation de spécialité (Python)** en **Master 1 Informatique – Université Lumière Lyon 2**.

L’objectif est de concevoir et implémenter un **moteur de recherche d’information textuelle** sans utiliser de bibliothèques de haut niveau dédiées au NLP (comme `nltk` ou `scikit-learn`), afin de comprendre en profondeur les mécanismes fondamentaux de :

* l’acquisition de données textuelles,
* la structuration d’un corpus,
* l’analyse de texte,
* la recherche d’information via **TF** et **TF-IDF**.

Le projet a été développé de manière incrémentale à travers les **TD 3 à TD 10**.

### Version

- Version **v1** : comprend **TD3, TD4 et TD5**
- Version **v2** : comprend **TD3, TD4, TD5, TD6 et TD7**
- Version **v1** : comprend **TD3 à TD10**

---

## 👥 Auteurs

* **Khadim NGOM**
* **Serigne Saliou THIAM**

📚 Master 1 Informatique 
🏫 Université Lumière Lyon 2
📅 Année universitaire : **2025–2026**

🔗 Dépôt GitHub :
[https://github.com/kngom427/Projet_Programmation_python]

---

## ⚙️ Fonctionnalités principales

* Saisie d’une requête utilisateur (un ou plusieurs mots-clés)
* Choix du nombre de résultats à afficher
* Calcul de scores de pertinence (TF / TF-IDF)
* Classement des documents par similarité
* Affichage des résultats (titre, auteur, date, score)
* Construction et sauvegarde d’un corpus textuel
* Exploration interactive du corpus via notebooks

---

## 🗂️ Organisation du projet

```
MOTEUR-DE-RECHERCHE/
│
├── data/                     # Données et corpus sauvegardés
│   ├── corpus.csv
│   ├── corpus_IA.csv
│   ├── corpus_Machine_learning.csv
│   └── discours_US.csv
│
├── notebooks/                # Interfaces et visualisations
│   ├── piste_TD9_10.ipynb
│   └── user_interface.ipynb
│
├── src/
│   ├── TD3/                  # Acquisition des données
│   │   ├── fetch_data.py
│   │   ├── corpus_builder.py
│   │   └── main_TD3.py
│   │
│   ├── TD4_5_6/               # Modélisation objet & corpus
│   │   ├── Author.py
│   │   ├── Document.py
│   │   ├── Corpus.py
│   │   ├── Factory.py
│   │   └── main_TD4_5_6.py
│   │
│   ├── TD7/                   # Moteur de recherche
│   │   ├── SearchEngine.py
│   │   └── main_TD7.py
│
├── tests/                     # Tests unitaires (pytest)
│   ├── test_clean_text.py
│   ├── test_construire_corpus.py
│   └── test_corpus.py
│
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧠 Architecture logicielle

### Principales classes

* **Document** : représentation générique d’un document (titre, auteur, date, texte, url)
* **RedditDocument / ArxivDocument** : spécialisations de `Document`
* **Author** : gestion des auteurs et de leurs productions
* **Corpus** *(Singleton)* : gestion centrale des documents et analyses textuelles
* **DocumentFactory** *(Factory Pattern)* : création abstraite des documents
* **SearchEngine** : construction TF / TF-IDF et calcul de similarité

---

## 🔍 Algorithmes utilisés

* Nettoyage et normalisation du texte
* Construction du vocabulaire
* Matrice **TF** (Term Frequency) avec matrices creuses
* Pondération **TF-IDF**
* Vectorisation des requêtes utilisateur
* Recherche par **similarité cosinus** (produit scalaire)

Optimisations :

* Utilisation de `scipy.sparse.csr_matrix`
* Calcul uniquement sur valeurs non nulles

---

## 🧪 Tests

Les tests sont réalisés avec **pytest**.

### Tests unitaires

* `test_clean_text.py` : nettoyage de texte
* `test_corpus.py` : classe Corpus (statistiques, Singleton)
* `test_construire_corpus.py` : création et sauvegarde du corpus

Lancer les tests :

```bash
pytest
```

---

## 🖥️ Interfaces utilisateur

### Interface moteur de recherche

* Réalisée avec **Jupyter Notebook** et **ipywidgets**
* Saisie de requête
* Sélection du nombre de résultats
* Affichage tabulaire des documents pertinents

📓 Notebook : `notebooks/user_interface.ipynb`

### Interface d’exploration du corpus (TD9–TD10)

* Analyse visuelle du corpus
* Filtres et statistiques
* Graphiques de fréquence

📓 Notebook : `notebooks/piste_TD9_10.ipynb`

---

## 🚀 Installation et exécution

### Prérequis

* Python ≥ 3.9

### Installation

```bash
pip install -r requirements.txt
```

### Exécution des TD

```bash
python src/TD3/main_TD3.py
python src/TD4_5_6/main_TD4_5_6.py
python src/TD7/main_TD7.py
```

---

## ⚠️ Problèmes rencontrés

* **Caractères spéciaux** → Résolu avec l’encodage UTF-8
* **Limites de calcul** sur corpus volumineux → Optimisation via matrices creuses

---

## 📈 Perspectives d’amélioration

* Déploiement via une API REST (Flask)
* Interface web complète
* Amélioration du ranking (BM25, embeddings)
* Indexation persistante

---

## 📄 Licence

Projet académique – usage pédagogique uniquement.
