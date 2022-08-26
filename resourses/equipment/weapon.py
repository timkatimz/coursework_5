import random

import marshmallow

from dataclasses import dataclass
import marshmallow_dataclass


@dataclass
class Weapon:
    """Класс оружия"""
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    class Meta:
        unknown = marshmallow.EXCLUDE

    def count_damage(self) -> float:
        return random.uniform(self.min_damage, self.max_damage)


WeaponSchema = marshmallow_dataclass.class_schema(Weapon)