#%%
from dataclasses import dataclass, field


@dataclass
class Foot:
    num_toes: int = 5


print(Foot().num_toes)

print(Foot.num_toes)
