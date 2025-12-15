import pytest
from TD4_5_6.Corpus import Corpus

# -------------------------------------------------------------
# Fixture pytest pour créer un corpus propre pour chaque test
# Source  : https://docs.pytest.org/en/stable/explanation/fixtures.html
# -------------------------------------------------------------
@pytest.fixture
def corpus():
    """
    Fixture pytest :
    Cette fonction est exécutée avant chaque test.
    Elle crée un nouvel objet Corpus, garantissant que chaque test
    commence avec un corpus vide et indépendant.
    """
    return Corpus("Test Corpus")

# -------------------------------------------------------------
# Test 1 : ajout d'un document au corpus
# -------------------------------------------------------------
def test_add_document(corpus):
    """
    Vérifie que l'ajout d'un document fonctionne correctement.
    On teste :
    - L'incrémentation du nombre de documents (ndoc)
    - La création correcte de l'auteur si celui-ci n'existait pas
    - L'incrémentation du nombre d'auteurs (naut)
    """
    corpus.add_document(
        titre="Test IA",
        auteur_nom="Saliou",
        date="2024-01-01",
        url="http://test.com",
        texte="Contenu du document"
    )

    # Vérifie qu'un document a bien été ajouté
    assert corpus.ndoc == 1
    # Vérifie que l'auteur a été créé et ajouté au dictionnaire
    assert "Saliou" in corpus.authors
    # Vérifie que le nombre d'auteurs est correct
    assert corpus.naut == 1

# -------------------------------------------------------------
# Test 2 : lien entre l'auteur et ses documents
# -------------------------------------------------------------
def test_author_document_link(corpus):
    """
    Vérifie que le document ajouté est correctement lié à l'auteur.
    On teste :
    - Le nombre de documents de l'auteur (ndoc)
    - Que la production de l'auteur contient bien le document ajouté
    """
    corpus.add_document(
        "Doc 1",
        "Mr Thiam",
        "2024-02-02",
        "http://exemple.com",
        "Texte exemple"
    )

    author = corpus.authors["Mr Thiam"]
    # L'auteur doit avoir exactement 1 document
    assert author.ndoc == 1
    # La liste des documents de l'auteur doit contenir le document ajouté
    assert len(author.production) == 1

# -------------------------------------------------------------
# Test 3 : statistiques d'un auteur
# -------------------------------------------------------------
def test_author_statistics(corpus):
    """
    Vérifie que la méthode de statistiques de l'auteur fonctionne.
    On teste :
    - Le nombre total de documents de l'auteur
    - La taille moyenne des documents
    """
    # Ajout de deux documents pour le même auteur
    corpus.add_document(
        "Doc 1",
        "Khadim",
        "2024-03-03",
        "url1",
        "aaaa"
    )
    corpus.add_document(
        "Doc 2",
        "Khadim",
        "2024-03-04",
        "url2",
        "bbbbbbbb"
    )

    stats = corpus.authors["Khadim"].statatistiques()

    # Vérifie que le nombre de documents est correct
    assert stats["Nombre de documents"] == 2
    # Vérifie que la taille moyenne des documents est correcte
    assert stats["Taille moyenne des documents"] == (4 + 8) / 2

# -------------------------------------------------------------
# Test 4 : vérification du pattern Singleton pour Corpus
# -------------------------------------------------------------
def test_singleton_corpus():
    """
    Vérifie que la classe Corpus respecte le pattern Singleton.
    Cela signifie que plusieurs instanciations de Corpus doivent
    renvoyer la même instance.
    """
    c1 = Corpus("Corpus 1")
    c2 = Corpus("Corpus 2")

    # Les deux instances doivent être identiques
    assert c1 is c2
