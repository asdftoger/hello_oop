from abc import ABCMeta, ABC, abstractmethod


class Shape(ABC):
    """
    Shapes are an abstract representation of 2D objects
    """

    # @abstractmethod
    # def calculate_perimeter()->float:
    #     """_summary_

    #     Returns:
    #         float: _description_
    #     """


class Polygon(Shape):
    """_summary_

    Args:
        Shape (_type_): _description_
    """


class RegularPolygon(Polygon):
    """_summary_

    Args:
        Polygon (_type_): _description_
    """


class Square(RegularPolygon):
    """ssss

    Args:
        RegularPolygon (s): s
    """

    num_sides = 4


Shape()
