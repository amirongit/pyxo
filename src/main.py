from subprocess import call

from pyxo.game import Game, check_for_winner
from pyxo.play import Player


def get_point_by_numkey(numkey: int) -> tuple[int, int]:
    NUMKEYS_TO_POINTS = {7: (0, 0), 8: (0, 1), 9: (0, 2),
                         4: (1, 0), 5: (1, 1), 6: (1, 2),
                         1: (2, 0), 2: (2, 1), 3: (2, 2)}
    return NUMKEYS_TO_POINTS[numkey]


def get_raw_table(table: list) -> str:
    raw_str = str()
    for row in table:
        for point in row:
            raw_str += point
            raw_str += ' ' * 2
        raw_str += '\n'
    return raw_str


def check_game_status_after_marking(game: Game) -> bool:
    winner = check_for_winner(game)
    if winner:
        call('clear', shell=True)
        print(get_raw_table(game.table))
        print(f'{winner} won!')
        return True
    if game.is_full():
        call('clear', shell=True)
        print(get_raw_table(game.table))
        print('no winner!')
        return True
    return False


def main():
    game = Game()
    fir_player = Player(game, 'X')
    sec_player = Player(game, 'O')
    while True:
        call('clear', shell=True)
        print(get_raw_table(game.table))
        fir_player.mark(get_point_by_numkey(int(input('X mark: '))))
        if check_game_status_after_marking(game):
            exit()
        call('clear', shell=True)
        print(get_raw_table(game.table))
        sec_player.mark(get_point_by_numkey(int(input('O mark: '))))
        if check_game_status_after_marking(game):
            exit()


if __name__ == '__main__':
    main()
