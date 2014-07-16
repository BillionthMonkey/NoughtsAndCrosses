def test_move_is_legal_if_not_already_played():
	assert is_legal(0, []) is True

def test_move_is_not_legal_if_already_played():
	assert is_legal(0, [0]) is False


def is_legal(move, moves_played_so_far):
	return move not in moves_played_so_far
