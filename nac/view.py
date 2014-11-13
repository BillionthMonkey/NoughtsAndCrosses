class NoughtsAndCrossesView():
    def __init__(self, board_renderer):
        self._board_renderer = board_renderer

    def win(self):
        print 'Congratulations; you won!'

    def draw(self):
        print "It's a draw!"

    def reset(self):
        self._board_renderer.render([])

    def add_move(self, move):
        self._board_renderer.render([move])

    def report_error(self, message):
        print message
