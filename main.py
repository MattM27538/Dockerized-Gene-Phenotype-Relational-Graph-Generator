import networkx as nx
import matplotlib.pyplot as plt
import json
from pymongo import MongoClient

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

if __name__=="__main__":
    main()