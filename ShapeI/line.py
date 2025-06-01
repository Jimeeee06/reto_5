from ShapeI.point import Point

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


