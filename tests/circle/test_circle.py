from src.circle import Circle
import pytest


@pytest.mark.parametrize(
    "r, area",
    [
        (3, 28.274333882308138),
        (2.2, 15.205308443374602)
    ],
    ids = ['Circle_Positive_integer',
           'Circle_Positive_float'
           ]

)

def test_circle_area_positive(r, area):
    c = Circle(r)
    assert c.get_area == area, f'Needed area = {area}'


@pytest.mark.parametrize(
    "r, area",
    [
        (4, 6),
        (1.4, 7.26),
        (0, 23),
        (-1, -2),
    ],
    ids = ['Circle_Negative: integer',
           'Circle_Negative: float',
           'Circle_Negative: side with 0',
           'Circle_Negative: side with minus'
           ]
)


def test_circle_area_negative(r, area):
    if r <= 0:
        with pytest.raises(ValueError, match="Not available with minus or '0' !!!"):
            Circle(r)
    else:
        c = Circle(r)
        assert c.get_area != area