def test_move_is_legal_if_not_already_played():
	assert is_legal(0, []) is True

def test_move_is_not_legal_if_already_played():
	assert is_legal(0, [0]) is False

def test_move_is_not_legal_if_below_lower_bound():
	assert is_legal(-1, []) is False

def test_move_is_not_legal_if_above_upper_bound():
	assert is_legal(9, []) is False


def is_legal(move, moves_played_so_far):
	move_within_bounds = move > -1 and move < 9
	move_not_played = move not in moves_played_so_far
	return move_within_bounds and move_not_played
