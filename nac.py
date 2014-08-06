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
    player_one_moves = moves
    assert player_one_moves == [2, 1, 3]


def is_win(moves, options):
    return any([set(moves).issuperset(set(option))
        for option in options])
