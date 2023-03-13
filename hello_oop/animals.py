from abc import ABC


class Vocalisation(ABC):
    """dog vocalisation->bark, duck v... -> quack ....

    :param ABC: _description_
    :type ABC: _type_
    """


class Animal(ABC):
    def __init__(self, vocalisation: Vocalisation) -> None:
        super().__init__()
        self.vocalisation = vocalisation
