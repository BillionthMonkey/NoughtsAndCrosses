import mock

class TestNoughtsAndCrosses():
    def setup_method(self, method):
        self.fake_view = mock.Mock()
        self.fake_model = mock.Mock()
        self.controller = NoughtsAndCrossesController(
            self.fake_model,
            self.fake_view)

    def teardown_method(self, method):
        pass

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
            move_result = self.model.play_move(move)
            self.view.add_move(move)
            if move_result == MoveResult.win:
                self.view.win()
            if move_result == MoveResult.draw:
                self.view.draw()
        else:
            self.view.report_error('Illegal move')
