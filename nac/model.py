class NoughtsAndCrossesModel():
    def __init__(self, result_checker, number_of_cells):
        self._result_checker = result_checker
        self._moves_played = []
        self._number_of_cells = number_of_cells

    def is_legal(self, move):
        return move in range(self._number_of_cells) \
            and move not in self._moves_played

    def play_move(self, move):
        self._moves_played.append(move)
        return self._result_checker.check_result(self._moves_played)


class ResultChecker():
    def __init__(self, winning_moves, number_of_cells):
        self._winning_moves = winning_moves
        self._number_of_cells = number_of_cells
        self._number_of_players = 2

    def check_result(self, moves_played):
        if self._current_player_wins(moves_played):
            return MoveResult.win
        if self._is_draw(moves_played):
            return MoveResult.draw
        return MoveResult.no_result

    def _current_player_wins(self, moves):
        current_player_moves = self._get_current_player_moves(moves)
        return any([self._moves_match(current_player_moves, pattern) 
            for pattern in self._winning_moves])

    @staticmethod
    def _moves_match(played, pattern):
        return set(played).issuperset(set(pattern))

    def _get_current_player_moves(self, moves_played):
        current_player = self._get_current_player(moves_played)
        return moves_played[current_player::self._number_of_players]

    def _get_current_player(self, moves_played):
        return (len(moves_played) - 1) % self._number_of_players

    def _is_draw(self, moves_played):
        if len(moves_played) is self._number_of_cells:
            return MoveResult.draw


class MoveResult:
    no_result = 0
    win = 1
    draw = 2
