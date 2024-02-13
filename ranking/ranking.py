from nltk.corpus import stopwords
def calculate_score_occurances(tokens, index, documents):
    #importance sur le compte des tokens dans les documents
    scores = {}
    sorted_documents={}
    # Pour chaque document
    for document in documents:
        score = 0
        
        # Pour chaque token
        for token in tokens:
            # Si le token est présent dans le document
            if token in index and document in index[token]:
                # Ajouter le nombre d'occurrences de ce token dans le document au score
                score += index[token][document]['count']
        
        # Stocker le score pour ce document
        scores[document] = score
    
    # Trier les documents en fonction de leur score
    sorted_documents =dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
    return sorted_documents
def calculate_score_postions(index, filtered_docs, tokens):
    stop_words = set(stopwords.words())
    scores = {}
    
    for doc in filtered_docs:
        score = 0
        for token in tokens:
            if token in stop_words:
                weight = 0.2
            else:
                weight = 0.8
                
            try:
                positions = index[token][doc]["positions"]
                for position in positions:
                    if positions in [0,1,2]:
                        #attribuer un score plus élevé aux mots-clés en début de titre
                        score += weight*5
                    else:
                        score += weight*2
            except KeyError:
                pass
        
        scores[doc] = score
    sorted_documents =dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
    return sorted_documents

