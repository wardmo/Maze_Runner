from Maze_Types import Maze_Types
from Protocols import Maze
from PIL import Image
import numpy as np

class Maze_Rep():

    def __init__(self, maze: Maze, solution_nodes=set()):
        wall = Maze_Types.Wall
        path = Maze_Types.Path
        rep = [[wall for i in range(2*maze.width+1)] for j in range(2*maze.height+1)]
        rep[0][1] = Maze_Types.Start
        rep[-1][-2] = Maze_Types.End
        for node in maze.nodes:
            j,i = node
            repj = 2*j+1
            repi = 2*i+1
            if node in solution_nodes:
                rep[repj][repi] = Maze_Types.Solution
            else:
                rep[repj][repi] = path
        for edge in maze.paths:
            n1, n2 = edge
            j,i = n1
            jj,ii = n2
            edgej = 2*j+1
            edgei = 2*i+1
            if i == ii:
                edgej = 2*min(j,jj)+2
                if n1 in solution_nodes and n2 in solution_nodes:
                    rep[edgej][edgei] = Maze_Types.Solution
                else:
                    rep[edgej][edgei] = path
            elif j == jj:
                edgei = 2*min(i,ii)+2
                if n1 in solution_nodes and n2 in solution_nodes:
                    rep[edgej][edgei] = Maze_Types.Solution
                else:
                    rep[edgej][edgei] = path

        self.content = rep



        pass

    def set_solution(self, solution_nodes):
        for node in solution_nodes:
            j,i = node
            repj = 2*j+1
            repi = 2*i+1
            self.content[repj][repi] = Maze_Types.Solution
            adj_nodes = {
                (j,i+1), (j,i-1), (j-1,i), (j+1,i)
            }
            for adj_node in adj_nodes:
                if adj_node in solution_nodes:
                    jj,ii = adj_node
                    if ii == i:
                        newrepj = 2*min(j,jj)+2
                        if self.content[newrepj][repi] == Maze_Types.Path:
                            self.content[newrepj][repi] = Maze_Types.Solution
                    elif jj == j:
                        newrepi = 2*min(i,ii)+2
                        if self.content[repj][newrepi] == Maze_Types.Path:
                            self.content[repj][newrepi] = Maze_Types.Solution

    def save_img(self, name):

        array = np.array([[Maze_Rep.get_pixel_on_type(cell) for cell in row] for row in self.content], dtype=np.uint8)

        new_image = Image.fromarray(array)
        new_image.save(name)



    @staticmethod
    def get_pixel_on_type(cell):
        if cell == Maze_Types.Wall:
            return (0,0,0)
        elif cell == Maze_Types.Solution:
            return (245,56,56)
        elif cell == Maze_Types.Start or cell == Maze_Types.End:
            return (56,245,56)
        else:
            return (250,250,250)

    @staticmethod
    def get_ascii_block(text, color, width=1):

        # The ANSI escape codes for the different colors.
        ANSI_COLORS = {
            "red": "\033[31m",
            "green": "\033[32m",
            "blue": "\033[34m",
            "reset": "\033[39m"
        }

        # Print the colored block.
        return f"{ANSI_COLORS[color]}{text:^{width}}{ANSI_COLORS['reset']}"
    
    @staticmethod
    def get_char_on_type(cell):
        if cell == Maze_Types.Wall:
            return chr(0x2588)*2
        elif cell == Maze_Types.Solution:
            return Maze_Rep.get_ascii_block(chr(0x2588)*2, 'red')
        elif cell == Maze_Types.Start or cell == Maze_Types.End:
            return Maze_Rep.get_ascii_block(chr(0x2588)*2, 'green')
        else:
            return '  '

    def __str__(self):

        return '\n'.join([''.join([Maze_Rep.get_char_on_type(cell) for cell in row]) for row in self.content])