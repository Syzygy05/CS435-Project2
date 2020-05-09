import queue

class GraphSearch:

    def DFSRec(self, start, end):
        stack = [start]
        path = []
        return self.DFSRecHelper(end, stack, path)


    def DFSRecHelper(self, end, stack, path):
        if len(stack) > 0:
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
            
            return self.DFSRecHelper(end, stack, path)
        else:
            return None


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

    
    def BFTRec(self, graph):
        nodesInGraph = graph.getAllNodesAsList()
        q = queue.Queue(maxsize = 0) 
        path = []
        q.put(nodesInGraph[0])
        
        return self.BFTRecHelper(q, path)

    def BFTRecHelper(self, q, path):
        if q.qsize() > 0:
            currentNode = q.get()
            currentNode.visited = True
            path.append(currentNode)

            for node in currentNode.neighbors:
                if node.visited == False:
                    q.put(node)  
                else:
                    continue

            return self.BFTRecHelper(q, path)
        else:
            return path



    def BFTIter(self, graph):
        nodesInGraph = graph.getAllNodesAsList()
        q = queue.Queue(maxsize = 0) 
        path = []
        q.put(nodesInGraph[0])

        while q.qsize() > 0:
            currentNode = q.get()
            currentNode.visited = True
            path.append(currentNode)

            for node in currentNode.neighbors:
                if node.visited == False:
                    q.put(node)  
                else:
                    continue

        return path



