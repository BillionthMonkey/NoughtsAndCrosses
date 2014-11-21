from model import MoveResult

class NoughtsAndCrossesController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def reset(self):
        self.model.reset()
        self.view.reset()

    def play_move(self, move):
        if self.model.is_legal(move):
            self._play_legal_move(move)
        else:
            self.view.report_error('Illegal move')

    def quit(self):
        self.view.quit()

    def _play_legal_move(self, move):
        move_result = self.model.play_move(move)
        self.view.add_move(move)
        if move_result == MoveResult.win:
            self.view.win()
            self.model.reset()
        if move_result == MoveResult.draw:
            self.view.draw()
