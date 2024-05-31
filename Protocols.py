from typing import Protocol
from Maze_Types import Maze_Types

class MazeContract(Protocol):
    edges: set[Maze_Types.Edge]
    paths: set[Maze_Types.Edge]
    nodes: set[Maze_Types.NodeId] # (j, i)
    height:int
    width:int

class Solver(Protocol):

    def create_adjacency_list(self, maze: MazeContract) -> Maze_Types.AdjacencyList:
        # creates adjacency list from maze edges
        pass

class Animator(Protocol):
    frames:list[MazeContract]
    def save_frame(self, maze:MazeContract, solution_nodes:set[Maze_Types.NodeId]=set()) -> None:
        # appends maze state to list of maze states to stitch together and animate
        pass
    def animate(self, filename:str) -> None:
        # saves gif of animation to filename
        pass