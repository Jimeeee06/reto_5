from ShapeI.point import Point
from ShapeI.line import Line

class Shape:
    def __init__(self, vertices: list[Point] = None, edges: list[Line] = None,
                  inner_angles: list[float] = None, is_regular: bool = None):
    # Initialize the shape with vertices, edges, inner angles and regularity as private attributes
        self.__vertices = vertices
        self.__edges = edges
        self.__inner_angles = inner_angles
        self.__is_regular = is_regular

    def get_vertices(self):
        return self.__vertices

    def set_vertices(self, verts: list[Point]):
        self.__vertices = verts

    def get_edges(self):
        return self.__edges

    def set_edges(self, lines: list[Line]):
        self.__edges = lines

    def get_inner_angles(self):
        return self.__inner_angles

    def set_inner_angles(self, angles: list[float]):
        self.__inner_angles = angles

    def get_is_regular(self):
        return self.__is_regular

    def set_is_regular(self, val: bool):
        self.__is_regular = val

    def compute_area(self):
        pass

    def compute_perimeter(self):
        pass

    def compute_inner_angles(self):
        pass
