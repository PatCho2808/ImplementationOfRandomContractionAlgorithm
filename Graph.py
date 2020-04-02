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

    def get_are_vertices_adjacent(self, vertice_a, vertice_b):
        for edge in self.edges:
            if edge.get_vertice_a() == vertice_a or edge.get_vertice_a() == vertice_b:
                if edge.get_vertice_b() == vertice_a or edge.get_vertice_b() == vertice_b:
                    return True
        return False

    def merge_nodes(self, vertice_a, vertice_b):
        for edge in self.edges:
            edge.swap_vertice(vertice_b, vertice_a)
        vertice_a.add_merged_vertice(vertice_b)
        self.number_of_vertices = self.number_of_vertices - 1
        self.vertices.remove(vertice_b)


    def get_random_contraction(self):
        while self.get_nr_of_vertices() > 2:
            edge_to_contract = choice(self.edges)
            self.merge_nodes(edge_to_contract.get_vertice_a(), edge_to_contract.get_vertice_b())
            for edge in self.edges:
                if edge.get_is_self_loop():
                    self.edges.remove(edge)
        graph_cut = GraphCut()
        # return cut

    def get_vertice(self, nr_of_vertice):
        for vertice in self.vertices:
            if vertice.get_nr() == nr_of_vertice:
                return vertice
        return None




