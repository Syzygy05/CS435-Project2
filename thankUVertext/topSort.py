import queue

class TopSort:
    def Kahns(self, dag):
        q = queue.Queue(maxsize = 0)
        nodes = dag.getAllNodesAsList()
        path = []
        for node in nodes:
            if node.incomingEdges == 0:
                q.put(node)
        
        while q.qsize() > 0:
            currentNode = q.get()
            path.append(currentNode)
            for neighbor in currentNode.neighbors:
                neighbor.incomingEdges -= 1
                if neighbor.incomingEdges == 0:
                    q.put(neighbor)

        return path

    def mDFS(self, dag):
        stack = []
        nodes = dag.getAllNodesAsList()

        for node in nodes:
            for neighbor in node.neighbors:
                neighbor.visited = True
            stack.append(node)

        return stack.reverse()

    # DFS Iterative Travesal from graphsearch.py file
    def DFSIter(self, start, end):
        stack = [start]
        path = []

        while len(stack) > 0:
            currentNode = stack.pop()
            currentNode.visited = True
            path.append(currentNode)

            if currentNode == end:
                return path
            
            for node in currentNode.neighbors:
                if node.visited == False:
                    stack.append(node)
                else:
                    continue
            
        
        return None