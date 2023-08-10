from Protocols import Maze, Solver
from Maze_Types import Maze_Types
from Solver_Base import Solver_Base
from collections import deque


class BFS(Solver):
    def __init__(self, maze: Maze):
        self.maze: Maze = maze
        self.visited: list[Maze_Types.NodeId] = []
        self.adjacency_list = Solver_Base.create_adjacency_list(maze)
        self.deque = deque()

    def solve(self) -> list[Maze_Types.NodeId]:
        start = (0,0)
        end = (self.maze.height-1, self.maze.width-1)
        self.deque.append([start])
        while self.deque:
            path = self.deque.pop()
            node = path[-1]
            if node not in self.visited:
                neighbors = self.adjacency_list[node]
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    self.deque.append(new_path)

                    if neighbor == end:
                        self.maze.solution_nodes = set(new_path)
                        return new_path
                self.visited.append(node)
        pass