from enum import Enum

class Maze_Types(Enum):
    Wall = 0
    Path = 1
    Start = 2
    End = 3
    EdgeSet = set[tuple[tuple[int,int],tuple[int,int]]]