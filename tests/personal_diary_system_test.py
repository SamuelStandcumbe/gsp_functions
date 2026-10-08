from lib.personal_diary_system_functions import *
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

# These are tests for estimated_reading_time

def test_less_than_200_words():
    text = "I love python so much"
    assert estimated_reading_time(text) == "Estimated reading time: 1 minute"

def test_exactly_200_words():
    text = "I love python so much " * 40
    assert estimated_reading_time(text) == "Estimated reading time: 1 minute"

def test_more_than_200_words():
    text = "I love python so much yipee! " *100
    assert estimated_reading_time(text) == "Estimated reading time: 3 minutes"

# Tests for grammar_checker

def test_no_capital_letter():
    result = grammar_checker("hello, world!")
    assert result == "Hello, world!"

def test_no_punctuation():
    result = grammar_checker("Hello, world")
    assert result == "Hello, world!"

def test_no_punctuation_or_capitalisation():
    result = grammar_checker("hello, world")
    assert result == "Hello, world!"