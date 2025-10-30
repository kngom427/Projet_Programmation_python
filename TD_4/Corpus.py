import pandas as pd
from TD_4.Document import Document
from TD_4.Author import Author

class Corpus:
    def __init__(self, nom):
        self.nom = nom
        # nom de l'auteur
        self.authors = {} 
        # id_doc   
        self.id2doc = {}
        # nombre total de documents    
        self.ndoc = 0  
        # nombre total d'auteurs      
        self.naut = 0  

     # Ajouter un document au corpus 
    def add_document(self, titre, auteur_nom, date, url, texte):

        # Ajoute un document et met à jour les auteurs
        self.ndoc += 1
        id_doc = self.ndoc  

        # Créer un document
        doc = Document(titre, auteur_nom, date, url, texte)
        self.id2doc[id_doc] = doc  

        # Gérer l'auteur
        if auteur_nom not in self.authors:
            self.authors[auteur_nom] = Author(auteur_nom)
            self.naut += 1  
        
        # Ajouter le document à la production de l'auteur
        self.authors[auteur_nom].add(id_doc, doc)

        # Afficher les documents triés par date 
    def afficher_par_date(self, n=10):
        # Affiche les n documents les plus récents
        print(f"\n--- {n} documents les plus récents du corpus '{self.nom}' ---")
        docs_tries = sorted(self.id2doc.values(), key=lambda d: d.date, reverse=True)
        for doc in docs_tries[:n]:
            print(f"{doc.date} - {doc.titre} ({doc.auteur})")

    # Afficher les documents triés par titre 
    def afficher_par_titre(self, n=5):
        # Affiche les n premiers documents triés par titre
        print(f"\n--- {n} documents triés par titre du corpus '{self.nom}' ---")
        docs_tries = sorted(self.id2doc.values(), key=lambda d: d.titre)
        for doc in docs_tries[:n]:
            print(f"{doc.titre} ({doc.auteur}, {doc.date})")

    # Représentation digeste du corpus 
    def __repr__(self):
        return (f"Corpus '{self.nom}' : {self.ndoc} documents, {self.naut} auteurs.\n"
                f"Auteurs : {', '.join(list(self.authors.keys()))}")
    

    # Sauvegarde au format CSV via DataFrame 
    def save_csv(self, filename="Data\\Corpus_1.csv"):
        #Sauvegarde les métadonnées du corpus dans un fichier CSV
        data = [{
            "id": i,
            "titre": doc.titre,
            "auteur": doc.auteur,
            "date": doc.date,
            "url": doc.url,
            "texte": doc.texte
        } for i, doc in self.id2doc.items()]

        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(f"Corpus sauvegardé dans le fichier : {filename}")

    # Chargement depuis un CSV 
    def load_csv(self, filename="Data\\Corpus_1.csv"):
        # Charge le corpus depuis un fichier CSV
        df = pd.read_csv(filename)
        for _, row in df.iterrows():
            self.add_document(row["titre"], row["auteur"], row["date"], row["url"], row["texte"])
        print(f"Corpus chargé depuis : {filename}")

     