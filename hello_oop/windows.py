from dataclasses import dataclass, field


@dataclass
class Frame:
    """_summary_"""

    name: str
    material: str

@dataclass
class SalesCampaign:
    name: str

@dataclass
class FrameCatalog:
    frames: dict[str,Frame]
    campaign: SalesCampaign = field()

class Window:
    def __init__(self, frame: Frame) -> None:
        self.frame = frame
        pass

    def get_frame(self) -> dict:
        return {
            "nam": self.frame.name,
            "mate": self.frame.material,
        }

    @classmethod
    def from_catalog(cls, catalog, name):
        return cls(catalog[name])
    

