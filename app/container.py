from resourses.arena.arena import Arena
from resourses.equipment.equipment import Equipment
from resourses.skills.fury_punch import FuryPunch
from resourses.skills.hard_shot import HardShot
from resourses.unit_class import UnitClass


"""Creating instances"""
arena = Arena()
equipment = Equipment()

heroes = {
    "player": None,
    "enemy": None
}

"""Creating instance of two heroes"""
WarriorClass = UnitClass(
    name="Воин",
    max_health=30.0,
    max_stamina=30.0,
    damage_modifier=1.1,
    stamina_modifier=1.1,
    armor_modifier=1.1,
    skill=FuryPunch()
)

ThiefClass = UnitClass(
    name="Вор",
    max_health=30.0,
    max_stamina=30.0,
    damage_modifier=0.9,
    stamina_modifier=1.1,
    armor_modifier=1.2,
    skill=HardShot()
)

unit_classes = {
    WarriorClass.name: WarriorClass,
    ThiefClass.name: ThiefClass
}