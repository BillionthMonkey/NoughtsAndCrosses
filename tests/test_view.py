import sys
from nac.view import NoughtsAndCrossesView

class TestNoughtsAndCrossesView():
    def setup_method(self, method):
        self.view = NoughtsAndCrossesView()

    def test_win(self, capsys):
        self.view.win()
        self._assert_stdout_is('Congratulations; you won!\n', capsys)

    def test_draw(self, capsys):
        self.view.draw()
        self._assert_stdout_is("It's a draw!\n", capsys)

    def test_report_error(self, capsys):
        message = 'Illegal move.'
        self.view.report_error(message)
        self._assert_stdout_is(message + '\n', capsys)

    def test_reset(self):
        self.view.reset()
        self.fake_board_renderer.render.assert_called_with([])

    def _assert_stdout_is(self, expected, capsys):
        out, err = capsys.readouterr()
        assert out == expected
