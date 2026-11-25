TOLERANCE = 1e-9

class Temperature:
    def __init__(self, value, unit="C"):
        unit = unit.upper()
        if unit not in ("C", "F", "K"):
            raise ValueError("Unit must be C, F or K")
        self._value = float(value)
        self._unit = unit
        if self.to_kelvin() < 0:
            raise ValueError("Temperature is below absolute zero")

    @property
    def value(self):
        return self._value

    @property
    def unit(self):
        return self._unit

    def to_celsius(self):
        if self.unit == "F":
            return (self.value - 32) * 5 / 9
        elif self.unit == "K":
            return self.value - 273.15
        else:  # C
            return self.value

    def to_fahrenheit(self):
        if self.unit == "F":
            return self.value
        elif self.unit == "K":
            return (self.value - 273.15) * 9 / 5 + 32
        else:  # C
            return self.value * 9 / 5 + 32

    def to_kelvin(self):
        if self.unit == "F":
            return (self.value - 32) * 5 / 9 + 273.15
        elif self.unit == "K":
            return self.value
        else:  # C
            return self.value + 273.15

    def convert_to(self, target_unit):
        target_unit = target_unit.upper()
        if target_unit == "C":
            return Temperature(self.to_celsius(), "C")
        if target_unit == "F":
            return Temperature(self.to_fahrenheit(), "F")
        if target_unit == "K":
            return Temperature(self.to_kelvin(), "K")
        raise ValueError("Unit must be C, F or K")

    def __repr__(self):
        return f"Temperature({self.value}, '{self.unit}')"

    def __str__(self):
        return f"{self.value:.2f} °{self.unit}"

    # All comparisons are done in Kelvin
    def __eq__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return abs(self.to_kelvin() - other.to_kelvin()) < TOLERANCE

    def __ne__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return not self == other

    def __lt__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_kelvin() < other.to_kelvin() and self != other

    def __le__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return self < other or self == other

    def __gt__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_kelvin() > other.to_kelvin() and self != other

    def __ge__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return self > other or self == other