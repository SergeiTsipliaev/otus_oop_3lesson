from src.rectangle import Rectangle
import pytest





@pytest.mark.parametrize(
    "side_a, side_b, area",
    [
        (2, 3, 6),
        (2.2, 3.3, 7.26)
    ],
    ids = ['integer', 'float'] #в строке выводим какие были проверки
)


def test_rectangle_area_positive(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.get_area == area, f'Needed area = {area}'



