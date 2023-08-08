from random import choice
from Protocols import Maze


class DFS_Generation(Maze):
    def __init__(self, height, width):
        self.height, self.width = height, width
        self.nodes, self.edges = set(),set()

        for j in range(height):
            for i in range(width):
                current_node = (j,i)
                self.nodes.add(current_node)

        first_node = choice(list(self.nodes))
        self.paths = set()
        self.visited = set()
        self.solution_nodes = set()
        self._dfs(first_node)
        pass

    def _dfs(self, node):
        self.visited.add(node)
        nodes = self.unvisited_neighbor_nodes(node)
        while len(nodes) > 0:
            next_node = nodes.pop(choice(range(len(nodes))))
            self.paths.add((node,next_node))
            self._dfs(next_node)
            nodes = self.unvisited_neighbor_nodes(node)

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