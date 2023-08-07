from typing import Protocol
from Maze_Types import Maze_Types

class Maze(Protocol):
    edges: Maze_Types.EdgeSet
    paths: Maze_Types.EdgeSet
    walls: Maze_Types.EdgeSet
    nodes: list[Maze_Types.NodeId] # (j, i)
    height:int
    width:int

class Solver(Protocol):
    maze: Maze
    adjacency_list: dict[Maze_Types.NodeId, list[Maze_Types.NodeId]]
    solution_nodes: list[Maze_Types.NodeId]
    visited: list[Maze_Types.NodeId]

    def __init__(self, maze):
        # take the maze as part of the constructor
        pass

    def create_adjacency_list(self, maze: Maze) -> Maze_Types.AdjacencyList:
        # creates adjacency list from maze edges
        pass

    def solve(self) -> list[Maze_Types.NodeId]:
        # solves the maze, and returns self.solution_nodes as the path from start to end
        pass