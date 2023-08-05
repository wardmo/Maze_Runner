from Maze_Types import Maze_Types
from Protocols import Maze

class Maze_Rep():

    def __init__(self, maze: Maze):
        wall = Maze_Types.Wall
        path = Maze_Types.Path
        rep = [[wall for i in range(2*maze.width+1)] for j in range(2*maze.height+1)]
        for node in maze.nodes:
            j,i = node
            rep[2*j+1][2*i+1] = path
        for edge in maze.solution:
            n1, n2 = edge
            j,i = n1
            jj,ii = n2
            if i == ii:
                rep[2*min(j,jj)+2][2*i+1] = path
            elif j == jj:
                rep[2*j+1][2*min(i,ii)+2] = path

        self.content = rep



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