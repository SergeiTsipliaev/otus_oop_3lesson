from src.figure import Figure
from abc import ABC


class Triangle(Figure, ABC):
    def __init__(self, side_a, side_b, side_c):
        if (side_a + side_b) < side_c or (side_b + side_c) < side_a or (side_c + side_a) < side_b or side_a <= 0 or side_b <= 0 or side_c <= 0 :
            raise ValueError("It is impossible to create such a triangle. Not available with minus or '0' !!!")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c


    @property
    def get_area(self):
        return 0.5 * self.side_a + self.side_b


    @property
    def get_perimetr(self):
        return self.side_b + self.side_b + self.side_c
