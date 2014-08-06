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

def test_extract_player_one_moves():
    moves = [2, 7, 1, 8, 3]
    assert moves_for_player(0, moves) == [2, 1, 3]

def test_extract_player_two_moves():
    moves = [4, 5, 6, 7, 8]
    assert moves_for_player(1, moves) == [5, 7]


def is_win(moves, options):
    return any([set(moves).issuperset(set(option))
        for option in options])

def moves_for_player(player, moves):
    number_of_players = 2
    return moves[player::number_of_players]
