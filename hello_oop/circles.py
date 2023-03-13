"""

Why use class method?

"""
#%%
from math import pi


class Circle:
    _num_circles: int = 0

    def __init__(self, radius: float):
        """Instantiate a circle from its radius
        :param radius: It's radius
        :type radius: float
        """
        self.radius = radius
        Circle._num_circles += 1

    @classmethod
    def from_area(cls, area: float, **kwargs):
        """What if I wanted to from it's area? 1. Alternative constructor

        :param area: The area of a circle
        :type area: float
        :return: Return an Circle instance
        """
        return cls(area / (pi**2), **kwargs)

    @classmethod
    @property
    def num_circles(cls) -> int:
        """Suppose I wanted to track the total number of circles I've ever created?
        2. Access class level attributes

        :return: Number of circles instantiated
        :rtype: _type_
        """
        return cls._num_circles

    def __del__(self):
        Circle._num_circles -= 1
        del self

    @property
    def area(self):
        return self.radius**2 * pi

#%%
c0=Circle(1)
print(Circle.num_circles)
c1=Circle.from_area(2)
print(Circle.num_circles)
#Notice how a redefinition of a variable deletes and readds it > 2 circles
c1=Circle(100)
print(Circle.num_circles)


# %%
