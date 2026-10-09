
1. Describe the problem
" "

2. Design the function signature
Function name |  
Parameters    |
Output        |
Side Effects  |

3. Create examples as tests
" "

4. Implement 
______________________________________

1. Describe the problem
"As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute. "

2. Design the function signature
Function name | estimate_reading_time
Parameters    | text as a string
Output        | the estimated reading time
Side Effects  | None

3. Create examples as tests
" enter a string with less then 200 words, and it should return less than one minute"
estimate_reading_time(text) ==> "Less than one minute"

" enter a string with 200 words and and it should return 1 minute"
estimate_reading_time(text) ==> "One minute"

"enter a string with ore than 200 words and tand it should return more than one minute"
estimate_reading_time(text) ==> "More than one minute"

4. Implement 
___________________________

1. Describe the problem
"As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark. "

2. Design the function signature
Function name | grammar_checker
Parameters    | text as a string
Output        | capitalised text and has punctuation at the end
Side Effects  | change the text variable

3. Create examples as tests
"input text without a capital letter, but with punctuation"
grammar_checker("hello, world!) ==> "Hello, world!"

"input text with a caputal letter but no punctuation"
grammar_cecker("Hello, world) ==> "Hello, world!"

"No punctuation or capitalisation"
grammar_checker("hello, world) ==> "Hello, world!"

4. Implement 

---------
UNIT 4
---------

# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Reminder:
    # User-facing properties:
    #   name: string

    def __init__(self, name):
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets the name property of the self object
        pass # No code here yet

    def remind_me_to(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass # No code here yet

    def remind(self):
        # Returns:
        #   A string reminding the user to do the task
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a name and a task
#remind reminds the user to do the task
"""
reminder = Reminder("Kay")
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"

"""
Given a name and no task
#remind raises an exception
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
