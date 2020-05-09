import node
import directedGraph
import topSort
import random

def createRandomDAG(n):
    dag = directedGraph.DirectedGraph()

    randomNums = []

    for i in range(n):
        while True:
            val = random.randint(0, n * 10)

            if val not in randomNums:
                randomNums.append(val)
                dag.addNode(val)
                break
            else:
                continue
    
    nodes = dag.getAllNodes()

    for i in range(n):
        while True:
            # Get 2 random nodes from the list of nodes in the graph class
            first = random.choice(tuple(nodes))
            second = random.choice(tuple(nodes))

            # Add an edge if they are not the same node
            if first != second:
                dag.addDirectedEdge(first, second)
                break
            else:
                continue

    return dag

# Prints a list of nodes in a list
# Used to print the path used to traverse in the recursive and iterative approaches
def printPath(path):
    for node in path:
        print(node.value)



dag = createRandomDAG(5)

dag.printAllNodesWithNeighbors()

ts = topSort.TopSort()

#path = ts.Kahns(dag)

#path = ts.mDFS(dag)

#printPath(path)
