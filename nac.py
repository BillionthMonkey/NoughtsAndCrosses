import mock

def test_playing_legal_move_updates_view():
    fake_view = mock.Mock()
    fake_model = mock.Mock()
    controller = NoughtsAndCrossesController(fake_model, fake_view)
    controller.play_move(0)
    fake_view.add_move.assert_called_with(0)

def test_playing_illegal_move_does_not_update_view():
    fake_view = mock.Mock()
    fake_model = mock.Mock()
    fake_model.is_legal.return_value = False
    controller = NoughtsAndCrossesController(fake_model, fake_view)
    controller.play_move(42)
    assert not fake_view.add_move.called

class NoughtsAndCrossesController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def play_move(self, move):
        if self.model.is_legal(move):
            self.view.add_move(move)
