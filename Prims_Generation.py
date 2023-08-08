from random import shuffle,choice
from Protocols import Maze

class Prims_Generation(Maze):
    def __init__(self, height, width):
        self.nodes = set()
        self.edges = set()
        self.height,self.width = height,width

        #populate all the nodes and edges
        for j in range(height):
            for i in range(width):
                current_node = (j,i)
                self.nodes.add(current_node)
                if i < width-1:
                    self.edges.add((current_node, (j,i+1)))
                if j < height-1:
                    self.edges.add((current_node, (j+1,i)))

        #Start with a grid full of walls
        #Pick a cell, mark it as part of the maze. Add the walls of the cell to the wall list
        #while there are walls in the list:
        #   1. pick a random wall from the list. If only one of the cells that the wall divides is visited, then:
        #       1.Make the wall a passage and mark the unvisited cell as part of the maze
        #       2.Add the neighboring walls of the cell to the wall list
        #   2.Remove the wall from the list

        #first_node = choice(nodes)
        #lst = [get_edges(first_node)]
        #while len(shuffle(lst)) > 0:
            #n1,n2 = lst.pop()
            #if n2 not in visited:
                #solution.add(edge)
                #visited.add(n2)
                #lst.extend(get_edges(n2))
        first_node = choice(tuple(self.nodes))
        visited = {first_node}
        solution = set()
        lst = self.get_edges(first_node)
        shuffle(lst)
        while len(lst) > 0:
            n1,n2 = lst.pop()
            if (n1 in visited and n2 not in visited) or (n2 in visited and n1 not in visited):
                solution.add((n1,n2))
                if n1 not in visited:
                    visited.add(n1)
                    lst.extend(self.get_edges(n1))
                if n2 not in visited:
                    visited.add(n2)
                    lst.extend(self.get_edges(n2))
            shuffle(lst)
            
        self.paths = solution
        self.solution_nodes = set()


    def get_edges(self, node):
        j,i = node
        edges = []
        if i < self.width-1:
            edges.append((node, (j,i+1)))
        if i > 0:
            edges.append((node, (j,i-1)))
        if j < self.height-1:
            edges.append((node, (j+1,i)))
        if j > 0:
            edges.append((node, (j-1,i)))
        return edges