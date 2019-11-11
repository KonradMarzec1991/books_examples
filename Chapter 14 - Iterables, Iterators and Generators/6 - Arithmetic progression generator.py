from fractions import Fraction
from decimal import Decimal


class ArithemticProgression:

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index


ap = ArithemticProgression(0, 1, 3)
print(list(ap))
ap = ArithemticProgression(1, .5, 3)
print(list(ap))
ap = ArithemticProgression(0, Fraction(1, 3), 1)
print(list(ap))
ap = ArithemticProgression(0, Decimal('.1'), .3)
print(list(ap))
