import itertools


def test_legal_move_is_legal():
    move = 0
    assert is_legal(move, []) is True


def test_illegal_move_is_not_legal():
    move = -1
    assert is_legal(move, []) is False


def test_different_legal_move_is_legal():
    move = 1
    assert is_legal(move, []) is True


def test_high_illegal_move_is_not_legal():
    move = 9
    assert is_legal(move, []) is False


def test_move_is_illegal_if_already_played():
    moves_played = [0]
    move = 0
    assert is_legal(move, moves_played) is False


def test_moves_for_player_one_are_at_even_indices():
    moves_played = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    player_one_moves = moves_for_player(0, moves_played)
    assert player_one_moves == [0, 2, 4, 6, 8]


def test_moves_for_player_two_are_at_odd_indices():
    moves_played = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    player_two_moves = moves_for_player(1, moves_played)
    assert player_two_moves == [1, 3, 5, 7]


def test_player_moves_win():
    player_moves = [0, 1, 2]
    assert is_win(player_moves) is True


def test_player_moves_in_a_different_order_win():
    player_moves = [2, 1, 0]
    assert is_win(player_moves) is True


def test_more_than_three_player_moves_still_wins():
    player_moves = [8, 2, 1, 0]
    assert is_win(player_moves) is True


def test_first_player_played_last_move():
    game_moves = [0, 3, 1, 5, 2]
    assert last_player(game_moves) is 0


def test_second_player_played_last_move():
    game_moves = [0, 1, 2, 3, 4, 5]
    assert last_player(game_moves) is 1


def test_first_player_wins():
    game_moves = [0, 3, 1, 5, 2]
    assert last_move_wins(game_moves) is True


def test_second_player_wins():
    game_moves = [4, 0, 3, 1, 8, 2]
    assert last_move_wins(game_moves) is True


def is_legal(move, moves_played):
    return move >= 0 and move < 9 and move not in moves_played


def moves_for_player(player, moves_played):
    number_of_players = 2
    return moves_played[player::number_of_players]


def is_win(player_moves):
    combinations = itertools.combinations(player_moves, 3)
    winning_moves = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any([sorted(combination) in winning_moves
                for combination in combinations])


def last_player(moves_played):
    return (len(moves_played) + 1) % 2


def last_move_wins(moves_played):
    player = last_player(moves_played)
    player_moves = moves_for_player(player, moves_played)
    return is_win(player_moves)
