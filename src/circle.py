import math
from src.figure import Figure


class Circle(Figure):
    def __init__(self, r):
        if r <= 0:
            raise ValueError("Not available with minus or '0' !!!")
        self.r = r


    @property
    def get_area(self):
        return math.pi * self.r ** 2


    @property
    def get_perimetr(self):
        return 2 * math.pi * self.r
c = Circle(2.2)
print(c.get_area)