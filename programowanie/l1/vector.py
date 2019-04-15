from random import random
from math import sqrt

class Vector:

    def __init__(self, size=3):
        """
            Creates a vector of zeros in given size
        """
        self.size = int(size)
        self.values = [0]*int(size)


    def setValues(self, values):
        """
            Sets new vector elements adjusting its size
        """
        if all(isinstance(val, (int, float)) for val in values):
            self.size = len(values)
            self.values = values
        else:
            raise ValueError('Vector elements must be either integers or floats')

    def randomize(self):
        """
            Generates random vector elements from range [-10, 10]
        """
        self.setValues([ (random()-.5)*20 for _ in range(self.size) ])

    def length(self):
        """
            Returns length of the vector
        """
        return sqrt(sum([ x**2 for x in self.values ]))

    def sumOfValues(self):
        """
            Returns sum of vector elements
        """
        return sum(self.values)

    def scalarProduct(self, other):
        if isinstance(other, Vector) and other.size is self.size:
            return sum([ a*b for a, b in zip(self.values, other.values) ])
        elif isinstance(other, Vector) and other.size is not self.size:
            raise ValueError('Cannot calculate scalar product, dimensions are not equal')
        else:
            raise TypeError('Cannot perform multiplication of {} and {}'.format(self.__class__.__name__, other.__class__.__name__))

    def __getitem__(self, key):
        """
            [] operator returns particular vector element
        """
        return self.values[key]

    def __contains__(self, value):
        """
            'in' operator checks if an element belongs to a vector
        """
        return value in self.values

    def __add__(self, other):
        """
            + operator adds two vectors element by element if it's possible
        """
        if type(self) is not type(other):
            raise TypeError('Cannot add {} to {}'.format(other.__class__.__name__, self.__class__.__name__))
        elif self.size is not other.size:
            raise ValueError('Cannot add vectors, dimensions are not equal')
        else:
            added = [ a+b for a, b in zip(self.values, other.values) ]
            new = Vector()
            new.setValues(added)
            return new

    def __sub__(self, other):
        """
            - operator substracts two vectors element by element if it's possible
        """
        if type(self) is not type(other):
            raise TypeError('Cannot substract {} from {}'.format(other.__class__.__name__, self.__class__.__name__))
        elif self.size is not other.size:
            raise ValueError('Cannot substract vectors, dimensions are not equal')
        else:
            substracted = [ a-b for a, b in zip(self.values, other.values) ]
            new = Vector()
            new.setValues(substracted)
            return new

    def __mul__(self, other):
        """
            * operator calculates scalar product of two vectors or multiplies every element of a vector by any real number
        """
        if isinstance(other, (int, float)):
            multiplied = [ other*x for x in self.values ]
            new = Vector()
            new.setValues(multiplied)
            return new
        else:
            return self.scalarProduct(other)

    __rmul__ = __mul__ #commutative operation

    def __repr__(self):
        return str(self.values)
