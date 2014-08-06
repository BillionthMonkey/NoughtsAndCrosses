nac = None

def setup_module(module):
    global nac
    nac = NoughtsAndCrosses()

def test_win():
    moves = [2, 1, 3, 0]
    options = [
        [0, 1, 2]
    ]
    assert nac.is_win(moves, options) is True

def test_win_with_two_options():
    moves = [2, 1, 3, 0]
    options = [
        [0, 1, 2],
        [3, 4, 5]
    ]
    assert nac.is_win(moves, options) is True

def test_extract_first_player_moves():
    moves = [2, 7, 1, 8, 3]
    assert nac.moves_for_player(0, moves) == [2, 1, 3]

def test_extract_second_player_moves():
    moves = [4, 5, 6, 7, 8]
    assert nac.moves_for_player(1, moves) == [5, 7]

def test_draw():
    moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert nac.is_draw(moves) is True

def test_not_draw():
    moves = [0, 1, 2, 3, 4, 5, 6, 7]
    assert nac.is_draw(moves) is False

def test_legal_move():
    assert nac.is_legal(0, []) is True

def test_move_beyond_lower_bound():
    assert nac.is_legal(-1, []) is False

def test_move_beyond_upper_bound():
    assert nac.is_legal(9, []) is False


class NoughtsAndCrosses():
    def __init__(self):
        self.board_size = 9

    def is_win(self, moves, options):
        return any([set(moves).issuperset(set(option))
            for option in options])

    def moves_for_player(self, player, moves):
        number_of_players = 2
        return moves[player::number_of_players]

    def is_draw(self, moves):
        return len(moves) is self.board_size

    def is_legal(self, move, moves):
        move_lower_bound = 0
        return move >= move_lower_bound \
            and move < self.board_size \
            and move not in moves
