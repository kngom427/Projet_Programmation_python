from Document import RedditDocument, ArxivDocument

class DocumentFactory:
    @staticmethod
    def create_document(source, **kwargs):
        if source.lower() == "reddit":
            return RedditDocument(**kwargs)
        elif source.lower() == "arxiv":
            return ArxivDocument(**kwargs)
        else:
            raise ValueError("Type de document inconnu.")