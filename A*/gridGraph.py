import node

class GridGraph:
    def __init__(self):
        self.nodes = {}

    def addGridNode(self, x, y, nodeVal):
        self.nodes[(x, y)] = node.Node(x, y, nodeVal)

    def addUndirectedEdge(self, first, second):
        if abs(first.x - second.x) == 0 and abs(first.y - second.y) == 1:
            if second not in first.neighbors:
                first.neighbors.append(second)
            if first not in second.neighbors:
                second.neighbors.append(first)
        elif abs(first.x - second.x) == 1 and abs(first.y - second.y) == 0:
            if second not in first.neighbors:
                first.neighbors.append(second)
            if first not in second.neighbors:
                second.neighbors.append(first)

    def removeUndirectedEdge(self, first, second):
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

  
            
            