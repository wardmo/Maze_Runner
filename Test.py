import unittest
from Maze import Maze
from Solver import Solve
from MazeVisualizer import MazeVisualizer



class Tests(unittest.TestCase):

    def test_StaticGeneration(self):
        krus = Maze.GenerateFromKruskal(3,5)
        print('\n')
        print(MazeVisualizer(krus))

    def test_StaticPrims(self):
        prim = Maze.GenerateFromPrims(5,5)
        print('\n')
        print(MazeVisualizer(prim))

    def test_StaticDFS(self):
        dfs = Maze.GenerateFromDFS(5,5)
        print('\n')
        print(MazeVisualizer(dfs))

    def test_StaticWilson(self):
        wilson = Maze.GenerateFromWilsons(5,5)
        print('\n')
        print(MazeVisualizer(wilson))

    def test_SolveDFS(self):
        prim = Maze.GenerateFromPrims(5,5)
        solution = Solve.SolveDFS(prim)
        print('\n')
        print(MazeVisualizer(prim, solution_nodes=solution))

    def test_SolveBFS(self):
        prim = Maze.GenerateFromPrims(5,5)
        solution = Solve.SolveBFS(prim)
        print('\n')
        print(MazeVisualizer(prim, solution_nodes=solution))

    def test_SolveBigger(self):
        krus = Maze.GenerateFromKruskal(14,40)
        solution = Solve.SolveDFS(krus)
        print('\n')
        print(MazeVisualizer(krus, solution_nodes=solution))