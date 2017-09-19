from main import group_input, can_make_word, is_empty


def test_group():
    assert group_input('abccab') == {'a': 2, 'b': 2, 'c': 2}


def test_is_empty():
    assert is_empty({'a': 0, 'b': 0}) is True
    assert is_empty({'a': 0, 'b': 1}) is False


def test_can_make_word():
    assert can_make_word('abc', 'abc') is True
    assert can_make_word('abcc', 'abcc') is True
    assert can_make_word('abc', 'abcc') is True
    assert can_make_word('abcd', 'abcc') is False
    assert can_make_word('abccc', 'abcc') is False
