import praw


from fetch_data import (
    fetch_reddit_posts,
    fetch_arxiv_summaries
)
from corpus_builder import construire_corpus, charger_corpus, analyser_corpus
import os
from dotenv import load_dotenv

'''
Ce fichier main nous pertmet de tester
- l'acquisition des données
- la construction du corpus
- l'analyse du corpus
- le sauvegarde du corpus
'''
def main():

    # Charger les variables d'environnement
    load_dotenv(dotenv_path="../../.env")

    print("=== TD3 : Acquisition des Données (Partie 1) ===\n")

    # 1️ Choix du thème
    theme = input("Entrez le thème à rechercher : ").strip()
    print(f"\nRecherche des documents pour le thème : '{theme}'\n")

    # 2️ Création d'un client Reddit (une seule fois pour optimiser)
    reddit_client = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )

    # 3️ Récupération des données
    docs_reddit = fetch_reddit_posts(theme, limit=30, reddit_client=reddit_client)
    docs_arxiv = fetch_arxiv_summaries(theme, max_results=20)

    # 4️ Compter et afficher les résultats
    total = len(docs_reddit) + len(docs_arxiv)

    print("\n=== Résultats ===")
    print(f" Publications Reddit récupérées : {len(docs_reddit)}")
    print(f" Articles Arxiv récupérés      : {len(docs_arxiv)}")
    print(f"==> Total documents récupérés     : {total}\n")
    print(f"Un exemple de document Reddit :\n{docs_reddit[0] if docs_reddit else 'Aucun document Reddit trouvé.'}\n")

    print(" Fin de la partie 1 : acquisition terminée.")
    print("Vous pourrez verifier corpus sauvegarder dans le dossier data/ à la racine du projet.")
    
    df = construire_corpus(theme, reddit_client=reddit_client)
    df_clean, chaine = analyser_corpus(df)
    
    
    


if __name__ == "__main__":
    main()
