import praw
import urllib.request
import xmltodict

"""
    Récupère des publications Reddit liées à un thème donné.
    Retourne deux listes : docs_reddit et source_reddit.
"""

def reddit(theme):
    reddit = praw.Reddit(client_id='zT-FEkVC9uFaEsCGIsCb8Q', 
            client_secret='BOLjNsbMN2tH9qXcl0jZPK7k4Ykp1Q',
              user_agent='Projet')
    
    docs_reddit = []
    source_reddit = []

    # Rechercher les publications sur le thème
    for post in reddit.subreddit("all").search(theme, limit=100):
        # Les champs disponibles 
        #print(dir(post))
        # Le champ selftext contient le contenu textuel
        text = post.selftext
         # on vérifie qu’il y a du texte
        if text and text.strip():
             # Débarrassons des sauts de ligne (\n) 
             # en les remplaçant par des espaces
            text_nettoye = text.replace("\n", " ")
            # Ajoutons le texte et la source
            docs_reddit.append(text_nettoye)
            source_reddit.append("reddit")
    print("Le nombre de docs_reddit:",len(docs_reddit))
  
    return docs_reddit, source_reddit


"""
    fonction pour Récupérer des résumés d'articles scientifiques 
    Arxiv liés à un thème donné. Retourne deux listes : 
    docs_arxiv et source_arxiv

"""

def arxiv(theme):
     # Construire l'URL de la requête (avec le thème choisi)
    url = f"http://export.arxiv.org/api/query?search_query=all:{theme}&start=0&max_results=10"
    data = urllib.request.urlopen(url).read()
    # Conversion xml en dictionnaire pyhon
    parser = xmltodict.parse(data)

    docs_arxiv = []
    source_arxiv = []

    #Chaque entry correspond à un article scientiphique
    parser['feed']['entry'][0].keys()
    #le champ contenant le contenu textuel est summary
    # Extraire les résumés 
    entry = parser['feed']['entry']
    for entry in entry:
        text = entry.get('summary', '')
        text_nett = text.replace("\n", " ")
        docs_arxiv.append(text_nett)
        source_arxiv.append("arxiv")

    print("Le nombre de docs_arxiv:",len(docs_arxiv))

    return docs_arxiv, source_arxiv
