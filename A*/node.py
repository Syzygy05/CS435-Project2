class Node:
    def __init__(self, x, y, value):
        self.value = value
        self.x = x
        self.y = y
        self.neighbors = []
        self.visited = False
        