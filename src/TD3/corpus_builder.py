import os
import pandas as pd
import sys

sys.path.append(os.path.dirname(__file__))
from fetch_data import (
    fetch_reddit_posts,
    fetch_arxiv_summaries
)


# -------------------------------------------------------------------
#  Construire et sauvegarder le corpus
# -------------------------------------------------------------------
def construire_corpus(theme, reddit_client=None, save_path="../../data/"):
    """
    Récupère les textes Reddit et Arxiv, construit un DataFrame, et le sauvegarde.

    Paramètres :
        theme (str)            : mot-clé recherché
        reddit_client (object) : client Reddit optionnel
        save_path (str)        : emplacement du fichier cSV

    Retour :
        df (DataFrame) : corpus construit
    """

    # 1️ Récupération des textes
    docs_reddit = fetch_reddit_posts(theme, limit=30, reddit_client=reddit_client)
    docs_arxiv = fetch_arxiv_summaries(theme, max_results=20)

    # 2️ Création des colonnes source
    sources_reddit = ["reddit"] * len(docs_reddit)
    sources_arxiv = ["arxiv"] * len(docs_arxiv)

    docs = docs_reddit + docs_arxiv
    sources = sources_reddit + sources_arxiv
   

    # 3️ Construction du DataFrame
    df = pd.DataFrame({
        "Texte": docs,
        "Source": sources
    })
    
    filename=f"corpus_{theme.replace(' ','_')}.csv"
    
    full_save_path=os.path.join(save_path, filename)

    # 4️ Création du dossier si nécessaire
    os.makedirs(os.path.dirname(full_save_path), exist_ok=True)

    # 5️ Sauvegarde
    df.to_csv(full_save_path, sep="\t", index=False, encoding="utf-8")
    print(f" Corpus sauvegardé dans : {full_save_path}")

    return df



# -------------------------------------------------------------------
#  Charger un corpus déjà sauvegardé
# -------------------------------------------------------------------
def charger_corpus(path="../../data/corpus.csv"):
    """
    Charge le corpus depuis un fichier TSV.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f" Fichier non trouvé : {path}")

    df = pd.read_csv(path, sep="\t", encoding="utf-8")
    print(f" Corpus chargé : {len(df)} documents.")
    return df



# -------------------------------------------------------------------
#  Analyse du corpus : taille, mots, phrases, nettoyage
# -------------------------------------------------------------------
def analyser_corpus(df):
    """
    Affiche et retourne une analyse simple du corpus.
    """

    print(f"\n Taille initiale du corpus : {len(df)} documents\n")

    # 1️ Nombre de mots et phrases par document
    for i, texte in enumerate(df["Texte"], start=1):
        nb_mots = len(texte.split())
        nb_phrases = len(texte.split("."))
        print(f"• Document {i} : {nb_mots} mots | {nb_phrases} phrases")

    # 2️ Suppression des documents trop courts (< 20 caractères)
    taille_initiale = len(df)
    df = df[df["Texte"].str.len() >= 20].reset_index(drop=True)
    taille_finale = len(df)

    print(f"\n Nettoyage : {taille_initiale - taille_finale} documents supprimés.")
    print(f" Taille finale du corpus : {taille_finale} documents.\n")

    # 3️ Chaîne géante pour la suite
    chaine_corpus = " ".join(df["Texte"].tolist())
    print(f" Exemple du texte fusionné : {chaine_corpus[:150]}...\n")

    return df, chaine_corpus
