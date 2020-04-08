class Graph:

	def __init__(self):
		self.listOfNodes = {}

	def addNode(self, nodeVal):
		self.listOfNodes[nodeVal] = []

	def addUndirectedEdge(self, first, second):
		# If the nodes are equal, then it is a self-loop node and only needs to be added once 
		# to the adjacency matrix
		if first == second:
			self.listOfNodes[first].append(second)
		else:
			self.listOfNodes[first].append(second)
			self.listOfNodes[second].append(first)

	def removeUndirectedEdge(self, first, second):
		self.listOfNodes[first].remove(second)
		self.listOfNodes[second].remove(first)

		# Create a list that holds all of the keys in the Node dictionary
		k = list(self.listOfNodes.keys())

		# Iterate through the list of keys and remove any nodes with an empty list 
		for key in k:
			if self.listOfNodes[key] == []:
				del self.listOfNodes[key]

	def getAllNodes(self):
		return self.listOfNodes
		

