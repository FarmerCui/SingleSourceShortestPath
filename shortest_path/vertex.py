class Vertex(object):
    def __init__(self, vertex_id, dist, pred):
        self.vertex_id = vertex_id
        self.dist = dist
        self.pred = pred
