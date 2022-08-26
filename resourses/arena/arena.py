from typing import Optional, Dict

from resourses.arena.singletone import BaseSingleton
from resourses.units.base_unit import BaseUnit


class Arena(metaclass=BaseSingleton):
    """Arena instance"""
    STAMINA_PER_ROUND: float = 1
    player: BaseUnit
    enemy: BaseUnit
    is_game_on: bool = False
    battle_result: str = ""

    def start_game(self, player: BaseUnit, enemy: BaseUnit) -> str:
        self.player: BaseUnit = player
        self.enemy: BaseUnit = enemy
        self.is_game_on: bool = True
        return "Битва началась"

    def _check_players_hp(self) -> bool:

        if self.player.health_points_ > 0 and self.enemy.health_points_ > 0:
            return True

        if self.player.health_points_ >= 0 >= self.enemy.health_points_:
            self.battle_result = f"Игрок {self.player.name} выйграл битву"

        if self.player.health_points_ <= 0 <= self.enemy.health_points_:
            self.battle_result = f"Игрок {self.player.name} проиграл битву"

        if self.player.health_points_ <= 0 and self.enemy.health_points_ <= 0:
            self.battle_result = "Ничья"

        self.end_game()
        return False

    def _stamina_regeneration(self) -> None:
        player_stamina_regen = self.STAMINA_PER_ROUND * self.player.unit_class.stamina_modifier
        enemy_stamina_regen = self.STAMINA_PER_ROUND * self.enemy.unit_class.stamina_modifier

        self.player.stamina_points_ += player_stamina_regen
        self.enemy.stamina_points_ += enemy_stamina_regen

        """Ensure that stamina doesnt over limit max stamina"""
        if self.player.stamina_points_ > self.player.unit_class.max_stamina:
            self.player.stamina_points_ = self.player.unit_class.max_stamina
        if self.enemy.stamina_points_ > self.enemy.unit_class.max_stamina:
            self.enemy.stamina_points_ = self.enemy.unit_class.max_stamina

    def player_hit(self) -> str:
        player_result = self.player.hit(target=self.enemy)
        return player_result + " " + self.next_turn()

    def player_use_skill(self) -> str:
        player_result = self.player.use_skill(target=self.enemy)
        return player_result + " " + self.next_turn()

    def next_turn(self) -> Optional[str]:

        if self._check_players_hp():
            self._stamina_regeneration()
            enemy_result = self.enemy.hit(self.player)
            self._stamina_regeneration()
            return enemy_result
        return self.battle_result

    def end_game(self) -> None:
        self._instances: Dict = {}
        self.is_game_on = False