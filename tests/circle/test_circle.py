from src.circle import Circle
import pytest


@pytest.mark.parametrize(
    "r, area",
    [
        (3, round(28.274333882308138, 2)),
        (2.2, round(15.205308443374602, 2))
    ],
    ids = ['Circle_Area_Positive: integer',
           'Circle_Area_Positive: float'
           ]
)
def test_circle_area_positive(r, area):
    c = Circle(r)
    assert round(c.get_area, 2) == area, f'Needed area = {area}'


@pytest.mark.parametrize(
    "r",
    [
        (0),
        (-1)
    ],
    ids = ['Circle_Area_Negative: side with 0',
           'Circle_Area_Negative: side with minus'
           ]
)
def test_circle_area_negative(r):
        with pytest.raises(ValueError, match="Not available with minus or '0' !!!"):
            Circle(r)


@pytest.mark.parametrize(
    "r, perimetr",
    [
        (3, round(18.84955592153876, 2)),
        (2.2, round(13.823007675795091, 2))
    ],
    ids = ['Circle_perimetr_Positive: integer',
          'Circle_perimetr_Positive: float'
    ]
)
def test_circle_perimetr_positive(r, perimetr):
    c = Circle(r)
    assert round(c.get_perimetr, 2) == perimetr, f'Needed area = {perimetr}'


@pytest.mark.parametrize(
    "r",
    [
        (0),
        (-1000)
    ],
    ids=['Circle_Perimetr_Negative: side with 0',
         'Circle_Perimetr_Negative: side with minus'
         ]
)
def test_circle_perimetr_negative(r):
        with pytest.raises(ValueError, match="Not available with minus or '0' !!!"):
            Circle(r)


