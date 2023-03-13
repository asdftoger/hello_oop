from abc import ABC
from math import pi, sin, cos


class Arm:
    def __init__(self, forearm_length: float, upperarm_length: float) -> None:
        self.forearm_length = forearm_length
        self.upperarm_length = upperarm_length
        pass

    def grip(self):
        """_summary_"""

    def adjust(self):
        """_summary_"""


class Animal(ABC):
    """An Animal

    Args:
        ABC (_type_): _description_
    """


class Human(Animal):
    """_summary_

    Args:
        Animal (_type_): _description_
    """

    def __init__(self, arm: Arm) -> None:
        super().__init__()
        self.arm = arm

    def grab_clothing(self):
        self.arm.grip()


class Lizard(Animal):
    """_summary_

    Args:
        Animal (_type_): _description_
    """

    def __init__(self, arm: Arm) -> None:
        super().__init__()
        self.arm = arm

    def grab_food(self):
        self.arm.grip()


class KukaRobot:
    def __init__(self, arm: Arm) -> None:
        pass


def some_function():
    """_summary_"""
    x = 100
    y = x * pi
    z = y * 100

    new_var = new_func(x, y, z)
    return new_var


def new_func(x, y, z):
    t = sin(x) * cos(y) + sin(z)
