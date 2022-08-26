from dataclasses import dataclass

from resourses.skills.base_skill import BaseSkill


@dataclass
class UnitClass:
    """Unit instance"""

    name: str
    max_health: float
    max_stamina: float
    damage_modifier: float
    stamina_modifier: float
    armor_modifier: float
    skill: BaseSkill
