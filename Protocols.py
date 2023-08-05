from typing import Protocol
from Maze_Types import Maze_Types

class Maze(Protocol):
    edges: Maze_Types.EdgeSet
    solution: Maze_Types.EdgeSet
    walls: Maze_Types.EdgeSet
    nodes: list[tuple[int,int]] # (j, i)
    height:int
    width:int

