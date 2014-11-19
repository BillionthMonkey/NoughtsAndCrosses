import sys
import mock
from nac.view import NoughtsAndCrossesView, BoardRenderer

class TestNoughtsAndCrossesView():
    def setup_method(self, method):
        self.fake_board_renderer = mock.Mock()
        self.view = NoughtsAndCrossesView(self.fake_board_renderer)

    def test_win(self, capsys):
        self.view.win()
        assert_stdout_is('Congratulations; you won!\n', capsys)

    def test_draw(self, capsys):
        self.view.draw()
        assert_stdout_is("It's a draw!\n", capsys)

    def test_report_error(self, capsys):
        message = 'Illegal move.'
        self.view.report_error(message)
        assert_stdout_is(message + '\n', capsys)

    def test_reset(self):
        self.view.reset()
        self.fake_board_renderer.render.assert_called_with([])

    def test_add_move(self):
        self.view.add_move(0)
        self.fake_board_renderer.render.assert_called_with([0])

    def test_add_different_move(self):
        self.view.add_move(1)
        self.fake_board_renderer.render.assert_called_with([1])

    def test_add_a_second_move(self):
        self.view.add_move(0)
        self.view.add_move(1)
        self.fake_board_renderer.render.assert_called_with([0, 1])


class TestBoardRenderer():
    def test_empty_board(self, capsys):
        board_renderer = BoardRenderer()
        board_renderer.render([])
        assert_stdout_is('+---+---+---+\n' \
                         '|   |   |   |\n' \
                         '+---+---+---+\n' \
                         '|   |   |   |\n' \
                         '+---+---+---+\n' \
                         '|   |   |   |\n' \
                         '+---+---+---+\n',
                         capsys)

    def test_single_move(self, capsys):
        board_renderer = BoardRenderer()
        board_renderer.render([0])
        assert_stdout_is('+---+---+---+\n' \
                         '| O |   |   |\n' \
                         '+---+---+---+\n' \
                         '|   |   |   |\n' \
                         '+---+---+---+\n' \
                         '|   |   |   |\n' \
                         '+---+---+---+\n',
                         capsys)


def assert_stdout_is(expected, capsys):
    out, err = capsys.readouterr()
    assert out == expected
