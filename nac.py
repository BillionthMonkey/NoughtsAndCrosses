def test_legal_move():
    assert is_legal(1)

def test_move_bounds_lower():
    assert is_legal(-1) is False

def test_move_lower_boundary():
    assert is_legal(0) is True


def is_legal(move):
    return move >= 0
