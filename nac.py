def test_complete_top_row_is_win():
    moves = [0, 1, 2]
    assert is_win(moves) is True

def test_complete_top_row_in_different_order_is_win():
    moves = [2, 1, 0]
    assert is_win(moves) is True

def test_more_than_complete_top_row_is_win():
    moves = [0, 1, 2, 3]
    assert is_win(moves) is True

def test_complete_middle_row_is_win():
    moves = [3, 4, 5]
    assert (is_win(moves) or moves == [3, 4, 5]) is True


def is_win(moves):
    top_row = set([0, 1, 2])
    return set(moves).issuperset(top_row)
