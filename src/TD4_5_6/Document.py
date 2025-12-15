from datetime import datetime

class Document:
    """
    Représente un document générique.

    Attributs :
        titre : str
            Le titre du document.
        auteur : str
            Nom de l'auteur principal.
        date : datetime ou str
            Date du document. Si fourni en chaîne, tentative de conversion en datetime.
        url : str
            Lien vers le document.
        texte : str
            Contenu textuel du document.

    Méthodes :
        afficher_document()
            Affiche les informations principales du document avec un aperçu du texte.
        __str__()
            Retourne une représentation simple du document.
    """

    def __init__(self, titre, auteur, date, url, texte):
        self.titre = titre
        self.auteur = auteur
        self.url = url
        self.texte = texte

        # Conversion de la date si c'est une chaîne de caractères
        if isinstance(date, str):
            try:
                self.date = datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                # Si le format n'est pas reconnu, on garde la chaîne brute
                self.date = date
        else:
            self.date = date

    def afficher_document(self):
        # Affiche les informations essentielles du document et un extrait du texte
        print(f"Titre: {self.titre}\nAuteur: {self.auteur}\nDate: {self.date}\nURL: {self.url}\nTexte: {self.texte[:150]}...")

    def __str__(self):
        # Représentation textuelle simple
        return f"Document: {self.titre}"


# TD5 : Héritage

class RedditDocument(Document):
    """
    Document provenant de Reddit.

    Attributs supplémentaires :
        nb_commentaires : int
            Nombre de commentaires sur le post Reddit.
    """

    def __init__(self, titre, auteur, date, url, texte, nb_commentaires):
        super().__init__(titre, auteur, date, url, texte)
        self.nb_commentaires = nb_commentaires

    def __str__(self):
        # Affiche le titre avec le nombre de commentaires
        return f"[Reddit] {self.titre} ({self.nb_commentaires} commentaires)"


class ArxivDocument(Document):
    """
    Document provenant d'Arxiv.

    Attributs supplémentaires :
        co_auteurs : list
            Liste des co-auteurs du document.
    """

    def __init__(self, titre, auteurs, date, url, texte):
        # L'auteur principal est le premier de la liste, sinon "Inconnu"
        auteur_principal = auteurs[0] if auteurs else "Inconnu"
        super().__init__(titre, auteur_principal, date, url, texte)
        self.co_auteurs = auteurs

    def __str__(self):
        # Affiche le titre avec la liste des co-auteurs
        return f"[Arxiv] {self.titre} | Co-auteurs: {', '.join(self.co_auteurs)}"
