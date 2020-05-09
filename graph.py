import node

class Graph:
    def __init__(self):
        self.nodes = []

    def addNode(self, n):
        self.nodes.append(node.Node(n))

    def addUndirectedEdge(self, first, second):
        if second not in first.neighbors and first not in second.neighbors:
            first.neighbors.append(second)
            second.neighbors.append(first)

    def removeUndirectedEdge(self, first, second):
        try:
            first.neighbors.remove(second)
            second.neighbors.remove(first)
        except:
            print("Unable to remove edges from these nodes. They are not connected!")
    
    # Returns all of the nodes as a set as defined in requirements
    def getAllNodes(self):
        return set(self.nodes)

    # Returns all of the nodes as a list for use in by other functions (lists are easier to iterate over)
    def getAllNodesAsList(self):
        return self.nodes

    # Print the value of all nodes
    def printAllNodes(self):
        for node in self.nodes:
            print(node.value)

    # Print all nodes with their neighbors in a clean manner
    def printAllNodesWithNeighbors(self):
        for node in self.nodes:
            neighbor = node.neighbors
            nVal = []
            for x in neighbor:
                nVal.append(x.value)
            print(node.value, ' -> ', nVal)
