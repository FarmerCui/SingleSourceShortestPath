import unittest

from shortest_path import DijkstraSearch


class TestDijkstraSearch(unittest.TestCase):

    def test_search(self):
        self.graph = {0: {1: 6, 3: 18, 2: 8},
                      1: {4: 11},
                      2: {3: 9},
                      3: {},
                      4: {5: 3},
                      5: {3: 4, 2: 7}
                      }
        self.start = 0
        self.end = 5
        dijkstra = DijkstraSearch(self.graph, self.start, self.end)
        dist, travel = dijkstra.search()
        self.assertEqual(dist, 20)
        self.assertEqual(travel, [(0, 1), (1, 4), (4, 5)])
