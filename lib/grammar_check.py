# def grammar_check(text_to_check):
#     end_punct = '!.?'
#     if type(text_to_check) is not str:
#         raise Exception("I can only check strings, sorry!")
#     if text_to_check[-1] in end_punct: # checking if the end puncuation is correct
#         if text_to_check[0] == text_to_check.upper()[0]: # checking if the capital is in place
#             return "Well done, your grammar is correct!"
#         else:
#              return "Your grammar is incorrect.  Remember to begin your sentences with a capital letter."
#     else: # if the end punct is not correct
#         if text_to_check[0] != text_to_check.upper()[0]: # checking if the capital is missing
#             return "Your grammar is incorrect.  Remember to begin your sentences with a capital letter and end them with appropriate punctuation."
#         else:
#             return "Your grammar is incorrect.  Remember to end your sentences with appropriate punctuation."

class GrammarStats():
    def __init__(self):
        self.passed_checks = 0
        self.failed_checks = 0

    def check(self, text):
        if not isinstance(text, str):
            return None
        else:
            result = text[0].isupper() and text[-1] in '?.!' 
            if result == True:
                self.passed_checks += 1 
            else:
                self.failed_checks += 1
            return result
        

    def percentage_good(self):
        total = self.passed_checks + self.failed_checks
        if self.passed_checks != 0:
            return round((self.passed_checks/total*100), 2)
        