import math
import turtle

class Shape(object):
    def draw(self):
        print "Shape"

    def get_area(self):
        return 0

    def get_perimeter(self):
        return 0

    def to_string(self):
        return "I'm shape"

    def __str__(self):
        return "I'm shape"

class Rectangular(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def draw(self):
        drawing = turtle.Turtle()
        for _ in range(2):
            drawing.forward(self.length)
            drawing.left(90)
            drawing.forward(self.width)
            drawing.left(90)
        turtle.Screen().exitonclick()

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return self.length * 2 + self.width * 2

    def to_string(self):
        return super(Rectangular, self).to_string() + " of type rectangular with length {length} and width {width}".\
            format(length = self.length, width = self.width)

    def __str__(self):
        return super(Rectangular, self).__str__() + " of type rectangular with length {length} and width {width}".\
            format(length = self.length, width = self.width)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def draw(self):
        #win = turtle.Screen()
        drawing = turtle.Turtle()
        for _ in range(4):
            drawing.forward(self.side)
            drawing.left(90)
        turtle.Screen().exitonclick()

    def get_area(self):
        return self.side ** 2

    def get_perimeter(self):
        return self.side * 4

    def to_string(self):
        return super(Square, self).to_string() + " of type square with side {side}". \
            format(side=self.side)

    def __str__(self):
        return super(Square, self).to_string() + " of type square with side {side}". \
            format(side=self.side)

class Triangular(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def draw(self):
        pass

    def get_area(self):
        half_perimeter = self.get_perimeter() / 2
        return math.sqrt(half_perimeter * (half_perimeter - self.a.get_distance_to(self.b)) * \
                         (half_perimeter - self.b.get_distance_to(self.c)) * \
                         (half_perimeter - self.c.get_distance_to(self.a)))

    def get_perimeter(self):
        return self.a.get_distance_to(self.b) + self.b.get_distance_to(self.c) + self.c.get_distance_to(self.a)

    def to_string(self):
        return super(Triangular, self).to_string() + " of type triangle with points A({a}), B{b}, C{c}". \
            format(a=(self.a.x, self.a.y), b=(self.b.x, self.b.y), c=(self.c.x, self.c.y))

    def __str__(self):
        return super(Triangular, self).to_string() + " of type triangle with points A({a}), B{b}, C{c}". \
            format(a=(self.a.x, self.a.y), b=(self.b.x, self.b.y), c=(self.c.x, self.c.y))

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        pass

    def get_area(self):
        return self.radius ** 2 * 3.14

    def get_perimeter(self):
        return 2 * 3.14 * self.radius

    def to_string(self):
        return super(Circle, self).to_string() + " of type circle with radius {radius}". \
            format(radius = self.radius)

    def __str__(self):
        return super(Circle, self).to_string() + " of type circle with radius {radius}". \
            format(radius = self.radius)

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance_to(self, Point):
        return math.sqrt((self.x - Point.x) ** 2 + (self.y - Point.y) ** 2 )

    def to_string(self):
        return "I'm point {coordinates}".format(coordinates=(self.x, self.y))

    def __str__(self):
        return "I'm point {coordinates}".format(coordinates=(self.x, self.y))