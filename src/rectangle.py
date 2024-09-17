from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        if side_a <= 0 or side_b <= 0:
            raise  ValueError("Not available with minus or '0' !!!")
        self.side_a = side_a
        self.side_b = side_b


    @property
    def get_area(self):
        return self.side_a * self.side_b


    @property
    def get_perimetr(self):
        return (self.side_a + self.side_b) *  2


r = Rectangle(4, 5)
print(r.get_area, r.get_perimetr)