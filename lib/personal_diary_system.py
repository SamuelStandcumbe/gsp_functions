import math

'''
A function called make_snippet that takes a 
string as an argument and returns 
the first five words and then a '...' 
if there are more than that.
'''

def make_snippet(text):
    if len(text.split()) <= 5:
        return text
    else:
        short_text = " ".join(text.split()[:5]) + "..."
        return short_text

    """
    A function called count_words that takes a 
    string as an argument and returns the number 
    of words in that string.
    """

def count_words(word):
    if not isinstance(word, str):
        raise Exception("Input needs to be a string")
    else:
        return len(word.split())

def estimated_reading_time(text, wpm=200):
    words = len(text.split())
    
    if words == 0:
        return "Estimated reading time: 0 minutes"
    minutes = math.ceil(words / wpm)
    if minutes == 1:
        return "Estimated reading time: 1 minute"
    else:
        return f"Estimated reading time: {minutes} minutes"

def grammar_checker(text):
    if type(text) != str:
        raise Exception("Input must be a string!")

    formatted_text = text[0].upper() + text[1:]

    if formatted_text[-1] in [".", "!", "?"]:
        return formatted_text
    else:
        return formatted_text + "!"
