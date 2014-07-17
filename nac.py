def test_move_is_legal_if_not_already_played():
	nac = NaughtsAndCrosses()
	assert nac.is_legal(0) is True

def test_move_is_not_legal_if_already_played():
	nac = NaughtsAndCrosses()
	nac.moves_played_so_far = [0]
	assert nac.is_legal(0) is False

def test_move_is_not_legal_if_below_lower_bound():
	nac = NaughtsAndCrosses()
	assert nac.is_legal(-1) is False

def test_move_is_not_legal_if_above_upper_bound():
	nac = NaughtsAndCrosses()
	assert nac.is_legal(9) is False

def test_draw():
	nac = NaughtsAndCrosses()
	nac.moves_played_so_far = [ 0, 1, 2, 3, 4, 5, 6, 7, 8 ]
	assert nac.is_draw() is True

def test_not_draw():
	nac = NaughtsAndCrosses()
	nac.moves_played_so_far = [ 0, 1, 2, 3, 4, 5, 6, 7 ]
	assert nac.is_draw() is False

def test_top_row_filled_is_win():
	nac = NaughtsAndCrosses()
	nac.moves_played_so_far = [ 0, 7, 1, 8, 2 ]
	assert not set([0, 1, 2]).issubset(set(nac.moves_played_so_far[0::2]))


class NaughtsAndCrosses:
	def __init__(self):
		self.moves_played_so_far = []
		self.max_number_of_moves = 9

	def is_legal(self, move):
		move_within_bounds = move > -1 and move < self.max_number_of_moves
		move_not_played = move not in self.moves_played_so_far
		return move_within_bounds and move_not_played

	def is_draw(self):
		return len(self.moves_played_so_far) is self.max_number_of_moves
