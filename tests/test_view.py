import sys
import mock
from nac.view import NoughtsAndCrossesView

class TestNoughtsAndCrossesView():
    def setup_method(self, method):
        self.fake_stdout = mock.Mock()

    def test_win(self, capsys):
        view = NoughtsAndCrossesView()
        view.win()
        self._assert_stdout_is('Congratulations; you won!\n', capsys)

    def test_draw(self, capsys):
        view = NoughtsAndCrossesView()
        view.draw()
        self._assert_stdout_is("It's a draw!\n", capsys)

    def test_report_error(self, capsys):
        view = NoughtsAndCrossesView()
        message = 'Illegal move.'
        view.report_error(message)
        self._assert_stdout_is(message + '\n', capsys)

    def _assert_stdout_is(self, expected, capsys):
        out, err = capsys.readouterr()
        assert out == expected
