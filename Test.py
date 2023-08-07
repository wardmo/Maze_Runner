import unittest
from Kruskal_Generation import Kruskal_Generation
from Maze import Maze_Rep
from BFS import BFS


class Tests(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

    def test_square_maze(self):
        krus = Kruskal_Generation(3,3)
        rep = Maze_Rep(krus)
        print(rep)

    def test_unsquare_maze(self):
        krus = Kruskal_Generation(3,5)
        rep = Maze_Rep(krus)
        print(rep)

    def test_BFS(self):
        krus = Kruskal_Generation(3,5)
        bfs = BFS(krus)
        bfs.solve()