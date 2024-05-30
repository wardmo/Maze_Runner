from enum import Enum

class Maze_Types(Enum):
    Wall = 0
    Path = 1
    Start = 2
    End = 3
    Solution = 4
    NodeId = tuple[int,int]
    Edge = tuple[NodeId,NodeId]
    AdjacencyList = dict[NodeId, set[NodeId]]