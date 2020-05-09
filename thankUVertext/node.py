class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.incomingEdges = 0
        self.visited = False
