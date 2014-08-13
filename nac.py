import mock

def test_playing_legal_move_updates_view():
    fake_view = mock.Mock()
    controller = NoughtsAndCrossesController(fake_view)
    controller.play_move(0)
    fake_view.add_move.assert_called_with(0)

class NoughtsAndCrossesController:
    def __init__(self, view):
        self.view = view

    def play_move(self, move):
        self.view.add_move(move)
