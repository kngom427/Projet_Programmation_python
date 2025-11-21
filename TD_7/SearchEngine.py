import pandas as pd
import numpy as np
import re
from scipy.sparse import csr_matrix

class SearchEngine:
    def __init__(self, corpus):
        self.corpus = corpus
        self.vocab = {}          # dictionnaire des mots
        self.mat_TF = None       # matrice TF
        self.mat_TFxIDF = None # matrice TFxIDF
        self._build_vocab()
        self._build_matrices()
    
        # convertir 
        self.mat_TFxIDF = self.mat_TFxIDF.tocsr()


    def decouper_mots(self, texte):
        texte = texte.lower()
        texte = re.sub(r"[^\w\s]", " ", texte)
        return texte.split()

    def _build_vocab(self):
        # Construire vocabulaire avec ID unique
        all_mots = []
        for doc in self.corpus.id2doc.values():
            all_mots.extend(self.decouper_mots(doc.texte))
        unique_mots = sorted(set(all_mots))

        self.vocab = {w: {"id": i, "freq": 0, "doc_freq": 0} for i, w in enumerate(unique_mots)}

        # Calculer freq et doc_freq
        for doc in self.corpus.id2doc.values():
            mots = self.decouper_mots(doc.texte)
            unique_doc_mots = set(mots)
            for m in mots:
                self.vocab[m]["freq"] += 1
            for m in unique_doc_mots:
                self.vocab[m]["doc_freq"] += 1

    def _build_matrices(self):
        n_docs = len(self.corpus.id2doc)
        n_terms = len(self.vocab)
        mat = np.zeros((n_docs, n_terms))

        # Remplir la matrice TF
        for i, doc in self.corpus.id2doc.items():
            mots = self.decouper_mots(doc.texte)
            for m in mots:
                j = self.vocab[m]["id"]
                mat[i-1, j] += 1

        self.mat_TF = csr_matrix(mat)

        # Calcul TFxIDF
        N = n_docs
        idf = np.log((N+1) / (np.array([self.vocab[m]["doc_freq"] for m in self.vocab]) + 1)) + 1
        self.mat_TFxIDF = self.mat_TF.multiply(idf)

    def search(self, requete, k=5):
        # Transformer la requête en vecteur
        vecteur = np.zeros((1, len(self.vocab)))
        mots = self.decouper_mots(requete)
        for m in mots:
            if m in self.vocab:
                j = self.vocab[m]["id"]
                vecteur[0, j] += 1

        # Similarité cosinus
        def similarite_cosinus(q_vecteur, mat):
            similarite = []
            q_vecteur = np.asarray(q_vecteur).flatten()
            q_norme = np.linalg.norm(q_vecteur)
            for i in range(mat.shape[0]):
                d_vecteur = mat.getrow(i).toarray().flatten()  # vecteur du document
                multiply = np.dot(q_vecteur, d_vecteur)
                d_norme = np.linalg.norm(d_vecteur)
                if d_norme == 0 or q_norme == 0:
                    similarite.append(0.0)
                else:
                    similarite.append(float(multiply) / (q_norme * d_norme))
            return np.array(similarite)

        # d'utilisation
        similarite = similarite_cosinus(vecteur, self.mat_TFxIDF)
        top_idx = similarite.argsort()[::-1][:k]


        # Construire DataFrame résultats
        resultats = []

        for idx in top_idx:
            doc = self.corpus.id2doc[idx+1]
            resultats.append({
                "score": similarite[idx],
                "titre": doc.titre,
                "auteur": doc.auteur,
                "date": doc.date,
                "url": doc.url
            })

        return pd.DataFrame(resultats)
