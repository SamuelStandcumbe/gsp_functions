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