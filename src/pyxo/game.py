from .interfaces import GameInterface


class Game(GameInterface):
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self._table = [['-' for _ in range(3)] for _ in range(3)]

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

    def is_full(self) -> bool:
        for row in self.table:
            for point in row:
                if point == '-':
                    return False
        return True


def check_for_winner(game: Game) -> str:
    if res := check_for_row_winner(game):
        return res
    if res := check_for_column_winner(game):
        return res
    if res := check_for_rtl_diagonal_winner(game):
        return res
    if res := check_for_ltr_diagonal_winner(game):
        return res
    return ''


def check_for_row_winner(game: Game) -> str:
    for row in range(3):
        processed_row = ['' if item == '-' else item
                         for item in game.get_row(row)]
        if all(processed_row) and len(set(processed_row)) == 1:
            return game.get_row(row)[0]
    return ''


def check_for_column_winner(game: Game) -> str:
    for column in range(3):
        processed_column = ['' if item == '-' else item
                            for item in game.get_column(column)]
        if all(processed_column) and len(set(processed_column)) == 1:
            return game.get_column(column)[0]
    return ''


def check_for_rtl_diagonal_winner(game: Game) -> str:
    processed_rtl_diagonal = ['' if item == '-' else item
                              for item in game.get_rtl_diagonal()]
    if all(processed_rtl_diagonal) and len(set(processed_rtl_diagonal)) == 1:
        return game.get_rtl_diagonal()[0]
    return ''


def check_for_ltr_diagonal_winner(game: Game) -> str:
    processed_ltr_diagonal = ['' if item == '-' else item
                              for item in game.get_ltr_diagonal()]
    if all(processed_ltr_diagonal) and len(set(processed_ltr_diagonal)) == 1:
        return game.get_ltr_diagonal()[0]
    return ''
