from ranking.utils import *


def traitement(query):
    query=preprocessing(query)
    tokens=word_tokenizer(query)
    return tokens

def filtered_documents(tokens, index, mode='ET'):
    matching_docs = []

    # Pour chaque token dans la requête
    for token in tokens:
        # Vérifier si le token est présent dans l'index
        if token in index:
            # Récupérer la liste de documents pour ce token
            docs = list(index[token].keys())
            if len(matching_docs) == 0:
                matching_docs = docs
            elif mode == 'ET':
                matching_docs=list(set(matching_docs) & set(docs))
                if matching_docs==[]:
                    break

               
            elif mode == 'OU':
                matching_docs=list(set(matching_docs) | set(docs))
    # Enlever les doublons
    filtered_docs =list(set(matching_docs))
    return filtered_docs
