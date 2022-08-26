from flask import render_template, Blueprint, request, redirect, url_for

from app.container import equipment, unit_classes, heroes
from resourses.units.enemy_unit import EnemyUnit
from resourses.units.player_unit import PlayerUnit

start_bp = Blueprint("Start", __name__)


@start_bp.route("/")
def menu_page():
    return render_template("index.html")


@start_bp.route("/choose-hero/", methods=['POST', 'GET'])
def choose_hero():
    if request.method == 'GET':
        result = {
            "header": "Страница выбора героя",  # для названия страниц
            "classes": unit_classes,  # для названия классов
            "weapons": equipment.get_weapon_names(),  # для названия оружия
            "armors": equipment.get_armor_names()  # для названия брони
        }
        return render_template("hero_choosing.html", result=result)

    if request.method == 'POST':
        user_name = request.form.get("name")
        unit_class = unit_classes[request.form.get('unit_class')]
        weapon = equipment.get_weapon(request.form.get("weapon"))
        armor = equipment.get_armor(request.form.get("armor"))

        player_unit = PlayerUnit(name=user_name, unit_class=unit_class, weapon=weapon, armor=armor)
        heroes["player"] = player_unit

        return redirect(url_for("Start.choose_enemy"))


@start_bp.route("/choose-enemy/", methods=['POST', 'GET'])
def choose_enemy():
    if request.method == 'GET':
        result = {
            "header": "Страница выбора врага",  # для названия страниц
            "classes": unit_classes,  # для названия классов
            "weapons": equipment.get_weapon_names(),  # для названия оружия
            "armors": equipment.get_armor_names()  # для названия брони
        }
        return render_template("hero_choosing.html", result=result)

    if request.method == 'POST':
        user_name = request.form.get("name")
        unit_class = unit_classes[request.form.get('unit_class')]
        weapon = equipment.get_weapon(request.form.get("weapon"))
        armor = equipment.get_armor(request.form.get("armor"))

        enemy_unit = EnemyUnit(name=user_name, unit_class=unit_class, weapon=weapon, armor=armor)
        heroes["enemy"] = enemy_unit
        return redirect(url_for("Fight.fight"))