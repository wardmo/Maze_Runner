from typing import Protocol
from Maze_Types import Maze_Types

class MazeContract(Protocol):
    edges: set[Maze_Types.Edge]
    paths: set[Maze_Types.Edge]
    nodes: list[Maze_Types.NodeId] # (j, i)
    height:int
    width:int

class Solver(Protocol):
    maze: MazeContract
    adjacency_list: dict[Maze_Types.NodeId, list[Maze_Types.NodeId]]
    visited: list[Maze_Types.NodeId]

    def __init__(self, maze):
        # take the maze as part of the constructor
        pass

    def create_adjacency_list(self, maze: MazeContract) -> Maze_Types.AdjacencyList:
        # creates adjacency list from maze edges
        pass