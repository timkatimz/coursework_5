from dataclasses import dataclass, field
from typing import List


@dataclass
class EquipmentData:
    weapons: field(default_factory=List)
    armors: field(default_factory=List)
