from lib.grammar import *
import pytest
'''
1. Describe the problem
" i want a class  with two functions, check, which
should return true if text begins with a capital
letter and ends with a punctuation mark, and 
precentage_good, which returns the percentage of
texts chekced that have passed the 'check' method
"

2. Design the  signature
Function name |  Class name = GrammarStats():. 
                 Function names: check():
                                 percentage_good():
Parameters    | text, a string, 
Output        | boolean (true) and int (the percentage as a number)
Side Effects  | changes the text str

3. Create examples as tests
a. see if the check function works (CAPITAL AND EXCLAIMATION MARK + NO CAPITAL AND EXCLIMATION MARK)
grammar_check.check("Hello!") == True.    y
grammer_check.check("hello") == False

b. check to see if the percentage_ggod 
   function returns the correct result
grammar_stats.check("Hello!")
grammer_stats.check("hello!")
grammar_stats.percentage_good() == 50

c. starts with capital, edns with question mark + no capital and question mark y

d. starts with capital ends with period +no capital nd period y

e. empty string y

f. starts with punctuation y

g. starts with numbers y



4. Implement 
'''
#testing that true only returns if there is both a capitalised first letter and a punctuation mark at the end
def test_capital_and_exclaimation():
    grammar = GrammarStats()
    assert grammar.check("Hello!") == True
    assert grammar.check("hello!") == False
    assert grammar.check("hello") == False

def test_capital_and_question():
    grammar = GrammarStats()
    assert grammar.check("Hello?") == True
    assert grammar.check("hello?") == False
    assert grammar.check("hello") == False

def test_capital_and_period():
    grammar = GrammarStats()
    assert grammar.check("Hello.") == True
    assert grammar.check("hello.") == False
    assert grammar.check("hello") == False

def test_start_with_punctuation():
    grammar = GrammarStats()
    assert grammar.check("!Hello") == False
    assert grammar.check("!hello") == False
    assert grammar.check("?Hello") == False
    assert grammar.check("?hello") == False
    assert grammar.check(".Hello") == False
    assert grammar.check(".hello") == False

def test_input_type():
    grammar = GrammarStats()
    with pytest.raises(ValueError) as e:
        grammar.check(123)
    error_message = str(e.value)
    assert error_message == "Input must be a string"

def test_cannot_be_empty():
    grammar = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar.check(" ")
    error_message = str(e.value)
    assert error_message == "Imput cannot be empty"

"tests for percentage"
'''
a. no checks and you run percentage_good should return an error
b. one check passess should return 100
c. one check fails should return 0
d. multiple checks should return the correct percentage 
    - (2 fail 1 success - 33.33)

counter should be put above the check function to initialise them. 
counters should only be added to after the validation.
at the start of the perccentage_good function i check if total checks is 0, 
then raise error if it is. invalid imports shuld raise errors and i test by 
importing pytest
'''

def test_percentage_is_correct():
    grammar = GrammarStats()
    grammar.check("Hello!")
    grammar.check("hello")
    assert grammar.percentage_good() == 50

def test_percentage_with_no_checks():
    grammar = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar.percentage_good()
    error_message = str(e.value)
    assert error_message == "Total checks cannot be 0"

def test_percentage_one_success():
    grammar = GrammarStats()
    grammar.check("Hello!")
    assert grammar.percentage_good() == 100

def test_percentage_one_failure():
    grammar = GrammarStats()
    grammar.check("hello")
    assert grammar.percentage_good() == 0

def test_percentage_multiple_checks():
    grammar = GrammarStats()
    grammar.check("hello")
    grammar.check("hello")
    grammar.check("Hello!")
    assert grammar.percentage_good() == 33.33