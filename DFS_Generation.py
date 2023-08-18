from random import choice, shuffle
from Protocols import Maze


class DFS_Generation(Maze):
    def __init__(self, height, width):
        self.height, self.width = height, width
        self.nodes = set((j,i) for i in range(width) for j in range(height))
        self.visited = set()

        self.paths = set()
        first = choice(list(self.nodes))
        frontier = [(first, choice(self.unvisited_neighbor_nodes(first)))]
        self.visited.add(first)
        while frontier:
            previous,current = frontier.pop()
            if current not in self.visited:
                next_nodes = self.unvisited_neighbor_nodes(current)
                shuffle(next_nodes)
                for next in next_nodes:
                    frontier.append((current, next))
                self.paths.add((previous, current))
                self.visited.add(current)

        pass

    def unvisited_neighbor_nodes(self, node):
        j,i = node
        nodes = set()
        if i < self.width-1:
            next = (j,i+1)
            if next not in self.visited:
                nodes.add((j,i+1))
        if i > 0:
            next = (j,i-1)
            if next not in self.visited:
                nodes.add((j,i-1))
        if j < self.height-1:
            next = (j+1,i)
            if next not in self.visited:
                nodes.add((j+1,i))
        if j > 0:
            next = (j-1,i)
            if next not in self.visited:
                nodes.add((j-1,i))
        return list(nodes)