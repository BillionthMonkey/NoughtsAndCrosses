import mock

def test_playing_legal_move_updates_view():
    fake_view = mock.Mock()
    controller = NoughtsAndCrossesController()
    controller.play_move(0)
    fake_view.add_move.assert_called_with(0)

class NoughtsAndCrossesController:
    def play_move(self, move):
        pass
