import sys
import mock
from nac.view import NoughtsAndCrossesView

class TestNoughtsAndCrossesView():
    def test_win(self):
        fake_stdout = mock.Mock()
        sys.stdout = fake_stdout
        view = NoughtsAndCrossesView()
        view.win()
        fake_stdout.write.assert_any_call('Congratulations; you won!')

    def test_draw(self):
        view = NoughtsAndCrossesView()
        view.draw()
