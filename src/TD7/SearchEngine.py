import pandas as pd
import numpy as np
import re
from scipy.sparse import csr_matrix
from tqdm import tqdm


class SearchEngine:
    
    """
    Moteur de recherche simple basé sur le modèle TF-IDF.

    Cette classe permet d'indexer un corpus de documents et de rechercher 
    les documents les plus pertinents par rapport à une requête utilisateur.

    Attributs :
        corpus : objet corpus
            Le corpus contenant les documents à indexer.
        vocab : dict
            Dictionnaire des mots du corpus avec :
                - 'id' : identifiant unique du mot
                - 'freq' : fréquence totale du mot dans le corpus
                - 'doc_freq' : nombre de documents contenant le mot
        mat_TF : scipy.sparse.csr_matrix
            Matrice des fréquences de termes (TF) pour chaque document.
        mat_TFxIDF : scipy.sparse.csr_matrix
            Matrice TFxIDF utilisée pour mesurer la pertinence des documents.

    Méthodes :
        decouper_mots(texte)
            Nettoie et découpe un texte en mots.
        _build_vocab()
            Construit le vocabulaire unique et calcule les fréquences.
        _build_matrices()
            Construit les matrices TF et TFxIDF à partir du corpus.
        search(requete, k=5)
            Recherche les k documents les plus pertinents pour une requête.
    """

    
    def __init__(self, corpus):
        # Initialisation du moteur de recherche avec le corpus fourni
        self.corpus = corpus
        self.vocab = {}          # Dictionnaire qui contiendra les mots et leurs informations
        self.mat_TF = None       # Matrice des fréquences des termes (TF)
        self.mat_TFxIDF = None   # Matrice TF-IDF
        self._build_vocab()      # Construction du vocabulaire à partir du corpus
        self._build_matrices()   # Construction des matrices TF et TFxIDF
    
        # Conversion de la matrice TFxIDF en format sparse pour économiser de la mémoire
        self.mat_TFxIDF = self.mat_TFxIDF.tocsr()


    def decouper_mots(self, texte):
        # Nettoie et découpe un texte en mots
        texte = texte.lower()  # Passage en minuscules
        texte = re.sub(r"[^\w\s]", " ", texte)  # Suppression de la ponctuation
        return texte.split()  # Retourne la liste des mots

    def _build_vocab(self):
        # Construction du vocabulaire unique à partir du corpus
        all_mots = []
        for doc in self.corpus.id2doc.values():
            all_mots.extend(self.decouper_mots(doc.texte))  # On ajoute tous les mots de chaque document

        unique_mots = sorted(set(all_mots))  # On garde chaque mot une seule fois, trié

        # Création du dictionnaire vocab avec un ID unique pour chaque mot, et initialisation des fréquences
        self.vocab = {w: {"id": i, "freq": 0, "doc_freq": 0} for i, w in enumerate(unique_mots)}

        # Calcul des fréquences des mots et du nombre de documents où ils apparaissent
        for doc in self.corpus.id2doc.values():
            mots = self.decouper_mots(doc.texte)
            unique_doc_mots = set(mots)
            for m in mots:
                self.vocab[m]["freq"] += 1  # Fréquence totale du mot dans le corpus
            for m in unique_doc_mots:
                self.vocab[m]["doc_freq"] += 1  # Nombre de documents contenant le mot

    def _build_matrices(self):
        # Construction des matrices TF et TFxIDF
        n_docs = len(self.corpus.id2doc)  # Nombre de documents
        n_terms = len(self.vocab)          # Nombre de mots uniques
        mat = np.zeros((n_docs, n_terms))  # Matrice initialisée à zéro

        # Remplissage de la matrice TF
        for i, doc in self.corpus.id2doc.items():
            mots = self.decouper_mots(doc.texte)
            for m in mots:
                j = self.vocab[m]["id"]
                mat[i-1, j] += 1  # Incrémentation de la fréquence du mot dans le document

        self.mat_TF = csr_matrix(mat)  # Conversion en matrice sparse

        # Calcul de TFxIDF
        N = n_docs
        idf = np.log((N+1) / (np.array([self.vocab[m]["doc_freq"] for m in self.vocab]) + 1)) + 1
        self.mat_TFxIDF = self.mat_TF.multiply(idf)  # Application du facteur IDF à chaque terme

    
    def search(self, requete, k=5):
        # Transforme la requête en vecteur TF
        vecteur = np.zeros((1, len(self.vocab)))
        mots = self.decouper_mots(requete)
        for m in mots:
            if m in self.vocab:
                j = self.vocab[m]["id"]
                vecteur[0, j] += 1

        # Fonction interne pour calculer la similarité cosinus entre la requête et chaque document
        def similarite_cosinus(q_vecteur, mat):
            similarite = []
            q_vecteur = np.asarray(q_vecteur).flatten()
            q_norme = np.linalg.norm(q_vecteur)

            # Boucle sur tous les documents avec une barre de progression
            for i in tqdm(range(mat.shape[0]), desc="Calcul des similarités"):
                d_vecteur = mat.getrow(i).toarray().flatten()
                multiply = np.dot(q_vecteur, d_vecteur)
                d_norme = np.linalg.norm(d_vecteur)

                if d_norme == 0 or q_norme == 0:
                    similarite.append(0.0)  # Si vecteur nul, similarité = 0
                else:
                    similarite.append(float(multiply) / (q_norme * d_norme))  # Calcul cosinus

            return np.array(similarite)

        similarite = similarite_cosinus(vecteur, self.mat_TFxIDF)  # Calcul des similarités
        top_idx = similarite.argsort()[::-1][:k]  # Indices des k documents les plus pertinents

        # Construction du DataFrame des résultats
        resultats = []
        for idx in top_idx:
            doc = self.corpus.id2doc[idx + 1]
            resultats.append({
                "score": similarite[idx],
                "titre": doc.titre,
                "auteur": doc.auteur,
                "date": doc.date,
                "url": doc.url
            })

        return pd.DataFrame(resultats)  # Retourne les résultats sous forme de tableau
