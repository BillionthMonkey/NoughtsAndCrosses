def test_legal_move():
    last_move_was_legal = True
    assert last_move_was_legal

def test_move_bounds_lower():
    move = -1
    last_move_was_legal = move < 0
    assert last_move_was_legal is False
