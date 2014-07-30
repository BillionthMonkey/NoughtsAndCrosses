def test_win():
    moves = [2, 1, 3, 0]
    assert set(moves).issuperset(set([0, 1, 2]))

def test_win_with_two_options():
    moves = [2, 1, 3, 0]
    options = [
        [0, 1, 2],
        [3, 4, 5]
    ]
    assert any([moves == option for option in options])
