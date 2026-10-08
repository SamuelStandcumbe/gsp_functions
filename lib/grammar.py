class GrammarStats():
    def __init__(self):
        self.successful_check = 0
        self.failed_check = 0
        self.total_checks = 0

    def check(self, text):
        if type(text) != str:
            raise ValueError("Input must be a string")
        elif text == " ":
            raise Exception("Imput cannot be empty")
        
        punctuation = ["!", ".", "?"]
        if text[0].islower() or text[-1] not in punctuation:
            self.failed_check += 1
            self.total_checks += 1
            return False
        else:
            self.successful_check += 1
            self.total_checks += 1
            return True

    def percentage_good(self): 
        if self.total_checks == 0:
            raise Exception("Total checks cannot be 0")
        percentage = self.successful_check / self.total_checks * 100
        return round(percentage, 2)