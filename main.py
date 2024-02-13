import json
from ranking.filtrer_documents import *
from ranking.ranking import *
import click
@click.command()
@click.option('--query')
@click.option('--mode')
def run(query,mode):
 
   # Charger l'index à partir d'un fichier JSON
    with open("title_pos_index.json", 'r') as f:
     index = json.load(f)
    #faire le preprocessing de  Query 
    tokens=traitement(query)
    documents_filtred=filtered_documents(tokens,index,mode)
    #calculer le score en prenant en compte le nombres d'occurencs de mots "count
    sorted_documents=calculate_score_postions(index,documents_filtred,tokens)
    with open("documents.json",'r') as f:
       documents=json.load(f)

    output(sorted_documents,documents)


if __name__ == '__main__':
    run()