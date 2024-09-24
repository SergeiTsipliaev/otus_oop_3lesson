from src.rectangle import Rectangle
import pytest


@pytest.mark.parametrize(
    "side_a, side_b, area",
    [
        (2, 3, 6),
        (2.2, 3.3, 7.26)
    ],
    ids = ['Rectangle_Area_Positive_integer',
           'Rectangle_Area_Positive_float'
           ]

)
def test_rectangle_area_positive(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.get_area == pytest.approx(area), f'Needed area = {area}'


@pytest.mark.parametrize(
    "side_a, side_b",
    [
        (12, 12),
        (0, 3),
        (-1, 2)
    ],
    ids = ['Rectangle_Area_Negative: side_a == side_b',
           'Rectangle_Area_Negative: side with 0',
           'Rectangle_Area_Negative: side with minus'
           ]
)
def test_rectangle_area_negative(side_a, side_b):
        with pytest.raises(ValueError, match='Not available with minus or "0", and side_a should not will be == side_b !!!'):
            Rectangle(side_a, side_b)


@pytest.mark.parametrize(
    "side_a, side_b, perimetr",
    [
        (2, 3, 10),
        (2.2, 3.3, 11)
    ],
    ids = ['Circle_Perimetr_Positive: integer',
          'Circle_Perimetr_Positive: float'
    ]
)
def test_rectangle_perimetr_positive(side_a, side_b, perimetr):
    r = Rectangle(side_a, side_b)
    assert r.get_perimetr == perimetr, f'Needed perimetr = {perimetr}'


@pytest.mark.parametrize(
    "side_a, side_b",
    [
        (100, 100),
        (0, 3),
        (-1, 2)
    ],
    ids = ['Rectangle_Perimetr_Negative: side_a == side_b',
           'Rectangle_Perimetr_Negative: side with 0',
           'Rectangle_Perimetr_Negative: side with minus',
           ]
)
def test_rectangle_perimetr_negative(side_a, side_b):
        with pytest.raises(ValueError, match='Not available with minus or "0", and side_a should not will be == side_b !!!'):
            Rectangle(side_a, side_b)