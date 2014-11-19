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
    def __init__(self):
        self._number_of_players = 2
        self._player_one = 0
        self._player_two = 1

    def render(self, moves):
        cells = [' '] * 9
        self._update_cells(self._player_one, moves, cells)
        self._update_cells(self._player_two, moves, cells)
        row_size = 3
        start_of_rows = [0, 3, 6]
        for i in start_of_rows:
            self._print_border()
            self._print_row(cells[i:i + row_size])
        self._print_border()

    def _update_cells(self, player, moves, cells):
        player_moves = moves[player::self._number_of_players]
        symbol = 'O' if player is self._player_one else 'X'
        for player_move in player_moves:
            cells[player_move] = symbol

    def _print_row(self, row):
        print '| ' + ' | '.join(row) + ' |'

    def _print_border(self):
        print '+---+---+---+'
