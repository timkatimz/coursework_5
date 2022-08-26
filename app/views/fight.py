
from flask import render_template, Blueprint, current_app

from app.container import arena, heroes

fight_bp = Blueprint("Fight", __name__, url_prefix="/fight")


@fight_bp.route("/")
def fight():
    arena.STAMINA_PER_ROUND = current_app.config["STAMINA_PER_ROUND"]
    arena.start_game(player=heroes["player"], enemy=heroes["enemy"])
    result = "Битва началась"
    return render_template("fight.html", heroes=heroes, result=result)


@fight_bp.route("/hit/")
def hit():
    if arena.is_game_on:
        result = arena.player_hit()
        return render_template("fight.html", heroes=heroes, result=result)
    return render_template("fight.html", heroes=heroes, battle_result=arena.battle_result)


@fight_bp.route("/use-skill/")
def use_skill():
    if arena.is_game_on:
        result = arena.player_use_skill()
        return render_template("fight.html", heroes=heroes, result=result)
    return render_template("fight.html", heroes=heroes, battle_result=arena.battle_result)


@fight_bp.route("/pass-turn/")
def pass_turn():
    if arena.is_game_on:
        result = arena.next_turn()
        return render_template("fight.html", heroes=heroes, result=result)
    return render_template("fight.html", heroes=heroes, battle_result=arena.battle_result)


@fight_bp.route("/end-fight/")
def end_fight():
    arena.end_game()
    return render_template("index.html", heroes=heroes)