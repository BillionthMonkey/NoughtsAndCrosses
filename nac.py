def test_win():
    moves = [2, 1, 3, 0]
    options = [
        [0, 1, 2]
    ]
    assert is_win(moves, options) is True

def test_win_with_two_options():
    moves = [2, 1, 3, 0]
    options = [
        [0, 1, 2],
        [3, 4, 5]
    ]
    assert is_win(moves, options) is True

def test_extract_first_player_moves():
    moves = [2, 7, 1, 8, 3]
    assert moves_for_player(0, moves) == [2, 1, 3]

def test_extract_second_player_moves():
    moves = [4, 5, 6, 7, 8]
    assert moves_for_player(1, moves) == [5, 7]

def test_draw():
    moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert is_draw(moves) is True

def test_not_draw():
    moves = [0, 1, 2, 3, 4, 5, 6, 7]
    assert is_draw(moves) is False

def test_legal_move():
    assert is_legal(0, []) is True

def test_move_beyond_lower_bound():
    assert is_legal(-1, []) is False

def test_move_beyond_upper_bound():
    assert is_legal(9, []) is False


def is_win(moves, options):
    return any([set(moves).issuperset(set(option))
        for option in options])

def moves_for_player(player, moves):
    number_of_players = 2
    return moves[player::number_of_players]

def is_draw(moves):
    board_size = 9
    return len(moves) is board_size

def is_legal(move, moves):
    move_lower_bound = 0
    return move >= move_lower_bound and move not in moves
