from datetime import datetime

class Document:
    """
    Classe représentant un document textuel avec ses métadonnées

    """
    # Constructeur
    def __init__(self, titre, auteur, date, url, texte):
        self.titre = titre
        self.auteur = auteur
        self.url = url
        self.texte = texte

        # Si la date est une chaîne, 
        # on tente de la convertir en datetime
        if isinstance(date, str):
            try:
                self.date = datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                # Si le format ne correspond pas, 
                # on garde la chaîne brute
                self.date = date
        else:
            self.date = date

    # Affiche toutes les informations du document
    def method_1(self):
        print(f"Titre: {self.titre}")
        print(f"Auteur: {self.auteur}")
        print(f"date: {self.date}")
        print(f"url: {self.url}")
        # afficher les 150 premiers caractères
        print(f"texte: {self.texte[:150]}...")
     

    # Représentation simplifiée du document
    def __str__(self):
        return f"Document: {self.titre}"
    

      