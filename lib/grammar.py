class GrammarStats():
    def __init__(self):
        pass

    def check(self, text):
        if type(text) != str:
            raise ValueError("Input must be a string")
        elif text == " ":
            raise Exception("Imput cannot be empty")
        
        punctuation = ["!", ".", "?"]
        if text[0].islower() or text[-1] not in punctuation:
            return False
        else:
            return True

    def precentage_good(self):  