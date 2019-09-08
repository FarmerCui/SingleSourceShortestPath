import sys

from interface import implements

from .vertex import Vertex
from .search_interface import SearchInterface


class DepthFirstSearch(implements(SearchInterface)):
    """ Depth first search class. """

    def __init__(self, graph: {}, start: int, end: int):
        """ initialize depth first search class """
        self.graph = graph
        self.start = start
        self.end = end
        self.vertices = {}

    def __init_vertices(self):
        """ initialize vertices """
        for vertex_id in self.graph.keys():
            self.vertices.setdefault(vertex_id, Vertex(vertex_id, sys.maxsize, None))
        self.vertices.get(self.start).dist = 0

    def __one_step_forward(self, cur_vertex) -> []:
        """ one step forward """
        new_vertices = []
        for (next_vertex_id, between_dist) in self.graph.get(cur_vertex.vertex_id).items():
            next_vertex = self.vertices.get(next_vertex_id)
            if not next_vertex.pred or next_vertex.dist > cur_vertex.dist + between_dist:
                next_vertex.dist = cur_vertex.dist + between_dist
                next_vertex.pred = cur_vertex
                new_vertices.append(next_vertex)
        return new_vertices

    def __get_solution(self) -> (int, []):
        """ get dist and travel """
        dist, travel = sys.maxsize, []
        end_vertex = self.vertices.get(self.end)
        if end_vertex.pred:
            dist = end_vertex.dist
            cur_vertex = end_vertex
            while cur_vertex.pred.vertex_id != self.start:
                travel.append((cur_vertex.pred.vertex_id, cur_vertex.vertex_id))
                cur_vertex = cur_vertex.pred
            travel.append((cur_vertex.pred.vertex_id, cur_vertex.vertex_id))
            travel.reverse()
        return dist, travel

    def search(self) -> (int, []):
        self.__init_vertices()
        cur_vertices = [self.vertices.get(self.start)]
        while cur_vertices:
            vertex = cur_vertices.pop()
            new_vertices = self.__one_step_forward(vertex)
            cur_vertices.extend(new_vertices)
        dist, travel = self.__get_solution()
        return dist, travel
