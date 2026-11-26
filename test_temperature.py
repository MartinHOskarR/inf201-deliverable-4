import pytest
from temperature import Temperature


# 1. Initialization
def test_default_unit():
    assert Temperature(25).unit == "C"


def test_case_insensitive():
    assert Temperature(25, "c").unit == "C"
    assert Temperature(25, "f").unit == "F"
    assert Temperature(25, "k").unit == "K"


def test_read_only():
    t = Temperature(25, "C")
    with pytest.raises(AttributeError):
        t.value = 30
    with pytest.raises(AttributeError):
        t.unit = "F"


# 2. Validation
def test_invalid_unit():
    with pytest.raises(ValueError):
        Temperature(25, "X")


def test_below_absolute_zero():
    with pytest.raises(ValueError):
        Temperature(-274, "C")
    with pytest.raises(ValueError):
        Temperature(-460, "F")
    with pytest.raises(ValueError):
        Temperature(-1, "K")


# 3. Conversions (C, F, K)
points = [
    (-273.15, -459.67, 0),   # absolute zero
    (-40, -40, 233.15),      # crossover
    (0, 32, 273.15),         # water freezes
    (37, 98.6, 310.15),      # body temperature
    (100, 212, 373.15),      # water boils
]


def test_conversions():
    for c, f, k in points:
        t = Temperature(c, "C")
        assert t.to_fahrenheit() == pytest.approx(f)
        assert t.to_kelvin() == pytest.approx(k)
        assert Temperature(f, "F").to_celsius() == pytest.approx(c)
        assert Temperature(k, "K").to_celsius() == pytest.approx(c)


# 4. Round trip
def test_round_trip():
    t = Temperature(25, "C")
    assert t.convert_to("F").convert_to("K").convert_to("C") == t


# 5. Comparisons across units
def test_comparisons():
    assert Temperature(0, "C") == Temperature(32, "F")
    assert Temperature(0, "C") != Temperature(0, "F")
    assert Temperature(0, "C") < Temperature(100, "F")
    assert Temperature(0, "C") <= Temperature(273.15, "K")
    assert Temperature(100, "C") > Temperature(100, "F")
    assert Temperature(100, "C") >= Temperature(212, "F")


# 6. Formatting
def test_str_and_repr():
    t = Temperature(25, "C")
    assert str(t) == "25.00 °C"
    assert repr(t) == "Temperature(25.0, 'C')"
