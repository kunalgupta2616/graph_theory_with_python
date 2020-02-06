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
       are to be connected names 
    """
    print("Enter the name of nodes to connect in graph: ")
    graph.add_edge((tuple(map(str,input().split()))))
    return graph

def info(graph):
    """Function that take the graph whose information is to be displayed
       Information includes - 
       number of nodes - Total number of nodes
       number of edges - Total number of edges
       degree - Degree of nodes (Indegree+ Outdegree)
       radius - Minimum eccentricity
       diameter - Maximum eccentricity
       eccentricity - Eccentricity of a node v is the maximum distance from v to
        all other nodes in graph.
       center - Set of nodes with eccentricity equal to radius.
       periphery - Set of nodes with eccentricity equal to the diameter.
       density
    """
    n.info(graph)
    print("radius: %d" % radius(graph))
    print("diameter: %d" % diameter(graph))
    print("eccentricity: %s" % eccentricity(graph))
    print("center: %s" % center(graph))
    print("periphery: %s" % periphery(graph))
    print("density: %s" % density(graph))
    return graph

def save():
    filename = input("Enter filename to save graph as:")
    plt.savefig(f"{}.png".format(filename))
    
#### MAIN ###

G = n.Graph()

print("Welcome to world of Graphs\n")
while(True):
    print("What you want to perform with graphs:\n1.Add node \
    \n2.Add edge\n3.Display Information\n4.Save Graph")
    query = input()
    if query == "1" or "Add node":
        add_nodes(G)
        n.draw(G,with_labels=True)
        plt.show()
    elif query == "2" or "Add edge":
        add_edges(G)
        n.draw(G,with_labels=True)
        plt.show()
    elif query == "3" or "Display Information":
        info(G)
    else:
        sys.exit()    
