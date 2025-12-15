# main_search.py
# importons la classe Corpus depuis TD4_5_6


import os
import sys

# Ajouter le dossier parent au sys.path pour les imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from  TD4_5_6.Corpus import Corpus
from SearchEngine import SearchEngine
import pandas as pd

def main():
    corpus = Corpus("IA Research")

    # on essaye d'ajouter quelques exemple de documents
    # On peut également charger le corpus stocker dans notre dossier data a la racine du projet
    
    corpus.add_document("AI Advances", "Alice", "2025-01-10", "http://example.com/ai1", 
                        "AI is transforming research in multiple domains.")
    corpus.add_document("Machine Learning Basics", "Bob", "2025-02-15", "http://example.com/ml1", 
                        "Machine learning allows computers to learn from data.")
    corpus.add_document("Deep Learning Trends", "Alice", "2025-03-20", "http://example.com/dl1", 
                        "Deep learning is a subset of machine learning focused on neural networks.")
    
    print("\nCorpus chargé :")
    print(corpus)

    # Initialiser le moteur
    engine = SearchEngine(corpus)
    print("\nMoteur de recherche initialisé.")

    #  Afficher le vocabulaire
    print("\nVocabulaire (mots et IDs) :")
    for mot, info in engine.vocab.items():
        print(f"{mot} -> ID: {info['id']} , \tfreq_totale: {info['freq_totale']}, \tdoc_count: {info['doc_count']}")
        print("----------------------------------------------------------------------------------------\n")

    #  Afficher la matrice TF (dense pour test)
    print("\nMatrice TF :")
    print(engine.mat_tf.todense())

    #  Afficher la matrice TFxIDF (dense pour test)
    print("\nMatrice TFxIDF :")
    print(engine.mat_tfidf.todense())

    #  Test recherche interactive
    while True:
        query = input("\nEntrez votre requête (ou 'q' pour quitter) : ")
        if query.lower() == 'q':
            break

        top_k = input("Nombre de documents à afficher ? (défaut 3) : ")
        top_k = int(top_k) if top_k.isdigit() else 3

        results = engine.search(query, top_k=top_k, use_tfidf=True)
        if results.empty:
            print("Aucun document trouvé pour cette requête.")
        else:
            print("\nRésultats :")
            print(results)

if __name__ == "__main__":
    main()
