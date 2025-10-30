import pandas as pd
from TD_3.reddit_arxiv import *


# Fonction pour construire le corpus et le sauvegarder
def construire_corpus(theme):
    docs_reddit, source_reddit= reddit(theme)
    docs_arxiv,source_arxiv = arxiv(theme)
    
    # Création du deuxiéme colonnne contenant le texte
    docs = docs_reddit + docs_arxiv
    # Création du troisiéme colonne contenant son origine
    sources = source_reddit + source_arxiv
     # Création du premiére colonne contenant l'id
    id = list(range(1, len(docs) + 1))

    df = pd.DataFrame({
        "Id": id,
        "Texte": docs,
        "Sources": sources
    })

    # Sauvegarde
    return df.to_csv("Data\\corpus.csv", sep="\t", index=False, 
                     encoding="utf-8")

# Fonction pour charger le corpus
def charger_corpus():
    df_corpus = pd.read_csv("Data\\corpus.csv", sep="\t", encoding="utf-8")
    return df_corpus