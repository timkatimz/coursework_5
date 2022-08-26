from __future__ import annotations

from abc import ABC
from typing import Optional

from resourses.equipment.armor import Armor
from resourses.equipment.weapon import Weapon
from resourses.unit_class import UnitClass


class BaseUnit(ABC):
    """Base unit instance"""

    def __init__(self, name: str, unit_class: UnitClass, weapon: Weapon, armor: Armor):
        self.name: str = name
        self.unit_class: UnitClass = unit_class
        self.health_points_: float = unit_class.max_health
        self.stamina_points_: float = unit_class.max_stamina
        self.weapon: Weapon = weapon
        self.armor: Armor = armor
        self.is_skill_used: bool = False

    @property
    def health_points(self) -> float:
        if self.health_points_ < 0:
            return 0
        return round(self.health_points_, 1)

    @property
    def stamina_points(self) -> float:
        return round(self.stamina_points_, 1)

    def equip_weapon(self, weapon: Weapon) -> str:
        self.weapon = weapon
        return f"{self.name} экипирован оружием {self.weapon.name}"

    def equip_armor(self, armor: Armor) -> str:
        self.armor = armor
        return f"{self.name} экипирован броней {self.armor.name}"

    def count_damage(self, target: BaseUnit) -> Optional[float, int]:
        """Counting damage and defence of units"""
        damage = self.weapon.count_damage() * self.unit_class.damage_modifier
        defence = target.armor.defence if target.stamina_points_ >= target.armor.stamina_per_turn else 0

        if damage < defence:
            damage_dealt = 0
        else:
            damage_dealt = damage - defence

        return round(damage_dealt, 1)

    def get_damage(self, damage: int) -> None:
        self.health_points_ -= damage

    def use_skill(self, target: BaseUnit) -> str:
        if self.is_skill_used:
            return "Навык уже использован!"
        self.is_skill_used = True
        return self.unit_class.skill.use(user=self, target=target)

    def hit(self, target: BaseUnit) -> str:
        if self.stamina_points_ >= self.weapon.stamina_per_hit:
            damage_dealt = self.count_damage(target)
            target.get_damage(damage_dealt)

            self.stamina_points_ -= self.weapon.stamina_per_hit
            target.stamina_points_ -= target.armor.stamina_per_turn
            if target.stamina_points_ < 0:
                target.stamina_points_ = 0

            if damage_dealt > 0:
                return (f"{self.name} используя {self.weapon.name}"
                        f" пробивает {target.armor.name} соперника и наносит {damage_dealt} урона.")
            return (f"{self.name} используя {self.weapon.name}"
                   f" наносит удар, но {target.armor.name} cоперника его останавливает.")
        return (f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости.")
