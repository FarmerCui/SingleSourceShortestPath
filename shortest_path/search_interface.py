from interface import Interface


class SearchInterface(Interface):
    def __init__(self, graph: {}, start: int, end: int):
        pass

    def search(self) -> (int, []):
        pass
