from typing import List

import marshmallow

from resourses.equipment.armor import ArmorSchema, Armor
from resourses.equipment.equipment_data import EquipmentData
from resourses.equipment.weapon import WeaponSchema, Weapon
from utils import read_data_from_json


class Equipment:
    """Base equipment instance"""

    def __init__(self):
        self.equipment: EquipmentData = self._create_equipment_data()

    def _create_equipment_data(self) -> EquipmentData:
        data = read_data_from_json()
        try:
            return EquipmentData(
                weapons=WeaponSchema(many=True).load(data['weapons']),
                armors=ArmorSchema(many=True).load(data['armors'])
            )
        except marshmallow.exceptions.ValidationError:
            raise ValueError

    def get_weapon(self, weapon_name: str) -> Weapon:
        res = [x for x in self.equipment.weapons if x.name == weapon_name]
        return res[0]

    def get_armor(self, armor_name: str) -> Armor:
        res = [x for x in self.equipment.armors if x.name == armor_name]
        return res[0]

    def get_weapon_names(self) -> List:
        res = [x.name for x in self.equipment.weapons]
        return res

    def get_armor_names(self) -> List:
        res = [x.name for x in self.equipment.armors]
        return res
