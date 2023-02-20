from enum import Enum

class Maze_Types(Enum):
    Wall = 0
    Path = 1
    Start = 2
    End = 3

class Maze_Node():
    def __init__(self, id: tuple[int,int]):
        self.data = None
        self.id: tuple[int,int] = id
        self.connected_nodes: list[Maze_Node] = []

class Maze_Edge():
    def __init__(self, id: tuple[tuple[int,int], tuple[int,int]]):
        self.type: Maze_Types = Maze_Types.Wall
        self.id: tuple[tuple[int,int], tuple[int,int]] = id
        self.reverse_id: tuple[tuple[int,int],tuple[int,int]] = (id[1],id[0])