import mock

class TestNoughtsAndCrossesController():
    def setup_method(self, method):
        self.fake_view = mock.Mock()
        self.fake_model = mock.Mock()
        self.controller = NoughtsAndCrossesController(
            self.fake_model,
            self.fake_view)

    def test_playing_legal_move_updates_view(self):
        self.fake_model.is_legal.return_value = True
        self.controller.play_move(0)
        self.fake_view.add_move.assert_called_with(0)

    def test_playing_illegal_move_does_not_update_view(self):
        self.fake_model.is_legal.return_value = False
        self.controller.play_move(42)
        assert not self.fake_view.add_move.called

    def test_playing_illegal_move_reports_error_in_view(self):
        self.fake_model.is_legal.return_value = False
        self.controller.play_move(-1)
        self.fake_view.report_error.assert_called_with('Illegal move')

    def test_playing_legal_move_calls_model(self):
        self.fake_model.is_legal.return_value = True
        self.controller.play_move(2)
        self.fake_model.play_move.assert_called_with(2)

    def test_playing_move_that_wins_updates_view(self):
        self.fake_model.is_legal.return_value = True
        self.fake_model.play_move.return_value = MoveResult.win
        self.controller.play_move(4)
        assert self.fake_view.win.called
        assert not self.fake_view.draw.called

    def test_playing_move_that_draws_updates_view(self):
        self.fake_model.is_legal.return_value = True
        self.fake_model.play_move.return_value = MoveResult.draw
        self.controller.play_move(4)
        assert self.fake_view.draw.called
        assert not self.fake_view.win.called


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


class MoveResult:
    no_result = 0
    win = 1
    draw = 2


class NoughtsAndCrossesController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def play_move(self, move):
        if self.model.is_legal(move):
            self._play_legal_move(move)
        else:
            self.view.report_error('Illegal move')

    def _play_legal_move(self, move):
        move_result = self.model.play_move(move)
        self.view.add_move(move)
        if move_result == MoveResult.win:
            self.view.win()
        if move_result == MoveResult.draw:
            self.view.draw()


class NoughtsAndCrossesModel():
    def __init__(self, result_checker, number_of_cells):
        self._result_checker = result_checker
        self._moves_played = []
        self._number_of_cells = number_of_cells

    def is_legal(self, move):
        return move in range(self._number_of_cells) \
            and move not in self._moves_played

    def play_move(self, move):
        self._moves_played.append(move)
        return self._result_checker.check_result(self._moves_played)


class ResultChecker():
    def __init__(self, winning_moves, number_of_cells):
        self._winning_moves = winning_moves
        self._number_of_cells = number_of_cells
        self._number_of_players = 2

    def check_result(self, moves_played):
        current_player_moves = self._get_current_player_moves(moves_played)
        if self._current_player_wins(current_player_moves):
            return MoveResult.win
        if len(moves_played) is self._number_of_cells:
            return MoveResult.draw
        return MoveResult.no_result

    def _current_player_wins(self, moves):
        return any([self._moves_match(moves, pattern) 
            for pattern in self._winning_moves])

    @staticmethod
    def _moves_match(played, pattern):
        return set(played).issuperset(set(pattern))

    def _get_current_player_moves(self, moves_played):
        current_player = self._get_current_player(moves_played)
        return moves_played[current_player::self._number_of_players]

    def _get_current_player(self, moves_played):
        return (len(moves_played) - 1) % self._number_of_players
