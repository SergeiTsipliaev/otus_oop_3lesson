from src.triangle import Triangle
import pytest


@pytest.mark.parametrize(
    "side_a, side_b, side_c, area",
    [
        (9, 4, 8, 8.5),
        (2.2, 5.2, 6.9, 6.3)
    ],
    ids = ['Circle_Positive_integer',
           'Circle_Positive_float'
           ]

)

def test_circle_area_positive(side_a, side_b, side_c, area):
    t = Triangle(side_a, side_b, side_c)
    assert t.get_area == pytest.approx(area), f'Needed area = {area}'


@pytest.mark.parametrize(
    "side_a, side_b, side_c, area",
    [
        (4, 120, 567, 6),
        (1.4, 230.1, 230.45, 7.26),
        (0, 1, 0, 23),
        (-1, -34, -49, -2),
    ],
    ids = ['Triangle_Negative: integer',
           'Triangle_Negative: float',
           'Triangle_Negative: side with 0',
           'Triangle_Negative: side with minus'
           ]
)


def test_circle_area_negative(side_a, side_b, side_c, area):
    if (side_a + side_b) < side_c or (side_b + side_c) < side_a or (side_c + side_a) < side_b or side_a <= 0 or side_b <= 0 or side_c <= 0:
        with pytest.raises(ValueError, match="It is impossible to create such a triangle. Not available with minus or '0' !!!"):
            Triangle(side_a, side_b, side_c)
    else:
        t = Triangle(side_a, side_b, side_c)
        assert t.get_area != area