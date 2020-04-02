from unittest import TestCase
from Graph import *


class TestGraph(TestCase):
    def test_graph(self):
        graph = Graph([[1, 5, 7],
                       [2, 3, 5],
                       [3, 2, 4, 5],
                       [4, 6, 3],
                       [5, 2, 3, 6],
                       [6, 4, 5],
                       [7, 1]])
        self.assertEqual(8, graph.get_nr_of_edges())
        self.assertEqual(7, graph.get_nr_of_vertices())

        self.assertTrue(graph.get_are_vertices_adjacent(1, 7))
        self.assertTrue(graph.get_are_vertices_adjacent(4, 6))

        self.assertFalse(graph.get_are_vertices_adjacent(1, 2))
        self.assertFalse(graph.get_are_vertices_adjacent(4, 5))

        graph = Graph([[1, 2, 5],
                       [2, 5, 4],
                       [3, 4],
                       [4, 2, 3],
                       [5, 1, 2]])
        self.assertEqual(5, graph.get_nr_of_edges())
        self.assertEqual(5, graph.get_nr_of_vertices())

        self.assertTrue(graph.get_are_vertices_adjacent(1, 2))
        self.assertTrue(graph.get_are_vertices_adjacent(2, 4))

        self.assertFalse(graph.get_are_vertices_adjacent(1, 4))
        self.assertFalse(graph.get_are_vertices_adjacent(5, 3))

    def test_merge_nodes(self):
        graph = Graph([[1, 2, 5],
                       [2, 5, 4],
                       [3, 4],
                       [4, 2, 3],
                       [5, 1, 2]])

        graph.merge_nodes(1, 2)

        self.assertFalse(graph.get_are_vertices_adjacent(2, 5))
        self.assertFalse(graph.get_are_vertices_adjacent(2, 4))

        self.assertTrue(graph.get_are_vertices_adjacent(1, 1))
        self.assertTrue(graph.get_are_vertices_adjacent(1, 4))
        self.assertTrue(graph.get_are_vertices_adjacent(1, 5))

        graph = Graph([[1, 5, 7],
                       [2, 3, 5],
                       [3, 2, 4, 5],
                       [4, 6, 3],
                       [5, 2, 3, 6],
                       [6, 4, 5],
                       [7, 1]])

        self.assertTrue(graph.get_are_vertices_adjacent(graph.get_vertice(2), 5))
        self.assertTrue(graph.get_are_vertices_adjacent(2, 3))

        self.assertFalse(graph.get_are_vertices_adjacent(1, 3))

        graph.merge_nodes(1, 2)

        self.assertFalse(graph.get_are_vertices_adjacent(2, 5))
        self.assertFalse(graph.get_are_vertices_adjacent(2, 3))

        self.assertTrue(graph.get_are_vertices_adjacent(1, 3))