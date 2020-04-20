class Graph:

	def __init__(self):
		self.adjMatrix = {}
		self.nodes = []

	def addNode(self, nodeVal):
		self.adjMatrix[nodeVal] = []

	def addUndirectedEdge(self, first, second):
		# If the nodes are equal, then it is a self-loop node and only needs to be added once 
		# to the adjacency list
		self.adjMatrix[first].append(second)
		self.adjMatrix[second].append(first)

	def removeUndirectedEdge(self, first, second):
		try:
			self.adjMatrix[first].remove(second)
			self.adjMatrix[second].remove(first)
		except:
			print('Error! Nodes are not connected by an edge.')

	def getAdjMatrix(self):
		return self.adjMatrix

	def getAllNodes(self):
		return set(self.nodes)
		

