from src.triangle import Triangle
import pytest


@pytest.mark.parametrize(
    "side_a, side_b, side_c, area",
    [
        (9, 4, 8, 8.5),
        (2.2, 5.2, 6.9, 6.3)
    ],
    ids = ['Triangle_Area_Positive: integer',
           'Triangle_Area_Positive: float'
           ]

)
def test_triangle_area_positive(side_a, side_b, side_c, area):
    t = Triangle(side_a, side_b, side_c)
    assert t.get_area == pytest.approx(area), f'Needed area = {area}'


@pytest.mark.parametrize(
    "side_a, side_b, side_c",
    [
        (4, 120, 567),
        (0, 1, 0),
        (-1, -34, -49),
    ],
    ids = ['Triangle_Area_Negative: (side_a + side_b) < side_c',
           'Triangle_Area_Negative: side with 0',
           'Triangle_Area_Negative: side with minus'
           ]
)
def test_triangle_area_negative(side_a, side_b, side_c):
        with pytest.raises(ValueError, match="It is impossible to create such a triangle. Not available with minus or '0' !!!"):
            Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize(
    "side_a, side_b, side_c, perimetr",
    [
        (9, 4, 8, 21),
        (2.2, 5.2, 6.9, 14.3)
    ],
    ids = ['Triangle_Perimetr_Positive: integer',
           'Triangle_Perimetr_Positive: float'
           ]

)
def test_triangle_perimetr_positive(side_a, side_b, side_c, perimetr):
    t = Triangle(side_a, side_b, side_c)
    assert t.get_perimetr == pytest.approx(perimetr), f'Needed area = {perimetr}'


@pytest.mark.parametrize(
    "side_a, side_b, side_c",
    [
        (0, 1, 2),
        (-1, 3, -24),
        (1, 1, 5)
    ],
    ids = ['Triangle_Perimetr_Negative: with 0',
           'Triangle_Perimetr_Negative: with minus',
           'Triangle_Perimetr_Negative: (side_a + side_b) < side_c'
           ]

)
def test_triangle_perimetr_positive(side_a, side_b, side_c):
    with pytest.raises(ValueError, match = "It is impossible to create such a triangle. Not available with minus or '0' !!!"):
        Triangle(side_a, side_b, side_c)