import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(__file__))  # Ajoute le dossier courant pour les imports relatifs

from Document import Document
from Author import Author
import re

class Corpus:
    """
    Représente un corpus de documents avec gestion des auteurs et statistiques textuelles.

    Cette classe suit le pattern Singleton : un seul objet Corpus peut exister à la fois.

    Attributs :
        nom : str
            Nom du corpus.
        authors : dict
            Dictionnaire des auteurs, clé = nom de l'auteur, valeur = objet Author.
        id2doc : dict
            Dictionnaire des documents, clé = ID, valeur = objet Document.
        ndoc : int
            Nombre total de documents.
        naut : int
            Nombre total d'auteurs.
        _full_text : str
            Concaténation de tous les textes du corpus, utilisée pour les recherches.
    
    Méthodes :
        add_document(titre, auteur_nom, date, url, texte)
            Ajoute un document au corpus et crée l'auteur si nécessaire.
        afficher_par_date(n=5)
            Affiche les n documents les plus récents.
        afficher_par_titre(n=5)
            Affiche les n documents triés par titre.
        save_csv(filename)
            Sauvegarde le corpus dans un fichier CSV.
        load_csv(filename)
            Charge les documents depuis un CSV.
        _build_full_text()
            Construit une chaîne unique contenant tous les textes du corpus.
        search(motif)
            Retourne les passages contenant un motif donné.
        concorde(motif, contexte=30)
            Construit un concordancier pour un motif avec contexte gauche/droit.
        nettoyer_texte(texte)
            Nettoie un texte (minuscules, suppression chiffres et ponctuation).
        stats(n=10)
            Affiche des statistiques sur les mots du corpus.
    """

    _instance = None  # Pour le Singleton

    def __new__(cls, nom):
        # Singleton : crée une seule instance du corpus
        if cls._instance is None:
            cls._instance = super(Corpus, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, nom):
        if self._initialized:
            return  # Evite la réinitialisation
        self.nom = nom
        self.authors = {}
        self.id2doc = {}
        self.ndoc = 0
        self.naut = 0
        self._initialized = True
        self._full_text = None  # Texte concaténé pour recherche

        print(f" Corpus '{self.nom}' créé (Singleton).")

    def add_document(self, titre, auteur_nom, date, url, texte):
        # Ajoute un document au corpus et crée un auteur si nécessaire
        self.ndoc += 1
        id_doc = self.ndoc
        doc = Document(titre, auteur_nom, date, url, texte)
        self.id2doc[id_doc] = doc

        if auteur_nom not in self.authors:
            self.authors[auteur_nom] = Author(auteur_nom)
            self.naut += 1
        self.authors[auteur_nom].add(id_doc, doc)

    def afficher_par_date(self, n=5):
        # Affiche les n documents les plus récents
        docs = sorted(self.id2doc.values(), key=lambda d: d.date, reverse=True)
        print(f"\n--- {n} documents récents ---")
        for doc in docs[:n]:
            print(f"{doc.date} - {doc.titre} ({doc.auteur})")

    def afficher_par_titre(self, n=5):
        # Affiche les n documents triés par titre
        docs = sorted(self.id2doc.values(), key=lambda d: d.titre)
        print(f"\n--- {n} documents triés par titre ---")
        for doc in docs[:n]:
            print(f"{doc.titre} ({doc.auteur})")

    def __repr__(self):
        # Représentation concise du corpus
        return f"Corpus '{self.nom}' : {self.ndoc} docs, {self.naut} auteurs."

    def save_csv(self, filename="../../data/corpus.csv"):
        # Sauvegarde tous les documents dans un CSV
        data = [{"id": i, "titre": d.titre, "auteur": d.auteur, "date": d.date, "url": d.url, "texte": d.texte}
                for i, d in self.id2doc.items()]
        pd.DataFrame(data).to_csv(filename, index=False)
        print(f" Corpus sauvegardé dans {filename}")

    def load_csv(self, filename="../../data/corpus.csv"):
        # Charge les documents depuis un CSV et les ajoute au corpus
        df = pd.read_csv(filename)
        for _, row in df.iterrows():
            self.add_document(row["titre"], row["auteur"], row["date"], row["url"], row["texte"])
        print(f" Corpus chargé depuis {filename}")

    # TD 6

    def _build_full_text(self):
        # Construit une seule fois la concaténation de tous les textes pour recherche
        if self._full_text is None:
            self._full_text = " ".join([doc.texte for doc in self.id2doc.values()])
        return self._full_text
    
    def search(self, motif):
        # Retourne tous les passages contenant le motif (avec un peu de contexte)
        texte = self._build_full_text()
        results = re.findall(rf".{{0,30}}{motif}.{{0,30}}", texte, flags=re.IGNORECASE)
        return results
    
    def concorde(self, motif, contexte=30):
        # Construit un concordancier : extrait contexte gauche/droit autour de chaque occurrence
        texte = self._build_full_text()
        matches = re.finditer(rf"{motif}", texte, flags=re.IGNORECASE)

        data = []
        for m in matches:
            start, end = m.span()
            gauche = texte[max(0, start - contexte):start]
            droit = texte[end:end + contexte]
            data.append({"contexte_gauche": gauche, "motif": m.group(), "contexte_droit": droit})

        df = pd.DataFrame(data)
        return df
    
    def nettoyer_texte(self, texte):
        # Nettoie un texte : minuscules, suppression chiffres et ponctuation
        texte = texte.lower()
        texte = texte.replace("\n", " ")
        texte = re.sub(r"[0-9]", " ", texte)
        texte = re.sub(r"[^\w\s]", " ", texte)
        return texte
    
    def stats(self, n=10):
        # Génère des statistiques sur les mots : fréquence et fréquence par document
        vocab = {}
        doc_freq = {}

        for doc in self.id2doc.values():
            texte = self.nettoyer_texte(doc.texte)
            mots = re.split(r"\s+", texte.strip())

            # Comptage des occurrences
            for mot in mots:
                if mot:
                    vocab[mot] = vocab.get(mot, 0) + 1

            # Comptage document frequency
            unique_mots = set(mots)
            for mot in unique_mots:
                doc_freq[mot] = doc_freq.get(mot, 0) + 1

        # Création du DataFrame
        df = pd.DataFrame({
            "mot": list(vocab.keys()),
            "freq": list(vocab.values()),
            "doc_freq": [doc_freq[m] for m in vocab.keys()]
        })

        df_sorted = df.sort_values(by="freq", ascending=False)

        print(f"Nombre de mots différents : {len(vocab)}")
        print(f"{n} mots les plus fréquents :")
        print(df_sorted.head(n))

        return df_sorted
