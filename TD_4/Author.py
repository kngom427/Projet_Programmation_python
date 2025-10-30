class Author:
    def __init__(self, name):
        self.name = name 
        # Nombre de documents publiés              
        self.ndoc = 0  
        # Dictionnaire des documents de l’auteur             
        self.production = {}

    # Méthode add
    def add(self, id_doc, document):
        # Ajoute un document à la production de l'auteur
        self.production[id_doc] = document
        self.ndoc += 1

    
    def __str__(self):
        return f"Auteur : {self.name} | Nombre de documents : {self.ndoc}"
    
    