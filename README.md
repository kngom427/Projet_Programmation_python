# Projets en Programmation de Spécialité : Python
👨‍💻 Réalisé par Khadim NGOM & Serigne Saliou THIAM – Master 1 Informatique, Lyon 2

Dans le cadre de ce projet, On a développé un programme en Python en suivant l’ensemble des étapes du cycle de vie logiciel : la spécification, l’analyse, la conception, le codage, la vérification et la maintenance. Ce travail nous a  permis de mettre en pratique nos compétences en programmation et de démontrer notre capacité à concevoir une application complète, bien structurée et évolutive.
Le projet s’appuie sur les TD 3 à 10, dont les deux derniers offrent davantage de liberté dans la conception. Le rendu se fait en trois versions successives, chacune représentant une étape d’évolution et d’amélioration du projet.
## TD 3 : acquisition de données 
### Objectifs:
Construire un premier corpus textuel à partir de sources externes **(Reddit et Arxiv)**, le nettoyer et le sauvegarder pour éviter de réinterroger les APIs.

- Collecte des textes via praw (Reddit) et urllib/xmltodict (Arxiv).

- Nettoyage des contenus (\n, textes trop courts).

- Structuration dans un DataFrame avec id, texte, source.

- Sauvegarde au format .csv et possibilité de rechargement.

 **Résultat** : un corpus brut mais exploitable, prêt pour les étapes suivantes.

## TD 4 : Structuration orientée objet
### Objectifs : 
Organiser le projet avec une approche orientée objet pour rendre le corpus évolutif et maintenable.

- Création de la classe **Document** (titre, auteur, date, url, texte).

- Création de la classe **Author** (nom, nombre de documents, dictionnaire de production).

- Création de la classe **Corpus** (nom, auteurs, documents, méthodes d’affichage et de gestion).

**Résultat** : une architecture claire, avec des objets pour représenter les documents, les auteurs et le corpus.

 ## TD 5 : Héritage et patrons de conception
 ### Objectifs
 Enrichir le projet en introduisant l’héritage et des patrons de conception pour gérer différents types de documents et améliorer la flexibilité du corpus.

 - Création de deux classes filles :

    - **RedditDocument** : hérite de Document et ajoute un     champ spécifique (ex. nombre de commentaires).

    - **ArxivDocument** : hérite de Document et ajoute la gestion des co-auteurs.

- Mise à jour de la classe Corpus pour accueillir ces nouveaux types de documents grâce au polymorphisme.

- Ajout d’un champ type et d’une méthode getType() pour identifier la source (Reddit ou Arxiv).

- Mise en place de deux patrons de conception :

   - **Singleton** : garantir qu’un seul corpus est manipulé.

   - **Factory** : générer des documents selon leur type (Reddit ou Arxiv).

 **Résultat** : un corpus enrichi, extensible et mieux structuré, prêt pour les analyses avancées.
 ## TD 6 : Analyse du contenu textuel
  - Mettre en pratique l’utilisation des expressions régulières **(re)** pour analyser le contenu textuel.

 - Implémenter une fonction **search** dans la classe Corpus afin de retrouver les passages contenant un mot‑clé.

 - Construire un **concordancier (concorde)** qui affiche le contexte gauche et droit autour d’un motif trouvé.

 - Nettoyer les textes **(nettoyer_texte)** pour uniformiser le corpus :

 - mise en minuscules, suppression des chiffres, ponctuations et retours à la ligne.

 - Construire un vocabulaire des mots du corpus en supprimant les doublons.

 - Calculer des statistiques lexicales :

     - nombre de mots différents,

     - fréquence des mots,

     - fréquence documentaire.

## TD7 : Moteur de recherche en Python
### Objectifs
- La construction d’un **vocabulaire** (mots uniques du corpus, avec identifiant, fréquence et document frequency(voir TD6)).

- La création d’une **matrice Documents × Termes (TF et TF×IDF)**.

 - Une recherche basée sur la **similarité cosinus** entre la requête et les documents.

 - Une classe **SearchEngine** qui prend un Corpus en entrée et retourne les résultats sous forme de DataFrame.

---
## Prérequis
- Python 3.10 ou supérieur

## Installation
Avant de lancer le projet, installe les dépendances :

```bash
pip install -r requirements.txt
```
## strucure du Projet
```bash
python_project/
├── TD_3/
│   ├── reddit_arxiv.py   # récupération des textes
│   ├── corpus_builder.py  # construction, chargement et analyse
│   ├── main_td3.py        # test
├── TD_4_5_6/
│   ├── __init__.py # fichier vide     
│   ├── Document.py       # classe Document
│   ├── Author.py         # classe Author
│   ├── corpus.py         # classe Corpus
│   ├── Factory.py        # gere les type
│   ├── main_td6.py          # test
├── TD_7/
│   ├── __init__.py # fichier vide     
│   ├── SearchEngine.py       # classe moteur de recherche
│   ├── main_td7.py # test    
├── Data/                 # corpus sauvegardé
│   ├── corpus.csv
├── README.md             # ce fichier
├── requirements.txt      # librairies nécessaires

```
## Comment exécuter
### Cloner le projet
```bash
git clone https://github.com/kngom427/Projet_Programmation_python.git
cd Projet_TP_Python
```

## Version

- Version **v1** : comprend TD3, TD4 et TD5
-  Version **v2** : comprend TD3, TD4, TD5, TD6 et TD7

