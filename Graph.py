from Vertice import *
from random import choice
from GraphCut import *


class Graph:

    def __init__(self, array):
        self.number_of_vertices = 0
        self.vertices = []
        self.edges = []
        for row in array:
            self.number_of_vertices = self.number_of_vertices + 1
            new_vertice = Vertice(self.number_of_vertices, [])
            self.vertices.append(new_vertice)
        for vertice in self.vertices:
            row = array[vertice.get_nr()-1]
            for nr_of_adjacent_vertice in row[1:]:
                new_edge = vertice.create_edge(self.vertices[nr_of_adjacent_vertice - 1])
                if new_edge:
                    self.edges.append(new_edge)

    def get_nr_of_edges(self):
        return len(self.edges)

    def get_nr_of_vertices(self):
        return self.number_of_vertices

    def get_are_vertices_adjacent(self, a, b):
        for edge in self.edges:
            if edge.vertice_a == a or edge.vertice_a == b:
                if edge.vertice_b == a or edge.vertice_b == b:
                    return True
        return False

    def merge_nodes(self, a, b):
        for edge in self.edges:
            edge.swap_vertice(b, a)
        a.add_merged_vertices(b)


    def get_random_contraction(self):
        if self.get_nr_of_vertices() > 2:
            edge_to_contract = choice(self.edges)
            self.merge_nodes(edge_to_contract.vertice_a, edge_to_contract.vertice_b)
            for edge in self.edges:
                if edge.get_is_self_loop():
                    self.edges.remove(edge)
        # return cut

    def get_vertice(self, nr_of_vertice):
        return self.vertices[nr_of_vertice - 1]




