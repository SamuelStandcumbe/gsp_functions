from lib.personal_diary_system import *
import pytest

# tests for make_snippet
def test_five_words():
    result = make_snippet("The quick brown fox jumps")
    assert result == "The quick brown fox jumps"

def test_more_than_five_words():
    result = make_snippet("The quick brown fox jumps over")
    assert result == "The quick brown fox jumps..."

def test_less_than_5_words():
    result = make_snippet("The quick brown fox")
    assert result == "The quick brown fox"

def test_empty_string():
    result = make_snippet("")
    assert result == ""

#tests count_words
def test_returns_number_of_words():
    result = count_words("Ethan is great")
    assert result == 3

def test_input_is_integer():
    with pytest.raises(Exception) as e:
        count_words(123)
    assert str(e.value) == "Input needs to be a string"