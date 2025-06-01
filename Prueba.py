from ShapeU.Shape import Point, Line, Triangle, Isosceles, Rectangle, Square

p1 = Point(0, 0)
p2 = Point(0, 3)
p3 = Point(4, 0)

l1 = Line(start=p1, end=p2)
l2 = Line(start=p2, end=p3)
l3 = Line(start=p3, end=p1)

tri = Triangle(vertices=[p1, p2, p3], edges=[l1, l2, l3], inner_angles=None, is_regular=None)
print("Perímetro triángulo:", tri.compute_perimeter())
print("Área triángulo:", tri.compute_area())

p4 = Point(4, 3)
l4 = Line(start=p3, end=p4)
l5 = Line(start=p4, end=p2)
rect = Rectangle(vertices=[p1, p2, p4, p3], edges=[l1, l5, l4, l3], inner_angles=None, is_regular=False)
print("Área rectángulo:", rect.compute_area())
print("Perímetro rectángulo:", rect.compute_perimeter())

p5 = Point(0, 0)
p6 = Point(0, 2)
p7 = Point(2, 2)
p8 = Point(2, 0)
ls1 = Line(start=p5, end=p6)
ls2 = Line(start=p6, end=p7)
ls3 = Line(start=p7, end=p8)
ls4 = Line(start=p8, end=p5)
square = Square(vertices=[p5, p6, p7, p8], edges=[ls1, ls2, ls3, ls4], inner_angles=None, is_regular=True)
print("Área cuadrado:", square.compute_area())
print("Perímetro cuadrado:", square.compute_perimeter())
