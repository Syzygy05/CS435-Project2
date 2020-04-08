import graph
import graphsearch
import random

# Create a graph and empty list that holds nodes
g = graph.Graph()
nodes = []

def createRandomUnweightedGraphIter(n):
	
	adjMatrix = g.getAllNodes()
	
	for i in range(n):
		while True:
			# Pick a random number that will be added as a node
			randNum = random.randint(0, 1000)

			# If the number is in the adjaceny matrix, then pick another number (restart loop)
			# Else add the node to the graph, append the node to the local list of nodes in the 
			# graph, and exit the loop
			if randNum in adjMatrix:
				continue
			else:
				g.addNode(randNum)
				nodes.append(randNum)
				break

	# Add the edges to the nodes randomly. 
	# Node some nodes will not have edges and some will be cyclical due to the nodes being picked 
	# randomly
	for i in range(5):
		# Pick 2 random nodes
		first = random.choice(list(adjMatrix))
		second = random.choice(list(adjMatrix))

		# Add an edge as long as the edge does not already exist
		if second not in adjMatrix[first] and first not in adjMatrix[first]:
			g.addUndirectedEdge(first, second)



def createLinkedList(n):

	for i in range(n):
		# Pick a random number that will be added as a node
		randNum = random.randint(0, 1000)

		# Add node to graph and list of nodes
		g.addNode(randNum)
		nodes.append(randNum)

		# Only add an undirected edge if there are more than 1 nodes in the graph
		if i > 0:
			g.addUndirectedEdge(nodes[-2], randNum)




# TESTING CODE
#createLinkedList(5)

createRandomUnweightedGraphIter(5)

gs = graphsearch.GraphSearch(g)

print(gs.DFSRec(nodes[0], nodes[2]))








