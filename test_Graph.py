from unittest import TestCase
from Graph import *
from GraphCut import *


class TestGraph(TestCase):
    def test_creating_graph(self):
        graph = Graph([[1, 5, 7],
                       [2, 3, 5],
                       [3, 2, 4, 5],
                       [4, 6, 3],
                       [5, 2, 3, 6],
                       [6, 4, 5],
                       [7, 1]])
        self.assertEqual(8, graph.get_nr_of_edges())
        self.assertEqual(7, graph.get_nr_of_vertices())

        self.assertTrue(graph.get_are_vertices_adjacent(graph.get_vertice(1), graph.get_vertice(7)))
        self.assertTrue(graph.get_are_vertices_adjacent(graph.get_vertice(4), graph.get_vertice(6)))

        self.assertFalse(graph.get_are_vertices_adjacent(graph.get_vertice(1), graph.get_vertice(2)))
        self.assertFalse(graph.get_are_vertices_adjacent(graph.get_vertice(4), graph.get_vertice(5)))

        graph = Graph([[1, 2, 5],
                       [2, 5, 4],
                       [3, 4],
                       [4, 2, 3],
                       [5, 1, 2]])
        self.assertEqual(5, graph.get_nr_of_edges())
        self.assertEqual(5, graph.get_nr_of_vertices())

        self.assertTrue(graph.get_are_vertices_adjacent(graph.get_vertice(1), graph.get_vertice(2)))
        self.assertTrue(graph.get_are_vertices_adjacent(graph.get_vertice(2), graph.get_vertice(4)))

        self.assertFalse(graph.get_are_vertices_adjacent(graph.get_vertice(1), graph.get_vertice(4)))
        self.assertFalse(graph.get_are_vertices_adjacent(graph.get_vertice(5), graph.get_vertice(3)))

    def test_merge_nodes(self):
        graph = Graph([[1, 2, 5],
                       [2, 5, 4],
                       [3, 4],
                       [4, 2, 3],
                       [5, 1, 2]])

        graph.merge_nodes(graph.get_vertice(1), graph.get_vertice(2))

        self.assertEqual(None, graph.get_vertice(2))

        self.assertTrue(graph.get_are_vertices_adjacent(graph.get_vertice(1), graph.get_vertice(1)))
        self.assertTrue(graph.get_are_vertices_adjacent(graph.get_vertice(1), graph.get_vertice(4)))
        self.assertTrue(graph.get_are_vertices_adjacent(graph.get_vertice(1), graph.get_vertice(5)))

        graph = Graph([[1, 5, 7],
                       [2, 3, 5],
                       [3, 2, 4, 5],
                       [4, 6, 3],
                       [5, 2, 3, 6],
                       [6, 4, 5],
                       [7, 1]])

        self.assertTrue(graph.get_are_vertices_adjacent(graph.get_vertice(2), graph.get_vertice(5)))
        self.assertTrue(graph.get_are_vertices_adjacent(graph.get_vertice(2), graph.get_vertice(3)))

        self.assertFalse(graph.get_are_vertices_adjacent(graph.get_vertice(1), graph.get_vertice(3)))

        graph.merge_nodes(graph.get_vertice(1), graph.get_vertice(2))

        self.assertEqual(None, graph.get_vertice(2))

        self.assertTrue(graph.get_are_vertices_adjacent(graph.get_vertice(1), graph.get_vertice(3)))

    def test_random_contraction(self):
        graph = Graph([[1, 2, 3],
                       [2, 1, 3],
                       [3, 1, 2, 4],
                       [4, 3]])
        graph_cut = graph.get_random_contraction()

        self.assertTrue(graph_cut.get_nr_of_edges() > 0)

        vertices = graph_cut.get_numbers_of_vertices_a() + graph_cut.get_numbers_of_vertices_b()
        vertices.sort()

        self.assertEqual([1, 2, 3, 4], vertices)

        graph = Graph([[1, 2],
                       [2, 1, 3],
                       [3, 2]])

        graph_cut = graph.get_random_contraction()

        self.assertTrue(graph_cut.get_nr_of_edges() > 0)

        vertices = graph_cut.get_numbers_of_vertices_a() + graph_cut.get_numbers_of_vertices_b()
        vertices.sort()

        self.assertEqual([1, 2, 3], vertices)

        graph = Graph([[1, 2, 5],
                       [2, 1, 3, 4],
                       [3, 2, 4],
                       [4, 3, 2],
                       [5, 1]])

        graph_cut = graph.get_random_contraction()

        self.assertTrue(graph_cut.get_nr_of_edges() > 0)

        vertices = graph_cut.get_numbers_of_vertices_a() + graph_cut.get_numbers_of_vertices_b()
        vertices.sort()

        self.assertEqual([1, 2, 3, 4, 5], vertices)


class TestMinContraction(TestCase):
    def test_get_smallest_contraction(self):
        graph = Graph([[1, 2, 5, 4],
                       [2, 1, 3, 4],
                       [3, 2, 4],
                       [4, 3, 2, 1],
                       [5, 1]])

        graph_cut = graph.get_min_contraction()

        self.assertEqual(1, graph_cut.get_nr_of_edges())

        vertices_a = graph_cut.get_numbers_of_vertices_a()
        vertices_b = graph_cut.get_numbers_of_vertices_b()
        self.assertTrue([5] == vertices_a or [5] == vertices_b)

        graph = Graph([[1, 2, 6],
                       [2, 2, 6, 3],
                       [3, 2, 6, 4],
                       [4, 3, 6, 5],
                       [5, 4, 6],
                       [6, 4, 5, 3, 2, 1]])

        graph_cut = graph.get_min_contraction()

        self.assertEqual(2, graph_cut.get_nr_of_edges())

        vertices_a = graph_cut.get_numbers_of_vertices_a()
        vertices_b = graph_cut.get_numbers_of_vertices_b()
        self.assertTrue([1] == vertices_a or [1] == vertices_b or [5] == vertices_a or [5] == vertices_b)
