import networkx as n
import matplotlib.pyplot as plt
import sys


### Functions ###
def add_nodes(graph):
    """Function to add nodes in the graph:
       Parameters - take a list of space separated node names 
    """
    print("Enter the name of nodes to add to graph: ")
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

def info(graph):
    """Function that take the graph whose information is to be displayed
       Information includes - 
       number of nodes - Total number of nodes
       number of edges - Total number of edges
       Average degree - Degree of nodes (Indegree+ Outdegree)
       radius - Minimum eccentricity
       diameter - Maximum eccentricity
       eccentricity - Eccentricity of a node v is the maximum distance from v to
        all other nodes in graph.
       center - Set of nodes with eccentricity equal to radius.
       periphery - Set of nodes with eccentricity equal to the diameter.
       Density
    """
    try:
        print("-"*10,"Node Attributes","-"*10)
        print(n.info(graph))
        print("-"*10,"Distance Measures","-"*10)
        print("radius: %d" % n.radius(graph))
        print("diameter: %d" % n.diameter(graph))
        print("eccentricity: %s" % n.eccentricity(graph))
        print("center: %s" % n.center(graph))
        print("periphery: %s" % n.periphery(graph))
        print("density: %s" % n.density(graph))
    except Exception as ex:
        print(ex)
    return graph

def save():
    try:
        filename = input("Enter filename to save graph as:")
        plt.savefig(f"{0}.png".format(filename))
        print("File Saved Successfully")
    except Exception as e:
        print("Something went wrong: ",e)
    return None
    
#### MAIN ###

G = n.Graph()

print("Welcome to world of Graphs\n")
while(True):
    print("What you want to perform with graphs:\n1.Add node \
    \n2.Add edge\n3.Display Information\n4.Save Graph")
    query = input().lower()
    if (query == "1" or query=="Add node"):
        add_nodes(G)
        n.draw(G,with_labels=True)
        plt.show()
    elif (query == "2" or query=="Add edge"):
        add_edges(G)
        n.draw(G,with_labels=True)
        plt.show()
    elif (query == "3" or query=="Display Information"):
        info(G)
    elif (query =="4" or query=="save"):
        save()
    else:
        sys.exit()
