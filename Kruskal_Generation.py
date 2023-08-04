from random import shuffle

class Kruskal_Generation():
    @classmethod
    def generate(cls, height, width):
        return Kruskal_Generation(height, width).solution

    def __init__(self, height, width):
        self.nodes = set()
        self.edges = set()

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
        self.edges = list(self.edges)
        shuffle(self.edges)
        
        for n1,n2 in self.edges:
            if n1 != n2:
                if self.find_set(n1) != self.find_set(n2):
                    solution.add((n1,n2))
                    self.union(n1,n2)

        self.solution = solution
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
