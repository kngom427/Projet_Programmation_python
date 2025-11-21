import pandas as pd
from TD_4_5_6.Document import Document
from TD_4_5_6.Author import Author
import re


class Corpus:
    _instance = None  # Singleton

    def __new__(cls, nom):
        if cls._instance is None:
            cls._instance = super(Corpus, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, nom):
        if self._initialized:
            return  # éviter de réinitialiser
        self.nom = nom
        self.authors = {}
        self.id2doc = {}
        self.ndoc = 0
        self.naut = 0
        self._initialized = True
        self._full_text = None  # concaténation des textes 
        print(f" Corpus '{self.nom}' créé (Singleton).")

    def add_document(self, titre, auteur_nom, date, url, texte):
        self.ndoc += 1
        id_doc = self.ndoc
        doc = Document(titre, auteur_nom, date, url, texte)
        self.id2doc[id_doc] = doc

        if auteur_nom not in self.authors:
            self.authors[auteur_nom] = Author(auteur_nom)
            self.naut += 1
        self.authors[auteur_nom].add(id_doc, doc)

    def afficher_par_date(self, n=5):
        docs = sorted(self.id2doc.values(), key=lambda d: d.date, reverse=True)
        print(f"\n--- {n} documents récents ---")
        for doc in docs[:n]:
            print(f"{doc.date} - {doc.titre} ({doc.auteur})")

    def afficher_par_titre(self, n=5):
        docs = sorted(self.id2doc.values(), key=lambda d: d.titre)
        print(f"\n--- {n} documents triés par titre ---")
        for doc in docs[:n]:
            print(f"{doc.titre} ({doc.auteur})")

    def __repr__(self):
        return f"Corpus '{self.nom}' : {self.ndoc} docs, {self.naut} auteurs."

    def save_csv(self, filename="Data\\Corpus.csv"):
        data = [{"id": i, "titre": d.titre, "auteur": d.auteur, "date": d.date, "url": d.url, "texte": d.texte}
                for i, d in self.id2doc.items()]
        pd.DataFrame(data).to_csv(filename, sep="\t", index=False, encoding="utf-8")
        print(f" Corpus sauvegardé dans {filename}")

    def load_csv(self, filename="Data\\Corpus.csv"):
        df = pd.read_csv(filename, sep="\t", encoding="utf-8")
        for _, row in df.iterrows():
            self.add_document(row["titre"], row["auteur"], row["date"], row["url"], row["texte"])
        print(f" Corpus chargé depuis {filename}")

    
    # TD 6

    def _build_full_text(self):
        #Construit une seule fois la concaténation des textes du corpus
        if self._full_text is None:
            self._full_text = " ".join([doc.texte for doc in self.id2doc.values()])
        return self._full_text
    
    def search(self, motif):
        #Retourne les passages contenant le mot-clé AI
        texte = self._build_full_text()
        results = re.findall(rf".{{0,30}}{motif}.{{0,30}}", texte, flags=re.IGNORECASE)
        return results
    

    def concorde(self, motif, contexte=30):
        #Construit un concordancier pour une expression donnée
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
        #Nettoie un texte brut
        texte = texte.lower()
        texte = texte.replace("\n", " ")
        texte = re.sub(r"[0-9]", " ", texte)  # supprimer les chiffres
        texte = re.sub(r"[^\w\s]", " ", texte)  # supprimer les  ponctuations
        return texte
        

    
    def stats(self, n=10):
        # Afficher des statistiques textuelles sur le corpus
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




