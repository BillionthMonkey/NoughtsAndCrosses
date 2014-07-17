def test_move_is_legal_if_not_already_played():
	nac = NoughtsAndCrosses()
	assert nac.is_legal(0) is True

def test_move_is_not_legal_if_already_played():
	nac = NoughtsAndCrosses()
	nac.moves_played_so_far = [0]
	assert nac.is_legal(0) is False

def test_move_is_not_legal_if_below_lower_bound():
	nac = NoughtsAndCrosses()
	assert nac.is_legal(-1) is False

def test_move_is_not_legal_if_above_upper_bound():
	nac = NoughtsAndCrosses()
	assert nac.is_legal(9) is False

def test_draw():
	nac = NoughtsAndCrosses()
	nac.moves_played_so_far = [ 0, 1, 2, 3, 4, 5, 6, 7, 8 ]
	assert nac.is_draw() is True

def test_not_draw():
	nac = NoughtsAndCrosses()
	nac.moves_played_so_far = [ 0, 1, 2, 3, 4, 5, 6, 7 ]
	assert nac.is_draw() is False

def test_top_row_filled_player_one_is_win():
	nac = NoughtsAndCrosses()
	nac.moves_played_so_far = [ 0, 7, 1, 8, 2 ]
	assert nac.is_win_for_player_one() is True

def test_middle_row_filled_player_one_is_win():
	nac = NoughtsAndCrosses()
	nac.moves_played_so_far = [ 3, 7, 4, 8, 5 ]
	assert nac.is_win_for_player_one() is True

def test_bottom_row_filled_player_one_is_win():
	nac = NoughtsAndCrosses()
	nac.moves_played_so_far = [ 6, 0, 7, 1, 8 ]
	assert nac.is_win_for_player_one() is True


class NoughtsAndCrosses:
	def __init__(self):
		self.moves_played_so_far = []
		self.max_number_of_moves = 9

	def is_legal(self, move):
		move_within_bounds = move > -1 and move < self.max_number_of_moves
		move_not_played = move not in self.moves_played_so_far
		return move_within_bounds and move_not_played

	def is_draw(self):
		return len(self.moves_played_so_far) is self.max_number_of_moves

	def is_win_for_player_one(self):
		top_row = set([0, 1, 2])
		middle_row = set([3, 4, 5])
		return self._is_win_for_player_one(top_row) \
			or self._is_win_for_player_one(middle_row)

	def _is_win_for_player_one(self, pattern):
		player_one_moves = set(self.moves_played_so_far[0::2])
		return pattern.issubset(player_one_moves)
