import pandas as pd
from reddit_arxiv import *
import os

def construire_corpus(theme, save_path="Data\\corpus.csv"):
    """
    Récupère les données Reddit et Arxiv, construit le corpus et le sauvegarde.
    """
    docs_reddit, sources_reddit = reddit(theme)
    docs_arxiv, sources_arxiv = arxiv(theme)

    # Combinaison des deux sources
    docs = docs_reddit + docs_arxiv
    sources = sources_reddit + sources_arxiv
    ids = list(range(1, len(docs) + 1))

    # Construction du DataFrame
    df = pd.DataFrame({
        "Id": ids,
        "Texte": docs,
        "Source": sources
    })

    # Création du dossier data si nécessaire
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, sep="\t", index=False, encoding="utf-8")

    print(f" Corpus sauvegardé dans {save_path}")
    return df


def charger_corpus(path="Data\\corpus.csv"):
    """
    Charge le corpus depuis un fichier CSV.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Fichier non trouvé : {path}")
    df = pd.read_csv(path, sep="\t", encoding="utf-8")
    print(f" Corpus chargé ({len(df)} documents).")
    return df


def analyser_corpus(df):
    """
    Effectue des analyses simples : taille, nombre de mots, filtrage, etc.
    """
    print(f"\n Taille initiale du corpus : {len(df)} documents\n")

    for i, texte in enumerate(df["Texte"], start=1):
        nb_mots = len(texte.split())
        nb_phrases = len(texte.split('.'))
        print(f"Document {i} : {nb_mots} mots, {nb_phrases} phrases")

    # Suppression des documents trop courts (< 20 caractères)
    taille_initiale = len(df)
    df = df[df["Texte"].str.len() >= 20].reset_index(drop=True)
    taille_finale = len(df)

    print(f"\n Nettoyage : {taille_initiale - taille_finale} documents supprimés.")
    print(f" Taille finale du corpus : {taille_finale} documents.\n")

    # Chaîne géante pour la suite
    chaine_corpus = " ".join(df["Texte"].tolist())
    print(f"Exemple de texte fusionné : {chaine_corpus[:150]}...\n")

    return df, chaine_corpus