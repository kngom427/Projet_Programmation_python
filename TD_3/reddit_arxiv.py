import praw
import urllib.request
import xmltodict

"""
    Récupère des publications Reddit liées à un thème donné.
    Retourne deux listes : docs_reddit et source_reddit.
"""

def reddit(theme,limit=100):
    reddit = praw.Reddit(client_id='zT-FEkVC9uFaEsCGIsCb8Q', 
            client_secret='BOLjNsbMN2tH9qXcl0jZPK7k4Ykp1Q',
              user_agent='Projet')
    
    docs_reddit, sources_reddit = [], []

    for post in reddit.subreddit("all").search(theme, limit=limit):
        text = post.selftext.strip()
        if text:
            text_nettoye = text.replace("\n", " ")
            docs_reddit.append(text_nettoye)
            sources_reddit.append("reddit")

    print(f"{len(docs_reddit)} publications Reddit récupérées.")
    return docs_reddit, sources_reddit


"""
    fonction pour Récupérer des résumés d'articles scientifiques 
    Arxiv liés à un thème donné. Retourne deux listes : 
    docs_arxiv et source_arxiv

"""

def arxiv(theme, max_results=20):
    from urllib.parse import quote
    encoded_theme = quote(theme)  # encodage du thème
    url = f"http://export.arxiv.org/api/query?search_query=all:{encoded_theme}&start=0&max_results={max_results}"
    data = urllib.request.urlopen(url).read()
    parser = xmltodict.parse(data)
   
    docs_arxiv, sources_arxiv = [], []
    entries = parser["feed"].get("entry", [])

    # Si un seul article, le transformer en liste
    if isinstance(entries, dict):
        entries = [entries]

    for entry in entries:
        text = entry.get("summary", "").replace("\n", " ").strip()
        if text:
            docs_arxiv.append(text)
            sources_arxiv.append("arxiv")

    print(f"{len(docs_arxiv)} articles Arxiv récupérés.")
    return docs_arxiv, sources_arxiv
