import pandas as pd
from Corpus import Corpus

#Convertisseur TD3 -> TD5 
def convert_td3_to_td5(old_file="Data\\corpus.csv", new_file="Data\\Corpus.csv"):
    df = pd.read_csv(old_file, sep="\t", encoding="utf-8")

    # Création des colonnes enrichies
    df_new = pd.DataFrame({
        "id": df["Id"],
        "titre": ["Doc " + str(i) for i in df["Id"]],   # titre générique
        "auteur": df["Source"],                         # auteur = source
        "date": ["2025-01-01"] * len(df),               # valeur par défaut
        "url": ["" for _ in range(len(df))],            # vide
        "texte": df["Texte"]
    })

    df_new.to_csv(new_file, sep="\t", index=False, encoding="utf-8")
    print(f" Conversion terminée : {new_file}")


# Main avec tests TD6 
def main():
    # 1. Conversion TD3 -> TD5
    convert_td3_to_td5("Data\\corpus.csv", "Data\\Corpus.csv")

    # 2. Chargement du corpus enrichi
    corpus = Corpus("Corpus TD6")
    corpus.load_csv("Data\\Corpus.csv")

    print("\nCorpus chargé :", corpus)

    # 3. Tests TD6
    print("\nRésultats de search('AI') :")
    print(corpus.search("AI"))

    print("\nConcordancier pour 'data' :")
    print(corpus.concorde("data", contexte=20))

    print("\nStatistiques du corpus :")
    corpus.stats(n=10)


if __name__ == "__main__":
    main()
