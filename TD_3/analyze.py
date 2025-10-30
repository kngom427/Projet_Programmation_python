from TD_3.corpus import *

def analyser_corpus(df_corpus):
    df_corpus = charger_corpus()
    # Le nombre de documents
    len(df_corpus)

    # Pour chaque document, 
    # affichez le nombre de mots et de phrases
    
    for i, texte in enumerate(df_corpus["Texte"], start=1):
        # mots séparés par des espaces
        nb_mots = len(texte.split())
        # phrases séparées par des points          
        nb_phrases = len(texte.split('.'))     
        print(f"Document {i} : {nb_mots} mots, {nb_phrases} phrases")

    # Supprimez de notre corpus les documents trop petits,
    # ici qui contiennent moins de 20 caractéres
    taille_initiale = len(df_corpus)
    print("Taille initiale:",taille_initiale)
    df_corpus = df_corpus[df_corpus["Texte"].str.len() >= 20].reset_index(drop=True)
    taille_finale = len(df_corpus)
    print(f"Documents supprimés : {taille_initiale - taille_finale}")
    print(f"Taille du corpus après nettoyage : {taille_finale} documents")

    # Fusionner tous les textes en une seule chaîne géante
    chaine_corpus = " ".join(df_corpus["Texte"].tolist())
    print("Exemple chaîne géante:",chaine_corpus[:100])
    return 

