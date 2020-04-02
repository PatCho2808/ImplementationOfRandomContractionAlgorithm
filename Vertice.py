from Edge import *


class Vertice:

    def __init__(self, nr, edges):
        self.nr = nr
        self.edges = edges
        self.merges_vertices = []

    def create_edge(self, adjacent_vertice):
        if not self.get_is_adjacent(adjacent_vertice):
            new_edge = Edge(self, adjacent_vertice)
            adjacent_vertice.add_edge(new_edge)
            self.edges.append(new_edge)
            return new_edge
        else:
            return None

    def add_edge(self, edge):
        self.edges.append(edge)

    def get_is_adjacent(self, adjacent_vertice):
        for edge in self.edges:
            if edge.vertice_a == adjacent_vertice or edge.vertice_b == adjacent_vertice:
                return True
        return False

    def get_nr(self):
        return self.nr

    def add_merged_vertice(self, merged_vertice):
        self.merges_vertices.append(merged_vertice)

    def get_merged_vertices(self):
        return self.merges_vertices
