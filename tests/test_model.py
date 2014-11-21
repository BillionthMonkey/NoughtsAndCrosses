import mock
from nac.model import NoughtsAndCrossesModel, ResultChecker, MoveResult

class TestNoughtsAndCrossesModel():
    def setup_method(self, method):
        self.fake_result_checker = mock.Mock()
        self.model = NoughtsAndCrossesModel(self.fake_result_checker, 9)

    def test_is_legal_returns_true_with_legal_move(self):
        assert self.model.is_legal(0) is True

    def test_is_legal_returns_false_with_illegal_move(self):
        assert self.model.is_legal(-1) is False

    def test_is_legal_returns_false_with_another_illegal_move(self):
        assert self.model.is_legal(9) is False

    def test_is_legal_returns_false_if_move_already_played(self):
        self.model.play_move(0)
        assert self.model.is_legal(0) is False

    def test_is_legal_returns_false_if_move_historically_played(self):
        self.model.play_move(0)
        self.model.play_move(1)
        assert self.model.is_legal(0) is False

    def test_play_move_calls_result_checker_with_moves_played(self):
        self.model.play_move(0)
        self.model.play_move(1)
        self.model.play_move(2)
        self.fake_result_checker.check_result.assert_called_with([0, 1, 2])

    def test_play_move_returns_the_same_value_as_check_result(self):
        self.fake_result_checker.check_result.return_value \
            = MoveResult.no_result
        assert self.model.play_move(0) is MoveResult.no_result

    def test_reset_clears_move_history(self):
        self.model.reset()


class TestResultChecker():
    def setup_method(self, method):
        winning_moves = [
            [ 0, 1, 2 ], [ 3, 4, 5 ], [ 6, 7, 8 ],
            [ 0, 3, 6 ], [ 1, 4, 7 ], [ 2, 5, 8 ],
            [ 0, 4, 8 ], [ 2, 4, 6 ]
        ]
        number_of_cells = 9
        self.result_checker = ResultChecker(winning_moves, number_of_cells)

    def test_no_result(self):
        moves_played = [0]
        assert self.result_checker.check_result(moves_played) \
            is MoveResult.no_result

    def test_win_for_player_one(self):
        moves_played = [0, 3, 1, 4, 2]
        assert self.result_checker.check_result(moves_played) is MoveResult.win

    def test_win_for_player_two(self):
        moves_played = [6, 0, 3, 1, 4, 2]
        assert self.result_checker.check_result(moves_played) is MoveResult.win

    def test_not_win_with_complete_row(self):
        moves_played = [0, 1, 2]
        assert self.result_checker.check_result(moves_played) \
            is MoveResult.no_result

    def test_draw(self):
        moves_played = [0, 1, 2, 4, 3, 6, 5, 8, 7]
        assert self.result_checker.check_result(moves_played) is MoveResult.draw

    def test_win_on_last_move(self):
        moves_played = [0, 1, 2, 3, 4, 5, 7, 6, 8]
        assert self.result_checker.check_result(moves_played) is MoveResult.win
