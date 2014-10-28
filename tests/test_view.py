import sys
import mock
from nac.view import NoughtsAndCrossesView

class TestNoughtsAndCrossesView():
    def setup_method(self, method):
        self.fake_stdout = mock.Mock()

    def test_win(self, capsys):
        view = NoughtsAndCrossesView()
        view.win()
        out, err = capsys.readouterr()
        assert out == 'Congratulations; you won!\n'

    def test_draw(self, capsys):
        view = NoughtsAndCrossesView()
        view.draw()
        out, err = capsys.readouterr()
        assert out == "It's a draw!\n"

    def test_report_error(self, capsys):
        view = NoughtsAndCrossesView()
        message = 'Illegal move.'
        view.report_error(message)
        out, err = capsys.readouterr()
        assert out == message + '\n'
