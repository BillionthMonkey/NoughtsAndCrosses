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
        number_of_players = 2
        player_one = 0
        player_two = 1

        player_one_moves = moves[player_one::number_of_players]
        for player_one_move in player_one_moves:
            cells[player_one_move] = 'O'

        player_two_moves = moves[player_two::number_of_players]
        for player_two_move in player_two_moves:
            cells[player_two_move] = 'X'

        for i in [0, 3, 6]:
            self._print_border()
            self._print_row(cells[i:i + 3])
        self._print_border()

    def _print_row(self, row):
        print '| ' + ' | '.join(row) + ' |'

    def _print_border(self):
        print '+---+---+---+'
