import unittest
from Maze import Maze
from Solver import Solve
from MazeVisualizer import MazeVisualizer
from Animator import ConcreteAnimator



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

    def test_StaticOriginShift(self):
        originshift = Maze.GenerateFromOriginShift(20,20)
        print('\n')
        print(MazeVisualizer(originshift))

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

    def test_AnimatorKruskal(self):
        animator = ConcreteAnimator()
        Maze.GenerateFromKruskal(40,40,animator=animator)
        animator.animate('kruskal.gif')

    def test_AnimatorPrims(self):
        animator = ConcreteAnimator()
        Maze.GenerateFromPrims(40,40, animator=animator)
        animator.animate('prims.gif')
    
    def test_AnimatorDFS(self):
        animator = ConcreteAnimator()
        Maze.GenerateFromDFS(40,40, animator=animator)
        animator.animate('dfs.gif')

    def test_AnimatorWilsons(self):
        animator = ConcreteAnimator()
        Maze.GenerateFromWilsons(40,40, animator=animator)
        animator.animate('wilsons.gif')

    def test_AnimatorOriginShift(self):
        animator = ConcreteAnimator()
        Maze.GenerateFromOriginShift(40,40, animator=animator)
        animator.animate('originshift.gif')

    def test_AnimatorSolveDFS(self):
        animator = ConcreteAnimator()
        krus = Maze.GenerateFromKruskal(40,40)
        Solve.SolveDFS(krus, animator=animator)
        animator.animate('krus_solve.gif')
    
    def test_AnimatorSolveBFS(self):
        animator = ConcreteAnimator()
        krus = Maze.GenerateFromKruskal(40,40)
        Solve.SolveBFS(krus, animator=animator)
        animator.animate('krus_solve_bfs.gif')

    def test_FullAnimation(self):
        animator1 = ConcreteAnimator()
        animator2 = ConcreteAnimator()
        wilson = Maze.GenerateFromWilsons(40,40)
        Solve.SolveDFS(wilson, animator=animator1)
        Solve.SolveBFS(wilson, animator=animator2)
        animator1.animate('wilson_solve_dfs.gif')
        animator2.animate('wilson_solve_bfs.gif')

    def test_WallFlowerSolver(self):
        animator = ConcreteAnimator()
        krus = Maze.GenerateFromPrims(10,10)
        Solve.SolveWallFlower(krus, animator=animator)
        animator.animate('wallflower.gif')