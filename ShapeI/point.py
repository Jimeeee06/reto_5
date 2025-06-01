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
