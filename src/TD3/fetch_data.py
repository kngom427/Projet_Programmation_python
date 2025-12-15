import os
import praw
import urllib.request
import xmltodict
from urllib.parse import quote
from dotenv import load_dotenv

load_dotenv(dotenv_path="../../.env") # Charger les variables d'environnement


def clean_text(text):
    if not text:
        return ""
    return text.replace("\n", " ").strip()


# -------------------------------------------------------------------
# Fonction améliorée : client Reddit optionnel
# -------------------------------------------------------------------
def fetch_reddit_posts(theme, limit=100, reddit_client=None):
    """
    Récupère des publications Reddit contenant un mot-clé donné.

    Paramètres :
        theme (str) : mot-clé recherché
        limit (int) : nombre de posts à récupérer
        reddit_client (praw.Reddit) : client Reddit optionnel

    Fonctionnement :
        - si l'utilisateur fournit un client Reddit : on l'utilise
        - sinon : on crée un client par défaut (fallback)
    """

    #  Si aucun client n’est fourni → on crée un client local
    if reddit_client is None:
        reddit_client = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent=os.getenv("REDDIT_USER_AGENT")
        )

    docs = []

    for post in reddit_client.subreddit("all").search(theme, limit=limit):
        ''' 
        - Récupere le texte brute de chaque post (post.selftext)
        - Applique la fonction de nettoyage clean_text sur le texte brute
        - Si le texte nettoyé n'est pas vide, l'ajoute à la liste des documents
        '''
        text_clean = clean_text(post.selftext) 

        if text_clean:
            docs.append(text_clean)
            
    
    print(f"[Reddit] {len(docs)} textes récupérés.")
    return docs




# -------------------------------------------------------------------
# FONCTION : Récupération des résumés d’articles Arxiv
# -------------------------------------------------------------------
def fetch_arxiv_summaries(theme, max_results=20):
    """
    Récupère les résumés d’articles scientifiques liés à un thème via l’API Arxiv.

    Arguments :
        theme (str)       : mot-clé de recherche
        max_results (int) : nombre maximum de résumés retournés

    Retour :
        docs (list)   : résumés nettoyés
    """

    encoded_theme = quote(theme)

    # Construction de l'URL pour l'appel API
    url = (
        f"http://export.arxiv.org/api/query?"
        f"search_query=all:{encoded_theme}&start=0&max_results={max_results}"
    )

    # Récupération du XML brut depuis Arxiv
    xml_data = urllib.request.urlopen(url).read()
    parsed_data = xmltodict.parse(xml_data)

    docs = []

    # Les articles sont dans feed -> entry
    entries = parsed_data["feed"].get("entry", [])

    # Si Arxiv renvoie un seul article, "entry" est un dict → on le convertit en liste
    if isinstance(entries, dict):
        entries = [entries]

    # Extraction des résumés
    for entry in entries:
        ''' 
        - Récupere le texte brute de chaque post (entry.get("summary", ""))
        - Applique la fonction de nettoyage clean_text sur le texte brute
        - Si le texte nettoyé n'est pas vide, l'ajoute à la liste des documents
        '''
        summary_raw = entry.get("summary", "")
        summary = clean_text(summary_raw)

        if summary:
            docs.append(summary)

    print(f"[Arxiv] {len(docs)} résumés récupérés pour le thème : '{theme}'.")
    return docs
