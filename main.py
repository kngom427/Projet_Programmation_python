from TD_4.Corpus import Corpus
from TD_4.Document import Document
import pandas as pd
from datetime import datetime
def main():


    # === Chargement du DataFrame ===
    df = pd.read_csv("Data\\corpus.csv", sep="\t", encoding="utf-8")  

    # === Création du corpus ===
    corpus_1 = Corpus("Corpus_td4")

    # === Ajout des documents dans le corpus ===
    for i, row in df.iterrows():
        titre = row.get("title", "Sans titre")
        auteur = row.get("author", "Anonyme")
        date_str = row.get("date", "2025-01-01")

        try:
            date = datetime.strptime(str(date_str), "%Y-%m-%d")
        except ValueError:
            date = datetime.now()

        url = row.get("url", "")
        texte = row.get("texte", "")

        corpus_1.add_document(titre, auteur, date, url, texte)

    # === Affichage résumé ===
    print("\n=== Corpus créé avec succès ===")
    print(corpus_1)

    print("\n--- Documents triés par date ---")
    corpus_1.afficher_par_date(3)

    print("\n--- Documents triés par titre ---")
    corpus_1.afficher_par_titre(3)



    # Sauvegarde
    corpus_1.save_csv("Data\\Corpus_td4.csv")

    # Rechargement dans un nouveau corpus
    corpus_test = Corpus("Test Rechargement")
    corpus_test.load_csv("Data\\corpus_td4.csv")
    print(corpus_test)

   

  

if __name__ == "__main__":
    main()

