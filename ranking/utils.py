from unidecode import unidecode
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import json

def preprocessing(text):
    #pour unidecoder les mots 
    text=unidecode(text.lower())
    print(text)
    return text
def word_tokenizer(text):
    tokens = word_tokenize(text)
    return tokens
def stopWords(tokens):
    stop_words = set(stopwords.words())
    filtered_tokens = [token for token in tokens if token not in stop_words]
    return filtered_tokens


def output(documents_sorted,documents):
    results={}
    results["metadata"]={}
    results["metadata"]["num_documents_in_index"] = len(documents)
    results["metadata"]["num_filtered_documents"] = len(documents_sorted)
    for i, score in  documents_sorted.items():
        for j in range(len(documents)):
            if str(i)==str(documents[j]['id']):
                results[str(i)]={}
                results[str(i)]['url']=documents[j]['url']
                results[str(i)]['title']=documents[j]['title']
                results[str(i)]['score']=score
    with open("output/results.json","w") as f:
        json.dump(results,f)