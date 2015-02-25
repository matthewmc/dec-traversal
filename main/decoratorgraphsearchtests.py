import unittest
from inttrav import *

class Letter():
    def __init__(self, name):
        self.letter = name
        self.children = []

class DecoratorGraphTraversalTest(unittest.TestCase):
    """
    Graph has form:

    a <------------|
    | \  \         |
    b c  f         |
      |\/ \        |
      d e  g<---|  |
         \/ \___|  |
          h        |
           \_______|
    """

    def setUp(self):
        self.a = Letter('a')
        self.b = Letter('b')
        self.c = Letter('c')
        self.d = Letter('d')
        self.e = Letter('e')
        self.f = Letter('f')
        self.g = Letter('g')
        self.h = Letter('h')
        self.a.children = [self.b, self.c, self.f]
        self.c.children = [self.d, self.e]
        self.f.children = [self.e, self.g]
        self.e.children = [self.h]
        self.g.children = [self.g, self.h]
        self.h.children = [self.a]

    def test_prioritize(self):
        pass

    def test_bfs_path(self):
        @bfs
        def get_path(Node, **kwargs):
            kwargs['res'].append(Node.letter)
            return True

        results = []
        get_path(self.a, res=results)
        results = ''.join(results)
        self.assertEqual('abcfdegh', results)

    def test_dfs_path(self):
        pass


if __name__ == '__main__':
    unittest.main()