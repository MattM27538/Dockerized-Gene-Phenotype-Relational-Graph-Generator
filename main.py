import networkx as nx
import matplotlib.pyplot as plt
import json
from pymongo import MongoClient


def mongo_init(MongoDBclient):
    MongoDBclient=MongoClient('localhost', 27017)
    db=MongoDBclient['GenePhenotypeDB']
    return db

def main():
    #Initialize MongoDB and a mongo collection.
    mongoDBclient=None
    db=mongo_init(mongoDBclient)
    dbcollection=db['CancersAndRelatedGenes']

    #Read cancers and associated genes information from json file into MongoDB collection.
    with open('cancergenes.json') as file:
        fileData=json.load(file)

    dbcollection.insert_many(fileData)
    
    #Create and fill dictionary with values of genes and associated cancers.
    cancerGenesDict={}
    with open('cancergenes.json') as file2:
        fileData2=json.load(file2)
        for object in fileData2:
            for key,values in object.items():
                cancerGenesDict[key]=values
                for value in values:
                    if value not in cancerGenesDict:
                        cancerGenesDict[value]=[key]
                    else:
                        cancerGenesDict[value].append(key)

    #Enter gene or phenotype of interest and how many degrees of connections
    #from starting point to display in graph.
    querySet=set()
    genePhenotypeNetwork = nx.Graph()
    while True:
        print("Please enter your gene of phenotype of interest to begin.")
        initialQuery=str(input())

        if initialQuery in cancerGenesDict:
            print(cancerGenesDict[initialQuery])
            querySet.add(initialQuery)
            break
        else:
            print("Query not Found.")

    print("Please enter the number of degrees to display.")
    degrees=int(input())

    #Add nodes  and edge to graph based on initial interest gene or phenotype 
    #and degrees of separation. 
    for _ in range(degrees):
        tempSet=set()
        for query in querySet:
            for value in cancerGenesDict[query]:
                genePhenotypeNetwork.add_edge(query,value)
                tempSet.add(value) 
        querySet=tempSet

    pos=nx.spring_layout(genePhenotypeNetwork,k=3)
    plt.figure(3,figsize=(16,16))
    nx.draw_networkx(genePhenotypeNetwork, pos = pos, with_labels = True)
    plt.savefig("genePhenotypeNetwork.png")
    dbcollection.drop()

if __name__=="__main__":
    main()