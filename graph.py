class Graph:

	def __init__(self):
		self.listOfNodes = {}
		self.nodes = []
	def addNode(self, nodeVal):
		self.listOfNodes[nodeVal] = []

	def addUndirectedEdge(self, first, second):
		# If the nodes are equal, then it is a self-loop node and only needs to be added once 
		# to the adjacency matrix
		self.listOfNodes[first].append(second)
		self.listOfNodes[second].append(first)

	def removeUndirectedEdge(self, first, second):
		try:
			self.listOfNodes[first].remove(second)
			self.listOfNodes[second].remove(first)
		except:
			print('Error! Nodes are not connected by an edge.')

	def getAllNodes(self):
		return self.listOfNodes
		

