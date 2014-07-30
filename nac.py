def test_complete_top_row_is_win():
    moves = [0, 1, 2]
    top_row = [0, 1, 2]
    assert moves == top_row

def test_complete_top_row_in_different_order_is_win():
    moves = [2, 1, 0]
    top_row = [0, 1, 2]
    assert set(moves) == set(top_row)

def test_more_than_complete_top_row_is_win():
    moves = [0, 1, 2, 3]
    top_row = [0, 1, 2]
    assert moves == top_row
