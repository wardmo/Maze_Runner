from MazeVisualizer import MazeVisualizer
from Protocols import Animator, MazeContract
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
        self.frames:list[MazeContract] = list()

    def save_frame(self, maze:MazeContract) -> None:
        self.frames.append(maze)

    def animate(self, filename:str) -> None:
        images:list[Image] = list()
        for frame in self.frames:
            images.append(MazeVisualizer(frame).save_img())
        images[0].save(filename, save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)