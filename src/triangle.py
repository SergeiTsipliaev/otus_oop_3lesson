from src.figure import Figure
from abc import ABC


class Triangle(Figure, ABC):
    def __init__(self, side_a, side_b, side_c):
        if (side_a + side_b) < side_c or (side_b + side_c) < side_a or (side_c + side_a) < side_b:
            raise ValueError("It is impossible to create such a triangle!!!")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c


    @property
    def get_area(self):
        return 0.5 * self.side_a + self.side_b


    @property
    def get_perimetr(self):
        return self.side_b + self.side_b + self.side_c



t = Triangle(1, 1, 1, 0)

print(t.get_area, t.get_perimetr)