from math import acos, asin, degrees

class Point:
    def __init__(self, x=0, y=0):
        # Initialize the point with x and y coordinates as private attributes
        self.__x = x
        self.__y = y

    def compute_distance(self, point: "Point"):
        delta_x = self.get_x() - point.get_x()
        delta_y = self.get_y() - point.get_y()
        return (delta_x ** 2 + delta_y ** 2) ** 0.5
    
    def get_x(self):
        return self.__x

    def set_x(self, val):
        self.__x = val

    def get_y(self):
        return self.__y

    def set_y(self, val):
        self.__y = val
    
    def __str__(self):
        return f"({self.__x}, {self.__y})"

class Line:
    def __init__(self, length: float = 0, start: Point = None, end: Point = None):
    # Initialize the line with length, start and end points as private attributes
        self.__length = length
        self.__start = start
        self.__end = end
    
    def get_start(self):
        return self.__start

    def set_start(self, p: Point):
        self.__start = p

    def get_end(self):
        return self.__end

    def set_end(self, p: Point):
        self.__end = p
    
    def set_length(self, val: float):
        self.__length = val

    def get_length(self):
        # Calculate the length of the line using the distance formula
        dx = self.__end.get_x() - self.__start.get_x()
        dy = self.__end.get_y() - self.__start.get_y()
        self.set_length((dx**2 + dy**2)**0.5)
        return self.__length

#Superclass Shape
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

#Derived classes from Shape
class Triangle(Shape):
    def __init__(self, vertices, edges, inner_angles, is_regular):
        super().__init__(vertices, edges, inner_angles, is_regular)

    def compute_perimeter(self):
        a, b, c = (edge.get_length() for edge in self.get_edges())
        return a + b + c
    def compute_area(self):
        # Use Heron's formula to calculate the area of any triangle
        a, b, c = sorted(edge.get_length() for edge in self.get_edges())
        s = self.compute_perimeter() / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area

class Rectangle(Shape):
    def __init__(self, vertices, edges, inner_angles, is_regular):
        super().__init__(vertices, edges, inner_angles, is_regular)
        self.set_is_regular(is_regular)

    def compute_area(self):    
        a, b, c, d = sorted(edge.get_length() for edge in self.get_edges())
        return a * d
    
    def compute_perimeter(self):
        a, b, c, d = sorted(edge.get_length() for edge in self.get_edges())
        return a + b + c + d
    
    def compute_inner_angles(self):
        # All angles in a rectangle are 90 degrees
        angles = [90, 90, 90, 90]
        self.set_inner_angles(angles)
        return angles
    
    def is_regular(self):
        a, b, c, d = [edge.get_length() for edge in self.get_edges()]
        return a == b == c == d

#Derived classes from Triangle  
class Isosceles(Triangle):
    def __init__(self, vertices, edges, inner_angles, is_regular):
        super().__init__(vertices, edges, inner_angles, is_regular)
        self.set_is_regular(False)
        # Set the base and same sides of the isosceles triangle
        a, b, c = (edge.get_length() for edge in self.get_edges())
        if a == b:
            self._base, self._same = c, a
        elif b == c:
            self._base, self._same = a, b
        else:
            self._base, self._same = b, a

    def compute_area(self):
        return super().compute_area()
    
    def compute_perimeter(self):
        return super().compute_perimeter()
    
    def compute_inner_angles(self):
        # Calculate the angles of the isosceles triangle
        # using the law of cosines
        angle_1 = degrees(acos(1-((self._base**2)/(2*self._same**2))))
        angle_2 = angle_3 = (180 - angle_1) / 2
        angles = [angle_1, angle_2, angle_3]
        self.set_inner_angles(angles)
        return angles

class Equilateral(Triangle):
    def __init__(self, vertices, edges, inner_angles, is_regular):
        super().__init__(vertices, edges, inner_angles, is_regular)
        # Set the triangle as regular
        self.set_is_regular(True)

    def compute_area(self):
        return super().compute_area()
    
    def compute_perimeter(self):
        return super().compute_perimeter()
    
    def compute_inner_angles(self):
        # All angles in an equilateral triangle are 60 degrees
        angles = [60, 60, 60]
        self.set_inner_angles(angles)
        return angles

class Scalene(Triangle):
    def __init__(self, vertices, edges, inner_angles, is_regular):
        super().__init__(vertices, edges, inner_angles, is_regular)
        self.set_is_regular(False)

    def compute_area(self):
        return super().compute_area()
    
    def compute_perimeter(self):
        return super().compute_perimeter()
    
    def compute_inner_angles(self):
        # Calculate the angles of the scalene triangle
        # using the law of cosines
        a, b, c = sorted(edge.get_length() for edge in self.get_edges())
        angle_1 = degrees(acos((b**2 + c**2 - a**2)/(2 * b *  c)))
        angle_2 = degrees(acos((a**2 + c**2 - b**2)/(2 * a * c)))
        angle_3 = 180 - angle_1 - angle_2
        angles = [angle_1, angle_2, angle_3]
        self.set_inner_angles(angles)
        return angles

class TriRectangle(Triangle):
    def __init__(self, vertices, edges, inner_angles, is_regular):
        super().__init__(vertices, edges, inner_angles, is_regular)
        self.set_is_regular(False)

    def compute_area(self):
        return super().compute_area()
    
    def compute_perimeter(self):
        return super().compute_perimeter()
    
    def compute_inner_angles(self):
        # Calculate the angles of the right triangle
        # using the law of sines
        a, b, c = sorted(edge.get_length() for edge in self.get_edges())
        angle_1 = 90
        angle_2 = degrees(asin(a / c))
        angle_3 = 180 - angle_1 - angle_2
        angles = [angle_1, angle_2, angle_3]
        self.set_inner_angles(angles)
        return angles

#Derived classes from Rectangle 
class Square(Rectangle):
    def __init__(self, vertices, edges, inner_angles, is_regular):
        super().__init__(vertices, edges, inner_angles, is_regular)
        # Set the square as regular
        self.set_is_regular(True)
    
    def compute_area(self):
        return super().compute_area()
    
    def compute_perimeter(self):
        return super().compute_perimeter()
    
    def compute_inner_angles(self):
        super().compute_inner_angles()
