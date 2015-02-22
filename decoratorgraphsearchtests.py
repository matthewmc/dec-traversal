import unittest
from inttrav import *


class DecoratorGraphTraversalTest(unittest.TestCase):
    
    def setUp(self):
    a = Letter('a')
    b = Letter('b')
    c = Letter('c')
    d = Letter('d')
    e = Letter('e')
    f = Letter('f')
    g = Letter('g')
    h = Letter('h')
    a.children = [b, c, f]
    c.children = [d, e]
    f.children = [e, g]
    e.children = [h]
    g.children = [g, h]

    def test_bfs(self):


if __name__ == '__main__':
    unittest.main()