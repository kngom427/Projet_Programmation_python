# main.py
from corpus_builder import construire_corpus, charger_corpus, analyser_corpus

def main():
    theme = "Artificial Intelligence"  # Thématique choisie
    print(f"\n Construction du corpus sur le thème : {theme}\n")

    # Étape 1 : construire le corpus et le sauvegarder
    construire_corpus(theme)

    # Étape 2 : charger le corpus sauvegardé
    df = charger_corpus()

    # Étape 3 : analyser le corpus
    analyser_corpus(df)


if __name__ == "__main__":
    main()
