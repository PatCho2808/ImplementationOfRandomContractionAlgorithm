class GraphCut:

    def __init__(self, vertices_a, vertices_b, edges):
        self.vertices_a = vertices_a
        self.vertices_b = vertices_b
        self.edges = edges

    def get_nr_of_edges(self):
        return len(self.edges)

