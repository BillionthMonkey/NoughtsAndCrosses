def test_move_is_legal_if_not_already_played():
	move = 0
	moves_played_so_far = []
	is_legal = move not in moves_played_so_far
	assert is_legal is True

def test_move_is_not_legal_if_already_played():
	assert 0 not in [0]
