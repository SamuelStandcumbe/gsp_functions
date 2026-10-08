from lib.grammar import *

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
grammar_check.check("Hello!") == True
grammer_check.check("hello") == False

b. check to see if the percentage_ggod 
   function returns the correct result
grammar_stats.check("Hello!")
grammer_stats.check("hello!")
grammar_stats.percentage_good() == 50

c. starts with capital, edns with question mark + no capital and question mark

d. starts with capital ends with period +no capital nd period

e. empty string

f. starts with punctuation

g. starts with numbers



4. Implement 
'''