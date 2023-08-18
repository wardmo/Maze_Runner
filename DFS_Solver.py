from Protocols import Maze, Solver
from Maze_Types import Maze_Types
from Solver_Base import Solver_Base
from random import choice


class DFS(Solver):
    def __init__(self, maze:Maze):
        self.maze: Maze = maze
        self.visited: list[Maze_Types.NodeId] = []
        self.adjacency_list = Solver_Base.create_adjacency_list(maze)
        self.solution_nodes = set()
    
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

        path = set()
        path.add(start)
        while end != start:
            path.add(end)
            end = solution[end]
        return path





