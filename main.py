import networkx as nx
import matplotlib.pyplot as plt
import json

def draw_graph(genePhenotypeNetwork):
    pos=nx.spring_layout(genePhenotypeNetwork,k=3)
    plt.figure(3,figsize=(16,16))
    nx.draw_networkx(genePhenotypeNetwork, pos = pos, with_labels = True)
    print("Save file as:")
    saveFileName=str(input())
    plt.savefig(saveFileName+".png")
    plt.show()

# Read in diseases and associated gene(s) information from json file and 
# store information in dictionary.
def read_json_file(genePhenotypeDict):
    with open('cancergenes.json') as jsonFile:
        jsonFileData=json.load(jsonFile)
    
    for object in jsonFileData:
        for key,values in object.items():
            genePhenotypeDict[key]=values
            for value in values:
                if value not in genePhenotypeDict:
                    genePhenotypeDict[value]=[key]
                else:
                    genePhenotypeDict[value].append(key)

    jsonFile.close()

#Enter gene or phenotype of interest and how many degrees of connections
#from starting point to display in graph.
def get_user_input(genePhenotypeDict,querySet):
    while True:
        print("Please enter your gene or phenotype of interest to begin.")
        initialQuery=str(input())
        if initialQuery in genePhenotypeDict:
            querySet.add(initialQuery)
            break
        else:
            print("Query not Found.")

    print("Please enter the number of degrees to display.")
    degrees=int(input())
    return degrees

#Add nodes and edge to graph based on initial interest gene or phenotype 
#and degrees of separation. 
def add_nodes_to_graph(degrees,querySet,genePhenotypeDict,genePhenotypeNetwork):
    for _ in range(degrees):
        tempSet=set()
        for query in querySet:
            for value in genePhenotypeDict[query]:
                genePhenotypeNetwork.add_edge(query,value)
                tempSet.add(value) 
        querySet=tempSet

def main():
    #Create and fill dictionary with values of genes and associated disease.
    genePhenotypeDict={}
    read_json_file(genePhenotypeDict)

    querySet=set()
    genePhenotypeNetwork = nx.Graph()
    degrees=get_user_input(genePhenotypeDict,querySet)

    add_nodes_to_graph(degrees,querySet,genePhenotypeDict,genePhenotypeNetwork)
    
    draw_graph(genePhenotypeNetwork)
if __name__=="__main__":
    main()