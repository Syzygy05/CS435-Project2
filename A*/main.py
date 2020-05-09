import gridGraph
import node
import random
import math

def createRandomGridGraph(n):

    gg = gridGraph.GridGraph()

    for i in range(n):
        for j in range(n):
            val = i + j * 2
            gg.addGridNode(i, j, val)

    nodes = gg.getAllNodesAsList()
    print(nodes)
    
    for node in nodes:
        for neighbor in node.neighbors:
            randPercent = random.random()
            if randPercent >= .5:
                gg.addUndirectedEdge(node, neighbor)

    return gg

def astar(graph, sourceNode, destNode):
    dist = {}
    dist[sourceNode] = (0, manhattanDistance(sourceNode, destNode))
    path = []
    curr = sourceNode

    while curr != destNode:
        curr.visited = True
        for neighbor in curr.neighbors:
            if neighbor.visited == False:
                d = dist[curr][0] + 1
                h = manhattanDistance(neighbor, destNode)
                if d < dist[curr][1]:
                    dist[curr] = (d, h)

        visitedSet = set()
        nodes = graph.getAllNodesAsList()
        for node in nodes:
            if node.visited == True:
                visitedSet.add(node)
        
        curr = minDist(dist, visitedSet)

    return list(visitedSet)


def manhattanDistance(source, dest):
    return abs(source.x - dest.x) + abs(source.y - dest.y)

# Taken from Professors repl.it Lesson 18
def minDist(distances: dict, visited:set) -> node:
  ans = None
  m = math.inf
  for curr in distances.keys():
    if curr not in visited and distances[curr] <= m:
      m = distances[curr]
      ans = curr
  return ans

gg = createRandomGridGraph(5)

sourceNode = gg.nodes[(0, 0)]
destNode = gg.nodes[(100, 100)]

path = astar(gg, sourceNode, destNode)

for node in path:
    print((node.x, node.y) + " -> ", end="")