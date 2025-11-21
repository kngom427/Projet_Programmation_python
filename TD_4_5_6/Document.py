from datetime import datetime

class Document:
    def __init__(self, titre, auteur, date, url, texte):
        self.titre = titre
        self.auteur = auteur
        self.url = url
        self.texte = texte

        if isinstance(date, str):
            try:
                self.date = datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                self.date = date
        else:
            self.date = date

        self.type = "Document"

    def method_1(self):
        print(f"Titre: {self.titre}\nAuteur: {self.auteur}\nDate: {self.date}\nURL: {self.url}\nTexte: {self.texte[:150]}...")

    def __str__(self):
        return f"{self.type}: {self.titre}"


#  TD5 : Héritage 
class RedditDocument(Document):
    def __init__(self, titre, auteur, date, url, texte, nb_commentaires):
        super().__init__(titre, auteur, date, url, texte)
        self.nb_commentaires = nb_commentaires
        self.type = "Reddit"

    def getType(self):
        return self.type

    def __str__(self):
        return f"[Reddit] {self.titre} ({self.nb_commentaires} commentaires)"


class ArxivDocument(Document):
    def __init__(self, titre, auteurs, date, url, texte):
        auteur_principal = auteurs[0] if auteurs else "Inconnu"
        super().__init__(titre, auteur_principal, date, url, texte)
        self.co_auteurs = auteurs
        self.type = "Arxiv"

    def getType(self):
        return self.type

    def __str__(self):
        return f"[Arxiv] {self.titre} | Co-auteurs: {', '.join(self.co_auteurs)}"