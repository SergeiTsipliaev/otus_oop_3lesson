from src.square import Square
import pytest


@pytest.mark.parametrize(
    "side_a, side_b, area",
    [
        (3, 3, 9),
        (2.2, 2.2, 4.84)
    ],
    ids = ['Square_Area_Positive: integer',
           'Square_Area_Positive: float'
           ]

)
def test_square_area_positive(side_a, side_b, area):
    s = Square(side_a, side_b)
    assert s.get_area == pytest.approx(area), f'Needed area = {area}'


@pytest.mark.parametrize(
    "side_a, side_b",
    [
        (34, 4),
        (0, 3),
        (-1, 2)
    ],
    ids = ['Square_Area_Negative: side_a != side_b',
           'Square_Area_Negative: side with 0',
           'Square_Area_Negative: side with minus'
           ]
)
def test_square_area_negative(side_a, side_b):
        with pytest.raises(ValueError, match="Not available with minus or '0' and side_a should will be == side_b!!!"):
            Square(side_a, side_b)


@pytest.mark.parametrize(
    "side_a, side_b, perimetr",
    [
        (3, 3, 12),
        (2.2, 2.2, 8.8)
    ],
    ids = ['Square_Perimetr_Positive: integer',
          'Square_Perimetr_Positive: float'
    ]
)
def test_square_perimetr_positive(side_a, side_b, perimetr):
    r = Square(side_a, side_b)
    assert r.get_perimetr == perimetr, f'Needed perimetr = {perimetr}'


@pytest.mark.parametrize(
    "side_a, side_b",
    [
        (12, 11),
        (0, 3),
        (-1, 2)
    ],
    ids = ['Square_Perimetr_Negative: side_a == side_b',
           'Square_Perimetr_Negative: side with 0',
           'Square_Perimetr_Negative: side with minus',
           ]
)
def test_square_perimetr_negative(side_a, side_b):
        with pytest.raises(ValueError, match= "Not available with minus or '0' and side_a should will be == side_b!!!"):
            Square(side_a, side_b)