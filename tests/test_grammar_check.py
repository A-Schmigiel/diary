from lib.grammar_check import *
import pytest

# empty string -- 'I cannot check what isnt there'
# invalid input (float/int)
# String with correct grammar
# string missing uppercase at start
# string missing end punct
# string ending in innapropriate punct

# def test_wrong_input():
#     with pytest.raises(Exception) as e:
#         grammar_check(42.9) #should throw exception
#     error_message = str(e.value)
#     assert error_message == "I can only check strings, sorry!"

# def test_correct_grammar():
#     assert grammar_check('This is me, using correct grammar!') == "Well done, your grammar is correct!"

# def test_missing_capital():
#     assert grammar_check('oh no! Where is the capitol?') == "Your grammar is incorrect.  Remember to begin your sentences with a capital letter."

# def test_missing_punct():
#     assert grammar_check('Ahhhh! I forgot my puncuation! How can you know when I ask a question') == "Your grammar is incorrect.  Remember to end your sentences with appropriate punctuation."

# def test_other_punct():
#     assert grammar_check('Hmmm...will a smiley face count? :)') == "Your grammar is incorrect.  Remember to end your sentences with appropriate punctuation."
