import unittest

from shortest_path import DepthFirstSearch


class TestFoo(unittest.TestCase):

    def test_foo_name(self):
        self.graph = {0: {1: 6, 3: 18, 2: 8},
                      1: {4: 11},
                      2: {3: 9},
                      3: {},
                      4: {5: 3},
                      5: {3: 4, 2: 7}
                      }
        self.start = 0
        self.end = 5
        dfs = DepthFirstSearch(self.graph, self.start, self.end)
        dist, travel = dfs.search()
        self.assertEqual(dist, 20)
        self.assertEqual(travel, [(0, 1), (1, 4), (4, 5)])
