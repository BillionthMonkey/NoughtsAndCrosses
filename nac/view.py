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
        first_column = ' '
        if len(moves) is 1:
            first_column = 'O'
        elif len(moves) is 2:
            first_column = 'X'
        second_column = 'O' if len(moves) is 2 else ' '
        self._print_row(first_column, second_column)
        for i in range(2):
            self._print_border()
            self._print_row(' ', ' ')
        self._print_border()

    def _print_row(self, first_column, second_column):
        print '| ' + first_column + ' | ' + second_column + ' |   |'

    def _print_border(self):
        print '+---+---+---+'
