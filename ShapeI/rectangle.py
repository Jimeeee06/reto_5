from ShapeI.shape import Shape

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