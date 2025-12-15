import pytest


from TD3.fetch_data import clean_text

def test_clean_text_basic():
    """
    Test de base : vérifier que les retours à la ligne sont correctement remplacés par un espace.
    """
    assert clean_text("Hello\nWorld") == "Hello World"


def test_clean_text_strip_spaces():
    """
    Vérifie que la fonction supprime bien les espaces inutiles autour du texte.
    """
    assert clean_text("   Salut le monde   ") == "Salut le monde"


def test_clean_text_none():
    """
    Vérifie que la fonction ne plante pas quand elle reçoit None,
    et qu'elle renvoie simplement une chaîne vide (comportement attendu).
    """
    assert clean_text(None) == ""
