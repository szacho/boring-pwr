from random import random
from math import sqrt
# z listy pierwszej
class Vector:

    def __init__(self, values):
        self.values = values

    def __getitem__(self, key):
        return self.values[key]

    def __contains__(self, value):
        return value in self.values

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError('Cannot add {} to {}'.format(other.__class__.__name__, self.__class__.__name__))
        else:
            added = [ a+b for a, b in zip(self.values, other.values) ]
            return Vector(added)

    def __sub__(self, other):
        if type(self) is not type(other):
            raise TypeError('Cannot substract {} from {}'.format(other.__class__.__name__, self.__class__.__name__))
        else:
            substracted = [ a-b for a, b in zip(self.values, other.values) ]
            return Vector(substracted)

    def __repr__(self):
        return f'*{self.values}'
