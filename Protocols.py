from typing import Protocol
from Maze_Types import Maze_Types

class MazeContract(Protocol):
    edges: set[Maze_Types.Edge]
    paths: set[Maze_Types.Edge]
    nodes: list[Maze_Types.NodeId] # (j, i)
    height:int
    width:int

class Solver(Protocol):

    def create_adjacency_list(self, maze: MazeContract) -> Maze_Types.AdjacencyList:
        # creates adjacency list from maze edges
        pass