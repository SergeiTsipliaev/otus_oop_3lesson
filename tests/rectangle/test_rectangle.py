from src.rectangle import Rectangle
import pytest


@pytest.mark.parametrize(
    "side_a, side_b, area",
    [
        (2, 3, 6),
        (2.2, 3.3, 7.26)
    ],
    ids = ['Rectangle_Positive_integer',
           'Rectangle_Positive_float'
           ]

)


def test_rectangle_area_positive(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.get_area == pytest.approx(area), f'Needed area = {area}'


@pytest.mark.parametrize(
    "side_a, side_b, area",
    [
        (4, 3, 6),
        (1.1, 2.2, 7.26),
        (0, 3, 0),
        (-1, 2, -2),
        (2, 2, 4)
    ],
    ids = ['Rectangle_Negative: integer',
           'Rectangle_Negative: float',
           'Rectangle_Negative: side with 0',
           'Rectangle_Negative: side with minus',
           'Rectangle_Negative: side_a == side_b'
           ]
)


def test_rectangle_area_negative(side_a, side_b, area):
    if side_a <= 0 or side_b <= 0 or side_a == side_b:
        with pytest.raises(ValueError, match='Not available with minus or "0", and side_a should not will be == side_b !!!'):
            Rectangle(side_a, side_b)
    else:
        r = Rectangle(side_a, side_b)
        assert r.get_area != area