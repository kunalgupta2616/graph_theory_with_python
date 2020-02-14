import networkx as n
import matplotlib.pyplot as plt
import sys
import networkx.algorithms.isomorphism as iso
%matplotlib inline



### Functions ###
def choose_graph():
    print("Which graph you want to select G1 or G2: ")
    choice = input().lower()
    try:
        if choice =="g1":
            return G1
        if choice =="g2":
            return G2
    except Exception as e:
        print("Wrong Choice")
def add_nodes(graph):
    """Function to add nodes in the graph:
       Parameters - take a list of space separated node names 
    """
    print("Enter the name of node to add to graph: ")
    graph.add_nodes_from(list(map(str,input().split())))
    return graph

def add_edges(graph):
    """Function to add edges in the graph:
       Parameters - take a tuple of space separated nodes that
       are to be connected 
    """
    print("Enter the name of nodes to connect in graph: ")
    edge_tuple = tuple(map(str,input().split()))
    graph.add_edge(*edge_tuple)
    return graph

def isomorphism(graph1,graph2):
    """Returns True if both graphs are isomorphic else False
    """
    return n.is_isomorphic(graph1,graph2)
    


G1 = n.DiGraph()
G2 = n.DiGraph()
print("Welcome to world of Graphs\n")
while(True):
    print("What you want to perform with graphs:\n1.Add node \
    \n2.Add edge\n3.Check for Isomorphism")
    query = input().lower()
    
    if (query == "1" or query=="Add node"):
        G = choose_graph()
        add_nodes(G)
        plt.figure(2,figsize=(8, 5))
        n.draw_networkx(G1,with_labels=True,label="Graph G1")
        plt.figure(1,figswith_labels=(8, 6))
        n.draw_networkx(G2,with_labels=True,label="Graph G2")
        plt.show()
        
    elif (query == "2" or query=="Add edge"):
        G = choose_graph()
        add_edges(G)
        plt.figure(1,figsize=(8, 6))
        n.draw_networkx(G1,with_labels=True,label="Graph G1")
        plt.figure(1,figswith_labels=(8, 6))
        n.draw_networkx(G2,with_labels=True,label="Graph G2")        
        plt.show()
        
    elif (query == "3" or query=="check for isomorphism"):
        result = isomorphism(G1,G2)
        
        print(result)
        
    else:
        sys.exit() 
