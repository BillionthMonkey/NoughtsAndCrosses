class NoughtsAndCrossesView():
    def __init__(self, board_renderer):
        self._board_renderer = board_renderer
        self._moves = []

    def win(self):
        print 'Congratulations; you won!'

    def draw(self):
        print "It's a draw!"

    def reset(self):
        self._board_renderer.render([])

    def add_move(self, move):
        self._moves.append(move)
        self._board_renderer.render(self._moves)

    def report_error(self, message):
        print message


class BoardRenderer():
    def render(self, moves):
        self._print_border()
        if not moves:
            self._print_row()
        else:
            print '| O |   |   |'
        for i in range(2):
            self._print_border()
            self._print_row()
        self._print_border()

    def _print_row(self):
        print '|   |   |   |'

    def _print_border(self):
        print '+---+---+---+'
