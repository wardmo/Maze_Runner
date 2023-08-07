from enum import Enum

class Maze_Types(Enum):
    Wall = 0
    Path = 1
    Start = 2
    End = 3
    Solution = 4
    EdgeSet = set[tuple[tuple[int,int],tuple[int,int]]]
    NodeId = tuple[int,int]
    Edge = tuple[tuple[int,int],tuple[int,int]]
    AdjacencyList = dict[NodeId, set[NodeId]]