import pandas as pd
from unittest.mock import patch
from TD3.corpus_builder import construire_corpus
import os


def test_construire_corpus(tmp_path):
    """
    Test complet de la construction du corpus :
    - Mock des fonctions d'acquisition
    - Vérification du DataFrame
    - Vérification des colonnes
    - Vérification du fichier généré
    """

    # Données simulées
    fake_reddit_docs = ["Texte reddit 1", "Texte reddit 2"]
    fake_arxiv_docs = ["Texte arxiv 1"]

    # Patch des fonctions fetch
    with patch("TD3.corpus_builder.fetch_reddit_posts", return_value=fake_reddit_docs):
        with patch("TD3.corpus_builder.fetch_arxiv_summaries", return_value=fake_arxiv_docs):

            # Chemin du fichier pour le test
            save_path = tmp_path / "corpus.csv"

            # Exécution de la fonction
            df = construire_corpus("IA", save_path=str(save_path))

            # Vérifications du DataFrame
            assert len(df) == 3
            assert "Texte" in df.columns
            assert "Source" in df.columns

            assert list(df["Texte"]) == [
                "Texte reddit 1",
                "Texte reddit 2",
                "Texte arxiv 1"
            ]

            assert list(df["Source"]) == ["reddit", "reddit", "arxiv"]

            # Vérifions que le fichier a été créé
            assert save_path.exists(), "Le fichier TSV doit être créé"
