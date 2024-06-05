from MazeVisualizer import MazeVisualizer
from Protocols import Animator, MazeContract
from Maze_Types import Maze_Types as MAZE
from PIL.Image import Image

class NullAnimator(Animator):
    def __init__(self) -> None:
        self.frames:list[MazeContract] = list()
    
    def save_frame(self, maze:MazeContract) -> None:
        pass

    def animate(self, filename:str) -> None:
        pass

class ConcreteAnimator(Animator):
    def __init__(self) -> None:
        self.frames:list[tuple[MazeContract, set[MAZE.NodeId]]] = list()

    def save_frame(self, maze:MazeContract, solution_nodes:set[MAZE.NodeId]=set()) -> None:
        self.frames.append((maze,solution_nodes))

    def animate(self, filename:str) -> None:
        images:list[Image] = list()
        for frame, solution_nodes in self.frames:
            images.append(MazeVisualizer(frame, solution_nodes=solution_nodes).save_img())
        images[0].save(filename, save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)
