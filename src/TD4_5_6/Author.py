class Author:
    '''
    Classe représentant un auteur avec ses documents.
    Attributs :
      - name : nom de l'auteur
      - ndoc : nombre de documents produits
      - production : dictionnaire des documents produits (id_doc -> Document)
    Méthodes :
        - add : ajoute un document à la production de l'auteur
        - __str__ : représentation textuelle de l'auteur
    '''
    
    def __init__(self, name):
        self.name = name
        self.ndoc = 0
        self.production = {}

    def add(self, id_doc, document):
        self.production[id_doc] = document
        self.ndoc += 1

    def __str__(self):
        return f"Auteur : {self.name} | Nombre de documents : {self.ndoc}"
        
    def statatistiques(self):
        '''
        Cette affiche quelques statistiques sur les documents de l auteur.
        Par exemple : Nombre de documents produits et taille moyenne des documents, etc 
        '''
        production_totale = sum(len(doc.texte) for doc in self.production.values())
        taille_moyenne = production_totale / self.ndoc if self.ndoc > 0 else 0
        
        return {   "Auteur": self.name,
            "Nombre de documents": self.ndoc,
            "Taille moyenne des documents": taille_moyenne
        }
    