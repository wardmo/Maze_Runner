from Maze_Types import Maze_Types


class Solver_Base():
    def __init__(self):
        pass

    @staticmethod
    def create_adjacency_list(maze):
        adj: Maze_Types.AdjacencyList = {}
        for edge in maze.paths:
            n1,n2 = edge
            if n1 in adj:
                adj[n1].add(n2)
            else:
                adj[n1] = {n2}
            if n2 in adj:
                adj[n2].add(n1)
            else:
                adj[n2] = {n1}
        return adj