from Document import RedditDocument, ArxivDocument

class DocumentFactory:
    
    ''' 
    Factory pour créer des documents selon leur source
    indépendamment des classes concrètes.
    '''
    
    @staticmethod
    def create_document(source, **kwargs):
        ''' Cette methode est statique et crée des documents en fonction de la source fournie.
            On a donc pas besoin d'instancier la factory pour l'utiliser.
        '''
        if source.lower() == "reddit":
            return RedditDocument(**kwargs)
        elif source.lower() == "arxiv":
            return ArxivDocument(**kwargs)
        else:
            raise ValueError("Type de document inconnu.")