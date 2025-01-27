import networkx as nx
import matplotlib.pyplot as plt
import json
from pymongo import MongoClient

#Todo
# list all keys
# account for end range of degrees
#is int? degrees
# successfully found # of degrees from start
#if first query fails return error.
# change exit to restart while loop
#integrate assert
#graceful shutdown collection drop

def mongo_init(MongoDBclient):
    MongoDBclient=MongoClient('localhost', 27017)
    db=MongoDBclient['GenePhenotypeDB']
    return db

def main():
    mongoDBclient=None
    db=mongo_init(mongoDBclient)
    dbcollection=db['CancerRelatedGenes']

    with open('cancergenes.json') as file:
        fileData=json.load(file)

    dbcollection.insert_many(fileData)
    
    query=None
    start=None
    result=None
    degreeList=[]
    diseaseNetwork = nx.Graph()
    nodePair=[]

    while start==None:
        print("Please enter 'gene' or 'phenotype' to begin.")
        start=str(input())

        if start!="gene" and start!="phenotype":
            print("Unrecognized input.")
            start=None
    
    if start=="gene":
        print("Please enter the gene of interest.")
        query=str(input())
        result=dbcollection.find({"Associated Gene" : query}, {'_id': False})
    else:
        print("Please enter the phenotype of interest.")
        query=str(input())
        result=dbcollection.find({"Classification" : query}, {'_id': False})

    print("Please enter the number of degrees to display.")
    degrees=int(input())
    for document in result:
        for key,value in document.items():
            # print("key=", key)
            print("value =", value)
            nodePair.append(value)
        print("nodePair =", nodePair)
        diseaseNetwork.add_edge(nodePair[0],nodePair[1])
        degreeList.append(nodePair[0])
        nodePair=[]

    pos=nx.spring_layout(diseaseNetwork,k=3)
    plt.figure(3,figsize=(16,16))
    nx.draw_networkx(diseaseNetwork, pos = pos, with_labels = True)
    plt.savefig("diseaseNetwork.png")
    dbcollection.drop()

if __name__=="__main__":
    main()