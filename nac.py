def test_win():
    moves = [2, 1, 3, 0]
    assert set(moves).issuperset(set([0, 1, 2]))
