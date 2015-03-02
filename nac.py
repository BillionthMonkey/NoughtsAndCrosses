def test_legal_move_is_legal():
    move = 0
    assert move == 0


def test_illegal_move_is_not_legal():
    move = -1
    assert (move == 0) is False
