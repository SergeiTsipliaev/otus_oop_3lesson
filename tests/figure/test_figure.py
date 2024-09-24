from src.figure import Figure
from src.circle import Circle
from src.triangle import Triangle
import pytest


def test_add_area_positive():
    c = Circle(1)
    t = Triangle(4, 3, 6)
    assert c.add_area(t) == c.get_area + t.get_area, f'Needed {Figure}'


@pytest.mark.parametrize(
    "r",
    [
        -1,
        0
    ]
)
def test_add_area_negative(r):
    with pytest.raises(ValueError, match= "Argument 'figure' must be object Figure" and "Not available with minus or '0' !!!"):
        Circle(r)