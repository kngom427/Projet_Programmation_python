class Author:
    def __init__(self, name):
        self.name = name
        self.ndoc = 0
        self.production = {}

    def add(self, id_doc, document):
        self.production[id_doc] = document
        self.ndoc += 1

    def __str__(self):
        return f"Auteur : {self.name} | Nombre de documents : {self.ndoc}"
    