import networkx as n
import matplotlib.pyplot as plt
import sys


### Functions ###
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

def complete():
    """Make a complete graph of the number of nodes given by the user.
    """
    nodes=int(input("Enter number of nodes in Complete Graph: "))
    G = n.complete_graph(nodes)
    plt.title("Complete graph of %d nodes",% nodes)
    n.draw_networkx(G)
    plt.show()
    return G
    
def eulerian(graph):
    """Return the edges of an Eulerian circuit in G.
       An Eulerian circuit is a path that crosses every edge 
       in G exactly once and finishes at the starting node.
    """
    return print("Eulerian Path = ",list(n.eulerian_circuit(graph)))


### MAIN ###
G = n.Graph()
print("Welcome to world of Graphs\n")
while(True):
    print("What you want to perform with graphs:\n1.Add node \
    \n2.Add edge\n3.Make a complete graph\n4.Find Eulerian path if any")
    query = input().lower()
    
    if (query == "1" or query=="Add node"):
        add_nodes(G)
        n.draw(G,with_labels=True)
        plt.show()
        
    elif (query == "2" or query=="Add edge"):
        add_edges(G)
        n.draw(G,with_labels=True)
        plt.show()
        
    elif (query == "3" or query=="Make a complete graph"):
        complete()
    
    elif (query =="4" or query=="Eulerian Path"):
        hamiltonian(G)
        
    else:
        sys.exit()  
