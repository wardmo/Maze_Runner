from random import shuffle
from Protocols import Maze

class Kruskal_Generation(Maze):

    def __init__(self, height, width):
        self.nodes = set()
        self.edges = set()
        self.height,self.width = height,width

        # populate all the nodes and edges
        for j in range(height):
            for i in range(width):
                current_node = (j,i)
                self.nodes.add(current_node)
                if i < width-1:
                    self.edges.add((current_node, (j, i+1)))
                if j < height-1:
                    self.edges.add((current_node, (j+1, i)))

        self.clusters = {n:n for n in self.nodes}
        self.ranks = {n:0 for n in self.nodes}
        solution = set()
        edgelist = list(self.edges)
        shuffle(edgelist)
        
        for n1,n2 in edgelist:
            if n1 != n2:
                if self.find_set(n1) != self.find_set(n2):
                    solution.add((n1,n2))
                    self.union(n1,n2)

        self.solution = solution
        self.walls = self.edges.difference(self.solution)

        pass

    def find_set(self, n):
        if self.clusters[n] != n:
            self.clusters[n] = self.find_set(self.clusters[n])
        return self.clusters[n]
        pass
    
    def union(self,n1,n2):
        x,y = self.find_set(n1), self.find_set(n2)
        if self.ranks[x] == self.ranks[y]:
            self.clusters[y] = x
        else:
            self.clusters[x] = y
        if self.ranks[x] == self.ranks[y]:
            self.ranks[y] += 1
        pass
