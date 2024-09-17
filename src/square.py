from src.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("Not available with minus or '0' !!!")
        super().__init__(side_a, side_a)
        self.side_a = side_a


s = Square(5)
print(s.get_area, s.get_perimetr)