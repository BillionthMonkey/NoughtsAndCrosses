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
        cells = [' '] * 9
        player_one_moves = moves[0::2]
        player_two_moves = moves[1::2]
        for player_one_move in player_one_moves:
            cells[player_one_move] = 'O'
        for player_two_move in player_two_moves:
            cells[player_two_move] = 'X'
        self._print_border()
        self._print_row(cells[0], cells[1], cells[2])
        self._print_border()
        self._print_row(cells[3], cells[4], cells[5])
        self._print_border()
        self._print_row(cells[6], cells[7], cells[8])
        self._print_border()

    def _print_row(self, first_column, second_column, third_column):
        print '| ' + first_column + ' | ' + second_column + ' | ' + third_column + ' |'

    def _print_border(self):
        print '+---+---+---+'
