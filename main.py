import node
import graph
import graphsearch
import random


def createRandomUnweightedGraphIter(n):
    g = graph.Graph()

    # Holds the random numbers to ensure double are not entered into graph
    randomNums = []

    for i in range(n):
        while True:    

            val = random.randint(0, n * 10)

            # if the random value is unique, add to randomNum list and add to graph
            if val not in randomNums:
                randomNums.append(val)
                g.addNode(val)
                break
            else:
                continue
    
    nodes = g.getAllNodes()
    
    for i in range(n):
        while True:
            # Get 2 random nodes from the list of nodes in the graph class
            first = random.choice(tuple(nodes))
            second = random.choice(tuple(nodes))

            # Add them if they are not the same node
            if first != second:
                g.addUndirectedEdge(first, second)
                break
            else:
                continue

    return g

def createLinkedList(n):
    g = graph.Graph()

    for i in range(n):
        g.addNode(i)
        if len(g.nodes) > 1:
            g.addUndirectedEdge(g.nodes[-2], g.nodes[-1])

    return g

def BFTRecLinkedList(g):
    gs = graphsearch.GraphSearch()
    path = gs.BFTRec(g)
    printPath(path)

def BFTIterLinkedList(g):
    gs = graphsearch.GraphSearch()
    path = gs.BFTIter(g)
    printPath(path)

# Prints a list of nodes in a list
# Used to print the path used to traverse in the recursive and iterative approaches
def printPath(path):
    for node in path:
        print(node.value)


# Create a graph with randomness
#g = createRandomUnweightedGraphIter(5)
#g.printAllNodesWithNeighbors()

# Create a graph linearly
#g = createLinkedList(5)
#g.printAllNodesWithNeighbors()

# Get all the nodes in the graph
#nodes = g.getAllNodesAsList()

# Create a graphSearch object
gs = graphsearch.GraphSearch()

# DFSRec Traversal
#path = gs.DFSRec(nodes[1], nodes[-1])

# DFSIter Traversal
#path = gs.DFSIter(nodes[3], nodes[-1])

# BFTRec Traversal
#path = gs.BFTRec(g)

# BFTIter Traversal
#path = gs.BFTIter(g)

# BFTRecLinkedList Traversal
#linkedList = createLinkedList(100)
#BFTRecLinkedList(linkedList)

# BFTIterLinkedList Traversal
linkedList = createLinkedList(1000000)
BFTIterLinkedList(linkedList)

# This code has been implemented as a function in def printPath above
# Print the path returned by functions
#for node in path:
#    print(node.value)

