def test_legal_move_is_legal():
    move = 0
    assert is_legal(move, []) is True


def test_illegal_move_is_not_legal():
    move = -1
    assert is_legal(move, []) is False


def test_different_legal_move_is_legal():
    move = 1
    assert is_legal(move, []) is True


def test_high_illegal_move_is_not_legal():
    move = 9
    assert is_legal(move, []) is False


def test_move_is_illegal_if_already_played():
    moves_played = [0]
    move = 0
    assert is_legal(move, moves_played) is False


def test_moves_for_player_one_are_at_even_indices():
    moves_played = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    player_one_moves = []
    assert player_one_moves == [0, 2, 4, 6, 8]


def is_legal(move, moves_played):
    return move >= 0 and move < 9 and move not in moves_played
