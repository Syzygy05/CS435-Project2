class GraphSearch:

	def __init__(self, graph):
		self.graph = graph
		self.visitedNodes = []

	# Part d - Recursive DFS traversal that returns the nodes visited in a list from start to end
	def DFSRec(self, start, end):

		
		adjMatrix = self.graph.getAdjMatrix()
	
		
		self.visitedNodes.append(start)

		# Go through each neighboring node for the start node
		for node in adjMatrix[start]:
			# If the neighboring node is equal to the end node, add to visitedList and return list
			# Else if the node is in the already vistedNode list, goto next neighboring node
			# Else recursion to next node as start point 
			if node == end:
				self.visitedNodes.append(node)
				return self.visitedNodes
			elif node in self.visitedNodes:			
				continue
			else:
				return self.DFSRec(node, end)

	def DFSIter(self, start, end):
		
		# Pull the adjacenty matrix from the graph class
		adjMatrix = self.graph.getAllNodes()
		print(adjMatrix)
	
		# Add the start node to the visitedNode list
		self.visitedNodes.append(start)

		# Stack will add a node when it comes across it
		stack = []

		# Add the start node to stack
		stack.append(start)

		# Go through each neighboring node while the stack is not empty or the node has not been found, 
		# stop when node found or you have popped everything from stack
		while (len(stack) != 0):

			# Pop the node that was added last
			currNode = stack.pop()

			





		for node in adjMatrix[start]:
			print(node)
			break

	def BFTRec(self, start, end):
		pass

	def BFTIter(self, start, end):
		pass
