import unittest
from inttrav import *

class Letter():
    def __init__(self, name):
        self.letter = name
        self.children = []

class genericNode():
    def __init__(self):
        pass

class DecoratorGraphTraversalTest(unittest.TestCase):
    """
    Graph:

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

        self.neighbor1 = genericNode()
        self.neighbor2 = genericNode()
        self.neighbor3 = genericNode()

        # Generic node with a list holding neighbors
        self.list_ = genericNode()
        self.list_.neighbors = [self.neighbor1, 
                                self.neighbor2, 
                                self.neighbor3]

        # Node with a dict holding neighbors.
        self.dict_ = genericNode()
        self.dict_.neighbors = {'1' : self.neighbor1, 
                                '2' : self.neighbor2, 
                                '3' : self.neighbor3}

        # Node with neighbors as attributes.
        self.attrs = genericNode()
        self.attrs.attr1 = self.neighbor1
        self.attrs.attr2 = self.neighbor2
        self.attrs.attr3 = self.neighbor3

    def test_prioritize(self):
        def equal(list1, list2):
            set1 = set()
            set2 = set()
            for item in list1:
                set1.add(item)
            for item in list2:
                set2.add(item)
            if set1 == set2:
                return True
            elif set1 != set2:
                return False

        list_neighs = prioritize(self.list_)
        dict_neighs = prioritize(self.dict_)
        attrs_neighs = prioritize(self.attrs)
        control = [self.neighbor1, 
                   self.neighbor2, 
                   self.neighbor3]

        self.assertEqual(equal(list_neighs, control), True)
        self.assertEqual(equal(dict_neighs, control), True)
        self.assertEqual(equal(attrs_neighs, control), True)

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
        @dfs
        def get_path(Node, **kwargs):
            kwargs['res'].append(Node.letter)
            return True

        results = []
        get_path(self.a, res=results)
        results = ''.join(results)
        self.assertEqual('abcdehfg', results)


if __name__ == '__main__':
    unittest.main()