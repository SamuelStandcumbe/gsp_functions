
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