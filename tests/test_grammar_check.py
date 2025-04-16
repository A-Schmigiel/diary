from lib.grammar_check import *
import pytest # type: ignore

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

grammar_checker = GrammarStats()

def test_GrammarStats_correct():
    assert grammar_checker.check('This is a proper sentence.') == True

def test_GrammarStats_incorrect():
    assert grammar_checker.check('this is not a proper sentence') == False

def test_GrammarStats_no_cap():
    assert grammar_checker.check('is this correct?') == False

def test_GrammarStats_no_pun():
    assert grammar_checker.check('Maybe this is right') == False

def test_GrammarStats_wrong_pun():
    assert grammar_checker.check('Womp womp,') == False

def test_GrammarStats_moved_pun():
    assert grammar_checker.check('Hmm. Maybe? nahhhhh') == False

def test_question_mark():
    assert grammar_checker.check('Is this right?') == True

def test_exclaimation():
    assert grammar_checker.check('Yes, it is!') == True

def test_all_caps():
    assert grammar_checker.check('AM I A SENTENCE NOW?') == True

def test_all_pun():
    assert grammar_checker.check('...?!???') == False

def test_not_a_str():
    assert grammar_checker.check(12) == None



def test_GrammarStats_():
    assert grammar_checker.percentage_good() == 40.00