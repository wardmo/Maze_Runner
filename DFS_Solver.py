from Protocols import Maze, Solver
from Maze_Types import Maze_Types
from random import choice


class DFS(Solver):
    def __init__(self, maze:Maze):
        self.maze: Maze = maze
        self.visited: list[Maze_Types.NodeId] = []
        self.adjacency_list = self.create_adjacency_list(maze)
        self.solution_nodes = set()

    def create_adjacency_list(self, maze: Maze) -> Maze_Types.AdjacencyList:
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
    
    def solve(self) -> list[Maze_Types.NodeId]:
        start = (0,0)
        end = (self.maze.height-1, self.maze.width-1)
        frontier = [start]
        visited = set()
        solution = {}
        current = start
        while frontier:
            current = frontier.pop()
            if current == end:
                break
            visited.add(current)
            for next_node in self.adjacency_list[current]:
                if next_node in visited:
                    continue
                else:
                    frontier.append(next_node)
                    solution[frontier[-1]] = current

        self.maze.solution_nodes.add(start)
        while end != start:
            self.maze.solution_nodes.add(end)
            end = solution[end]




