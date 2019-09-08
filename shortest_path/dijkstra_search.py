import sys

from interface import implements

from .vertex import Vertex
from .search_interface import SearchInterface


class DijkstraSearch(implements(SearchInterface)):
    """ Dijkstra first search class. """

    def __init__(self, graph: {}, start: int, end: int):
        """ initialize dijkstra first search class """
        self.graph = graph
        self.start = start
        self.end = end
        self.vertices = {}
        self.solid_vertices = {}

    def __init_vertices(self):
        """ initialize vertices """
        for vertex_id in self.graph.keys():
            self.vertices.setdefault(vertex_id, Vertex(vertex_id, sys.maxsize, None))
        self.vertices.get(self.start).dist = 0

    def relex(self, vertex: Vertex, sibling: Vertex) -> bool:
        change = False
        sub_dist = self.graph.get(vertex.vertex_id).get(sibling.vertex_id)
        if sibling.dist > vertex.dist + sub_dist:
            sibling.dist = vertex.dist + sub_dist
            sibling.pred = vertex
            change = True
        return change

    def __one_step_forward(self, cur_vertices: []) -> [Vertex]:
        """ one step forward """
        new_vertices = []
        while cur_vertices:
            vertex, dist = cur_vertices.pop()
            if vertex in self.vertices:
                self.vertices.pop(vertex.vertex_id)
            self.solid_vertices.setdefault(vertex.vertex_id, vertex)
            for sibling_id, sub_dist in self.graph.get(vertex.vertex_id).items():
                if sibling_id in self.solid_vertices:
                    sibling = self.solid_vertices.get(sibling_id)
                    change = self.relex(vertex, sibling)
                    if change:
                        new_vertices.append((sibling, sub_dist))
                else:
                    sibling = self.vertices.get(sibling_id)
                    sibling.dist = vertex.dist + sub_dist
                    sibling.pred = vertex
                    new_vertices.append((sibling, sub_dist))
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
        cur_vertices_info = [(vertex_id, dist) for (vertex_id, dist) in self.graph.get(self.start).items()]
        cur_vertices_info.sort(key=lambda item: -item[1])
        start_vertex = self.vertices.pop(self.start)
        cur_vertices = [(self.vertices.get(vid), dist) for vid, dist in cur_vertices_info]
        for vertex, dist in cur_vertices:
            vertex.pred = start_vertex
            vertex.dist = start_vertex.dist + self.graph.get(start_vertex.vertex_id).get(vertex.vertex_id)
        while cur_vertices:
            new_vertices = self.__one_step_forward(cur_vertices)
            cur_vertices = new_vertices if new_vertices else None
        dist, travel = self.__get_solution()
        return dist, travel
