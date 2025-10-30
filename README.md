# Projets en Programmation de Spécialité : Python
👨‍💻 Réalisé par Khadim & Saliou – Master 1 Informatique, Lyon 2

Dans le cadre de ce projet, j’ai développé un programme en Python en suivant l’ensemble des étapes du cycle de vie logiciel : la spécification, l’analyse, la conception, le codage, la vérification et la maintenance. Ce travail m’a permis de mettre en pratique mes compétences en programmation et de démontrer ma capacité à concevoir une application complète, bien structurée et évolutive.
Le projet s’appuie sur les TD 3 à 10, dont les deux derniers offrent davantage de liberté dans la conception. Le rendu se fait en trois versions successives, chacune représentant une étape d’évolution et d’amélioration du projet.
## TD 3 : acquisition de données (version 1)
### Objectifs:
#### Partie 1 — Collecte des données
**But** : extraire des documents textuels à partir de sources externes (APIs).

1.1 Interroger Reddit avec la librairie praw pour récupérer le champ textuel selftext.

1.2 Interroger Arxiv avec urllib et parser les résultats XML avec xmltodict.

1.3 Nettoyer les textes (supprimer les \n).

1.4 Alimenter une liste Python docs contenant uniquement le contenu textuel des documents.
#### Partie 2 — Construction et sauvegarde du corpus
**But** : éviter de réinterroger les APIs à chaque exécution.

2.1 Créer un DataFrame pandas avec trois colonnes :

id → identifiant unique du document

texte → contenu textuel du document

source → origine du texte (reddit ou arxiv)

2.2 Sauvegarder ce tableau sur disque au format .csv avec le séparateur de tabulation \t.

2.3 Ajouter du code permettant de recharger directement ce fichier lors d’une prochaine exécution, sans repasser par les appels API
#### Partie 3 — Premières manipulations du corpus
**But** : explorer et préparer les données textuelles.

3.1 Afficher la taille du corpus (nombre de documents).

3.2 Calculer, pour chaque document, le nombre de mots et de phrases (avec split(" ") et split(".")).

3.3 Supprimer les documents trop courts (< 20 caractères).

3.4 Fusionner tous les textes en une seule chaîne de caractères (" ".join(...)) pour une analyse globale.

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
├── td3/
│   ├── reddit_arxiv.py # recupération des textes
│   ├── corpus.py # construction et chargement du corpus
│   ├── analyze.py # analyse du corpus
├── main.py # fichier principale
├── data/  # corpus sauvegardé
├── README.md  # ce fichier
├── requirements.txt # librairies necesssaires
```
## Version

- Version **v1** : comprend TD3, TD4 et TD5

