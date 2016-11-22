from figures import Rectangular


class SquareInherit(Rectangular):
    def __init__(self, side):
        super(SquareInherit, self).__init__(side, side)


class SquareComposition(object):
    def __init__(self, side):
        self.square_rectangular = Rectangular(side, side)

    def get_area(self):
        return self.square_rectangular.get_area()

    def get_perimeter(self):
        return self.square_rectangular.get_perimeter()

    def draw(self):
        self.square_rectangular.draw()

    def to_string(self):
        return self.square_rectangular.to_string()

    def __str__(self):
        return self.square_rectangular.__str__()