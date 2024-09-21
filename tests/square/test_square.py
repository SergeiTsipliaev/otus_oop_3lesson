from src.square import Square
import pytest


@pytest.mark.parametrize(
    "side_a, side_b, area",
    [
        (3, 3, 9),
        (2.2, 2.2, 4.84)
    ],
    ids = ['Square_Positive_integer',
           'Square_Positive_float'
           ]

)

def test_square_area_positive(side_a, side_b, area):
    s = Square(side_a, side_b)
    assert s.get_area == pytest.approx(area), f'Needed area = {area}'


@pytest.mark.parametrize(
    "side_a, side_b, area",
    [
        (4, 3, 6),
        (1.4, 1.2, 7.26),
        (0, 3, 0),
        (-1, 2, -2),
        (12, 2, 4)
    ],
    ids = ['Square_Negative integer',
           'Square_Negative float',
           'Square_Negative: side with 0',
           'Square_Negative: side with minus',
           'Square_Negative: side_a != side_b'
           ]
)


def test_square_area_negative(side_a, side_b, area):
    if side_a >= 0 or side_b >= 0 or side_a != side_b:
        with pytest.raises(ValueError, match="Not available with minus or '0' and side_a should will be == side_b!!!"):
            Square(side_a, side_b)
    else:
        s = Square(side_a, side_b)
        assert s.get_area != area