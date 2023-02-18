from Maze_Types import Maze_Types

class Maze_square():

    def __init__(self, dim: int):
        self.content = [ [Maze_Types.Wall for i in range(dim)] for j in range(dim)]
        self.content[0][1] = Maze_Types.Start
        self.content[dim-1][dim-2] = Maze_Types.End
        # TODO assign randomize maze, but don't create any loops or cycles
        pass

    def __str__(self):
        return '\n'.join([''.join([chr(0x2588) if cell == Maze_Types.Wall else ' ' for cell in row]) for row in self.content])
        # a = []
        # for row in self.content:
        #     b = []
        #     for cell in row:
        #         b.append(chr(0x2588)) if cell == Maze_Types.Wall else b.append(' ') 
        #     a.append(''.join(b))
        # return '\n'.join(a)