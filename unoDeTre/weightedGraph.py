import node

class WeightedGraph:
    def __init__(self):
        self.nodes = []

    def addNode(self, nodeVal):
        self.nodes.append(node.Node(nodeVal))

    def addWeightedEdge(self, first, second, edgeWeight):
        if second not in first.neighbors:
            first.neighbors.append(second)
            first.edgeWeights[second] = edgeWeight

    def removeDirectedEdge(self, first, second):
        try:
            first.neighbors.remove(second)
            first.edgeWeights.pop(second)
        except:
            print("Unable to remove weighted edge. They are not connected.")

    # Returns all of the nodes as a set as defined in requirements
    def getAllNodes(self):
        return set(self.nodes)  

    # Returns all of the nodes as a list for use in by other functions (lists are easier to iterate over)
    def getAllNodesAsList(self):
        return self.nodes

    # Print the value of all nodes
    def printAllNodes(self):
        for node in self.nodes:
            if node != None:
                print(node.value)

    # Print all nodes with their neighbors in a clean manner
    def printAllNodesWithNeighbors(self):
        for node in self.nodes:
            neighbor = node.neighbors
            nVal = []
            for x in neighbor:
                nVal.append(x.value)
            
            print(node.value, ' -> ', nVal, ' -> ', node.edgeWeights)
            
        