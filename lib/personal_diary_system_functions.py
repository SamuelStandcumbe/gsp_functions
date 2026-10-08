import math

def make_snippet(text):
    if len(text.split()) <= 5:
        return text
    else:
        short_text = " ".join(text.split()[:5]) + "..."
        return short_text

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
'''
class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        pass

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        pass

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        pass

'''