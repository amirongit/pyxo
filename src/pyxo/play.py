from .interfaces import PlayerInterface, GameInterface


class Player(PlayerInterface):
    def __init__(self, game: GameInterface, char: str):
        self._game = game
        self.char = char

    @property
    def game(self) -> GameInterface:
        return self._game

    def mark(self, point: tuple):
        self.game.set_point(point, self.char)
