import pytest
from fraction import Fraction


# Initialiser
def test_init():
    f = Fraction(3, 4)
    assert f.numerator == 3
    assert f.denominator == 4


def test_default_denominator():
    assert Fraction(5).denominator == 1


def test_lowest_terms():
    f = Fraction(6, 8)
    assert f.numerator == 3
    assert f.denominator == 4


def test_denominator_must_be_positive():
    with pytest.raises(ValueError):
        Fraction(1, 0)
    with pytest.raises(ValueError):
        Fraction(1, -2)


def test_must_be_integers():
    with pytest.raises(TypeError):
        Fraction(1.5, 2)
    with pytest.raises(TypeError):
        Fraction(1, "2")


# Comparisons
def test_comparisons():
    assert Fraction(1, 2) == Fraction(2, 4)
    assert Fraction(1, 2) != Fraction(1, 3)
    assert Fraction(1, 3) < Fraction(1, 2)
    assert Fraction(1, 2) <= Fraction(2, 4)
    assert Fraction(1, 2) > Fraction(-1, 2)
    assert Fraction(1, 2) >= Fraction(1, 3)


def test_comparison_with_other_type():
    assert Fraction(1, 2) != "1/2"
    with pytest.raises(TypeError):
        Fraction(1, 2) < 1


# Other special methods
def test_repr_and_str():
    assert repr(Fraction(1, 2)) == "Fraction(1, 2)"
    assert str(Fraction(-3, 4)) == "-3/4"


def test_add():
    assert Fraction(1, 2) + Fraction(1, 3) == Fraction(5, 6)


def test_sub():
    assert Fraction(1, 3) - Fraction(1, 2) == Fraction(-1, 6)


def test_mul():
    assert Fraction(2, 3) * Fraction(3, 4) == Fraction(1, 2)