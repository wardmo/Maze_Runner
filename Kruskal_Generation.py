from random import shuffle


class Kruskal_Generation():
    def __init__(self, height, width):
        nodes = set()
        edges = set()

        for j in range(height):
            for i in range(width):
                current_node = (i,j)
                nodes.add(current_node)
                if i > 0:
                    neighbor_node = (i-1,j)
                    edges.add((current_node,neighbor_node))
                if i < width - 1:
                    neighbor_node = (i+1,j)
                    edges.add((current_node,neighbor_node))
                if j > 0:
                    neighbor_node = (i,j-1)
                    edges.add((current_node,neighbor_node))
                if j < height - 1:
                    neighbor_node = (i,j+1)
                    edges.add((current_node,neighbor_node))
        
        clusters = {n:n for n in nodes}
        ranks = {n:0 for n in nodes}
        solution = set()
        edges = list(edges)
        shuffle(edges)

        def find_set(n):
            if clusters[n] != n:
                clusters[n] = find_set(clusters[n])
            return clusters[n]
        
        def union(n1,n2):
            x,y = find_set(n1), find_set(n2)
            if ranks[x] == ranks[y]:
                clusters[y] = x
            else:
                clusters[x] = y
            if ranks[x] == ranks[y]:
                ranks[y] += 1
        
        for n1,n2 in edges:
            if n1 != n2:
                if find_set(n1) != find_set(n2):
                    solution.add((n1,n2))
                    union(n1,n2)

        self.solution = solution
