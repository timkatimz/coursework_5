from resourses.units.base_unit import BaseUnit
from random import randint


class EnemyUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        """Random hit for computer unit"""
        if not self.is_skill_used:
            random_chance = randint(0, 10)
            if random_chance == 6:
                return self.use_skill(target)
        return super().hit(target)
