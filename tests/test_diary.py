from lib.diary import *

def test_make_snippet_over_5():
    result = make_snippet('Here is a more verbose string, containing more than 5 words.')
    assert result == 'Here is a more verbose...'

def test_make_snippet_under_5():
    result = make_snippet('A few words.')
    assert result == 'A few words.'

def test_make_snippet_5_words():
    result = make_snippet('A string with five words.')
    assert result == 'A string with five words.'

def test_make_snippet_empty_string():
    result = make_snippet('')
    assert result == ''

def test_count_words_normal():
    result = count_words('A string with five words.')
    assert result == 5

def test_count_words_empty():
    result = count_words('')
    assert result == 0
