from random import choice
from Protocols import Maze


class Wilsons_Generation(Maze):
    def __init__(self, height, width):
        self.height,self.width = height,width
        self.nodes = list()

        for j in range(height):
            for i in range(width):
                self.nodes.append((j,i))

        
        self.paths = set()
        self.solution_nodes = set()
        first_node = self.pop_random_node()
        maze_nodes = {first_node}
        while self.nodes:
            arb = self.pop_random_node()
            visited = [arb]
            next_node = choice(self.get_neighbor_nodes(arb))
            while next_node not in maze_nodes:
                if next_node not in visited:
                    visited.append(next_node)
                    next_node = choice(self.get_neighbor_nodes(next_node))
                else:
                    while visited.pop() != next_node:
                        pass
            for i,node in enumerate(visited):
                maze_nodes.add(node)
                if node in self.nodes:
                    self.nodes.remove(node)
                next = next_node if i == len(visited)-1 else visited[i+1]
                self.paths.add((node,next))
        
        self.nodes = maze_nodes

    def get_neighbor_nodes(self, node):
        j,i = node
        nodes = set()
        if i < self.width-1:
            nodes.add((j,i+1))
        if i > 0:
            nodes.add((j,i-1))
        if j < self.height-1:
            nodes.add((j+1,i))
        if j > 0:
            nodes.add((j-1,i))
        return list(nodes)


    def pop_random_node(self):
        return self.nodes.pop(choice(range(len(self.nodes))))


