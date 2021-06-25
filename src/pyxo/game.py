from .interfaces import GameInterface


class Game(GameInterface):
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self._table = [['-' for point in range(3)] for row in range(3)]

    @property
    def table(self) -> list:
        return self._table

    def get_row(self, index: int) -> list:
        if index >= 0 and index <= 2:
            return self.table[index]
        raise ValueError

    def get_column(self, index: int) -> list:
        if index >= 0 and index <= 2:
            return [row[index] for row in self.table]
        raise ValueError

    def get_rtl_diagonal(self) -> list:
        return [self.table[row][index] for row, index in zip(range(3),
                reversed(range(3)))]

    def get_ltr_diagonal(self) -> list:
        return [self.table[index][index] for index in range(3)]

    def set_point(self, point: tuple[int, int], value: str):
        if self.table[point[0]][point[1]] != '-':
            raise IndexError
        self._table[point[0]][point[1]] = value


def check_for_winner(game: GameInterface) -> tuple[bool, str]:
    for row in range(3):
        if all(['' if item == '-' else item for item in game.get_row(row)]):
            return (True, game.get_row(row)[0])
    for column in range(3):
        if all(['' if item == '-' else item
                for item in game.get_column(column)]):
            return (True, game.get_row(column)[0])
    if all(['' if item == '-' else item for item in game.get_rtl_diagonal()]):
        return (True, game.get_rtl_diagonal()[0])
    if all(['' if item == '-' else item for item in game.get_ltr_diagonal()]):
        return (True, game.get_ltr_diagonal()[0])
    return (False, '')
