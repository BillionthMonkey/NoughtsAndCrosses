def test_move_is_legal_if_not_already_played():
    nac = _create_noughts_and_crosses()
    assert nac.is_legal(0) is True

def test_move_is_not_legal_if_already_played():
    nac = _create_noughts_and_crosses()
    nac.moves_played_so_far = [0]
    assert nac.is_legal(0) is False

def test_move_is_not_legal_if_below_lower_bound():
    nac = _create_noughts_and_crosses()
    assert nac.is_legal(-1) is False

def test_move_is_not_legal_if_above_upper_bound():
    nac = _create_noughts_and_crosses()
    assert nac.is_legal(9) is False

def test_draw():
    nac = _create_noughts_and_crosses()
    nac.moves_played_so_far = [ 0, 1, 2, 3, 4, 5, 6, 7, 8 ]
    assert nac.is_draw() is True

def test_not_draw():
    nac = _create_noughts_and_crosses()
    nac.moves_played_so_far = [ 0, 1, 2, 3, 4, 5, 6, 7 ]
    assert nac.is_draw() is False

def test_top_row_filled_player_one_is_win():
    _is_win_for_player_one([ 0, 7, 1, 8, 2 ])

def test_middle_row_filled_player_one_is_win():
    _is_win_for_player_one([ 3, 7, 4, 8, 5 ])

def test_bottom_row_filled_player_one_is_win():
    _is_win_for_player_one([ 6, 0, 7, 1, 8 ])

def test_first_column_filled_player_one_is_win():
    _is_win_for_player_one([ 0, 7, 3, 8, 6 ])

def test_second_column_filled_player_one_is_win():
    _is_win_for_player_one([ 1, 6, 4, 8, 7 ])

def test_third_column_filled_player_one_is_win():
    _is_win_for_player_one([ 2, 6, 5, 7, 8 ])

def test_top_left_diagonal_filled_player_one_is_win():
    _is_win_for_player_one([ 0, 7, 4, 6, 8 ])

def test_bottom_left_diagonal_filled_player_one_is_win():
    _is_win_for_player_one([ 2, 7, 4, 8, 6 ])

def test_is_win_for_player_two():
    moves_played_so_far = [ 5, 0, 7, 1, 8, 2 ]
    player_two_moves = moves_played_so_far[1::2]
    result_checker = ResultChecker()
    is_win_for_player_two = result_checker.is_win(player_two_moves)
    assert is_win_for_player_two is True

def _is_win_for_player_one(moves_played_so_far):
    nac = _create_noughts_and_crosses()
    nac.moves_played_so_far = moves_played_so_far
    assert nac.is_win_for_player_one() is True

def _create_noughts_and_crosses():
    return NoughtsAndCrosses(ResultChecker())


class NoughtsAndCrosses:
    def __init__(self, result_checker):
        self.moves_played_so_far = []
        self.max_number_of_moves = 9
        self.result_checker = result_checker

    def is_legal(self, move):
        move_within_bounds = move > -1 and move < self.max_number_of_moves
        move_not_played = move not in self.moves_played_so_far
        return move_within_bounds and move_not_played

    def is_draw(self):
        return len(self.moves_played_so_far) is self.max_number_of_moves

    def is_win_for_player_one(self):
        return self.result_checker.is_win(self._player_one_moves())

    def _player_one_moves(self):
        return set(self.moves_played_so_far[0::2])

class ResultChecker:
    def is_win(self, moves):
        top_row = set([0, 1, 2])
        middle_row = set([3, 4, 5])
        bottom_row = set([6, 7, 8])
        first_column = set([0, 3, 6])
        second_column = set([1, 4, 7])
        third_column = set([2, 5, 8])
        top_left_diagonal = set([0, 4, 8])
        bottom_left_diagonal = set([2, 4, 6])
        return top_row.issubset(moves) \
            or middle_row.issubset(moves) \
            or bottom_row.issubset(moves) \
            or first_column.issubset(moves) \
            or second_column.issubset(moves) \
            or third_column.issubset(moves) \
            or top_left_diagonal.issubset(moves) \
            or bottom_left_diagonal.issubset(moves)
