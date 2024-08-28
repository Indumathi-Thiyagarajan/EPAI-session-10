import math

class Polygon:
    def __init__(self, vertices, circumradius):
        self.vertices = vertices
        self.circumradius = circumradius

    @property
    def edges(self):
        return self.vertices

    @property
    def interior_angle(self):
        return (self.vertices - 2) * 180 / self.vertices

    @property
    def edge_length(self):
        return 2 * self.circumradius * math.sin(math.pi / self.vertices)

    @property
    def apothem(self):
        return self.circumradius * math.cos(math.pi / self.vertices)

    @property
    def area(self):
        return 0.5 * self.vertices * self.edge_length * self.apothem

    @property
    def perimeter(self):
        return self.vertices * self.edge_length

    @property
    def efficiency(self):
        return self.area / self.perimeter

    def __repr__(self):
        return (f'Polygon(vertices={self.vertices}, circumradius={self.circumradius}, '
                f'edge_length={self.edge_length:.2f}, apothem={self.apothem:.2f}, '
                f'area={self.area:.2f}, perimeter={self.perimeter:.2f})')

    def __eq__(self, other):
        if isinstance(other, Polygon):
            return self.vertices == other.vertices and self.circumradius == other.circumradius
        return False

    def __gt__(self, other):
        if isinstance(other, Polygon):
            return self.vertices > other.vertices
        return False

class PolygonSequence:
    def __init__(self, max_vertices, circumradius):
        self.max_vertices = max_vertices
        self.circumradius = circumradius
        self._polygons = [Polygon(i, circumradius) for i in range(3, max_vertices + 1)]

    def __len__(self):
        return len(self._polygons)

    def __getitem__(self, s):
        return self._polygons[s]

    @property
    def max_efficiency_polygon(self):
        return max(self._polygons, key=lambda p: p.efficiency)

    def __repr__(self):
        return (f'PolygonSequence(max_vertices={self.max_vertices}, circumradius={self.circumradius}, '
                f'polygons={len(self._polygons)})')