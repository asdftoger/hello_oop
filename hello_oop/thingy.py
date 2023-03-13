#%%
from abc import abstractmethod, ABC
from dataclasses import dataclass, field, asdict
from math import pi
from numbers import Number


@dataclass
class Point:
    """What should I point out

    Raises:
        NotImplementedError: _description_

    Returns:
        _type_: _description_
    """

    x: float = 0
    y: float = 0

    def __sub__(self, o):

        if isinstance(o, Point):
            return Point(self.x - o.x, self.y - o.y)
        elif isinstance(o, (float, int)):
            return Point(self.x - float(o), self.y - float(o))
        else:
            raise NotImplementedError()


@dataclass
class Rotation:
    """idk why i'm doing this, cuz of unity?"""

    theta: float = 0


class Shape2D(ABC):
    """Shapes!!!

    Args:
        ABC (_type_): _description_

    Returns:
        _type_: _description_
    """

    @abstractmethod
    def area(self):
        """_summary_

        Returns:
            _type_: _description_
        """


@dataclass
class Circle(Shape2D):
    """Circle my dircle

    Args:
        Shape2D (_type_): _description_

    Returns:
        _type_: _description_
    """

    radius: float = 1
    center: Point = field(default_factory=Point)

    @classmethod
    def from_area(cls, area, **kwargs):
        return cls(area / (pi**2), **kwargs)

    @classmethod
    def from_perimeter(cls, per, **kwargs):
        return cls(per / (pi * 2), **kwargs)

    @property
    def area(self):
        return self.radius**2 * pi


radius_conf = dict(radius=1)

c_r = Circle(**radius_conf)
print(c_r.radius)

c_a = Circle.from_area(1, center=10)

print(asdict(c_a))
print(c_a.radius)

Circle.from_perimeter(1)


@dataclass
class Square(Shape2D):
    """A square, what's there to say?

    Args:
        Shape2D (_type_): _description_

    Returns:
        _type_: _description_
    """

    length: float = 1
    bl_point: Point = field(default_factory=Point)
    rotation: Rotation = field(default_factory=Rotation)

    @classmethod
    def from_center(cls, center: Point, length: float, **kwargs):
        return cls(length, center - length / 2, **kwargs)

    @property
    def area(self):
        return self.length**2


class CircleSquare(Shape2D):
    """
    A Point at the center of a square and circle, default override the Circle and Square points

    Args:
        Shape2D (_type_): _description_

    Returns:
        _type_: _description_
    """

    def __init__(self, circle: Circle, square: Square, center: Point) -> None:
        circle.center = center
        self.circle = circle
        # square.bl_point
        self.square = Square.from_center(
            center=center, length=square.length, rotation=square.rotation
        )
        self.center = center

        super().__init__()

    @property
    def area(self):
        return self.square.area - self.circle.area


s = Square()

cs = CircleSquare(Circle(center=Point(100, 100)), Square(), Point(2, 2))

print(cs.__dict__)
print(cs.area)
