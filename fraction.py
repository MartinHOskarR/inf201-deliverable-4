from math import gcd


class Fraction:
    def __init__(self, numerator: int, denominator: int = 1):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers")
        if denominator <= 0:
            raise ValueError("Denominator must be strictly positive")
        # Store the fraction in lowest terms, so 2/4 becomes 1/2
        divisor = gcd(numerator, denominator)
        self.numerator = numerator // divisor
        self.denominator = denominator // divisor

    def __repr__(self) -> str:
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"

    # Comparisons use cross multiplication: a/b < c/d is the same as a*d < c*b
    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __ne__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator != other.numerator * self.denominator

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(
            self.numerator * other.denominator + other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(
            self.numerator * other.denominator - other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)