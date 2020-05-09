import weightedGraph
import random
import math
import queue
import node


def createRandomCompleteWeightedGraph(n):
    wg = weightedGraph.WeightedGraph()

    valuesToAdd = []

    for i in range(n):
        while True:
            val = random.randint(0, n * 10)

            if val not in valuesToAdd:
                valuesToAdd.append(val)
                wg.addNode(val)
                break
            else:
                continue
    
    nodes = wg.getAllNodesAsList()

    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if nodes[i] != nodes[j]:
                weight = random.randint(1, 51)
                wg.addWeightedEdge(nodes[i], nodes[j], weight)

    return wg

def createLinkedList(n):
    wgLL = weightedGraph.WeightedGraph()

    for i in range(n):
        wgLL.addNode(i)
        if len(wgLL.nodes) > 1:
            wgLL.addWeightedEdge(wgLL.nodes[-2], wgLL.nodes[-1], 1)
    
    return wgLL

def dijkstras(graph, start):
    dist = {}
    nodes = graph.getAllNodesAsList()
    

    for node in nodes:
        dist[node] = math.inf
    
    dist[start] = 0
    curr = start
    
    while curr != None and dist[curr] != math.inf:
        curr.visited = True
        for neighbor in curr.neighbors:
            if neighbor.visited == False:
                updatedDist = dist[curr] + curr.edgeWeights[neighbor]
        
        visitedSet = set()
        for node in nodes:
            if node.visited == True:
                visitedSet.add(node)

        curr = minDist(dist, visitedSet)

    return dist


# Taken from Professors repl.it Lesson 18
def minDist(distances: dict, visited:set) -> node:
  ans = None
  m = math.inf
  for curr in distances.keys():
    if curr not in visited and distances[curr] <= m:
      m = distances[curr]
      ans = curr
  return ans



#wg = createRandomCompleteWeightedGraph(5)

wg = createLinkedList(5)

#wg.printAllNodesWithNeighbors()
nodes = wg.getAllNodesAsList()
print(dijkstras(wg, nodes[0]))