class Edge:

    def __init__(self, a, b):
        self.vertice_a = a
        self.vertice_b = b

    def get_has_vertice(self, vertice):
        return self.vertice_a == vertice or self.vertice_b == vertice

    def swap_vertice(self, old_vertice, new_vertice):
        if self.vertice_a == old_vertice:
            self.vertice_a = new_vertice
        elif self.vertice_b == old_vertice:
            self.vertice_b = new_vertice

    def get_is_self_loop(self):
        return self.vertice_a == self.vertice_b

