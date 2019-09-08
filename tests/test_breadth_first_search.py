import unittest

from shortest_path import BreadthFirstSearch


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
        bfs = BreadthFirstSearch(self.graph, self.start, self.end)
        dist, travel = bfs.search()
        self.assertEqual(dist, 20)
        self.assertEqual(travel, [(0, 1), (1, 4), (4, 5)])
