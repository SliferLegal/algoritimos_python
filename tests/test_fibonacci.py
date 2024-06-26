from scripts.fibonacci import fibonnacci

def test_first_10_numbers():
    res = fibonacci (10)
    assert res == (1, 2, 3, 5, 8, 13, 21, 34)