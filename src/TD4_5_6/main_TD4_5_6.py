from Corpus import Corpus
from Factory import DocumentFactory

def menu():
    print("\n===== MENU CORPUS =====")
    print("1. Ajouter un document")
    print("2. Afficher documents par date")
    print("3. Afficher documents par titre")
    print("4. Afficher statistiques d'un auteur")
    print("5. Sauvegarder le corpus")
    print("6. Charger le corpus")
    print("7. Rechercher un mot ou expression")
    print("8. Concordancier pour un mot ou expression")
    print("0. Quitter")

def main():
    '''
    Dans ce main, on permet à l'utilisateur d'interagir avec le corpus via un menu.
    il peut ajouter des documents, afficher des listes triées, voir les statistiques des auteurs,
    sauvegarder et charger le corpus, rechercher des mots et créer un concordancier.
    '''
    corpus = Corpus("IA Research")
    
    while True:
        menu()
        choix = input("Votre choix : ")

        if choix == "1":
            titre = input("Titre : ")
            auteur = input("Auteur : ")
            date = input("Date (YYYY-MM-DD) : ")
            url = input("URL : ")
            texte = input("Texte : ")

            corpus.add_document(titre, auteur, date, url, texte)
            print("Document ajouté avec succès.")

        elif choix == "2":
            n = int(input("Combien de documents afficher ? "))
            corpus.afficher_par_date(n)

        elif choix == "3":
            n = int(input("Combien de documents afficher ? "))
            corpus.afficher_par_titre(n)

        elif choix == "4":
            nom = input("Nom de l'auteur : ")
            if nom in corpus.authors:
                stats = corpus.authors[nom].statatistiques()
                print("\nStatistiques :")
                for k, v in stats.items():
                    print(f"{k} : {v}")
            else:
                print("Auteur non trouvé.")

        elif choix == "5":
            corpus.save_csv()
        
        elif choix == "6":
            corpus.load_csv()

        elif choix == "7":
            motif = input("Mot ou expression à rechercher : ")
            results = corpus.search(motif)
            print(f"\n{len(results)} occurrences trouvées :")
            for i, r in enumerate(results, 1):
                print(f"{i}. ...{r}...")

        elif choix == "8":
            motif = input("Mot ou expression pour le concordancier : ")
            contexte = input("Taille du contexte (nombre de caractères, défaut=30) : ")
            contexte = int(contexte) if contexte.isdigit() else 30
            df = corpus.concorde(motif, contexte)
            print(f"\nConcordancier pour '{motif}':")
            if df.empty:
                print("Aucune occurrence trouvée.")
            else:
                for _, row in df.iterrows():
                    print(f"...{row['contexte_gauche']}[{row['motif']}] {row['contexte_droit']}...")

        elif choix == "0":
            print("Fin du programme.")
            break

        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
