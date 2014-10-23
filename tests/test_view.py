import sys
import mock
from nac.view import NoughtsAndCrossesView

class TestNoughtsAndCrossesView():
    def setup_method(self, method):
        self.fake_stdout = mock.Mock()

    def test_win(self):
        sys.stdout = self.fake_stdout
        view = NoughtsAndCrossesView()
        view.win()
        self.fake_stdout.write.assert_any_call('Congratulations; you won!')

    def test_draw(self):
        sys.stdout = self.fake_stdout
        view = NoughtsAndCrossesView()
        view.draw()
        self.fake_stdout.write.assert_any_call("It's a draw!")

    def test_report_error(self):
        sys.stdout = self.fake_stdout
        view = NoughtsAndCrossesView()
        message = 'Illegal move.'
        view.report_error(message)
        self.fake_stdout.write.assert_any_call(message)
