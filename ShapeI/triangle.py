from math import acos, asin, degrees
from ShapeI.shape import Shape

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
