from src.figure import Figure
from src.rectangle import Rectangle


class Square(Figure):
    def __init__(self, side_a, side_b):
        if side_a <= 0 or side_a != side_b:
            raise ValueError("Not available with minus or '0' and side_a should will be == side_b!!!")
        self.side_a = side_a
        self.side_b = side_b

    @property
    def get_area(self):
        return self.side_a * self.side_b


    @property
    def get_perimetr(self):
        return (self.side_a + self.side_b) * 2
