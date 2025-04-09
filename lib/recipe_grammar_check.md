# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_As a user_
_So that I can improve my grammar_
_I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark._

## 2. Design the Function Signature


```python
def grammar_check(text_to_check):
    """Checks that a text begins with a capital letter and ends with a suitable sentence-end punctuation mark.
    Parameters: 
        text_to_check: a string containing words
    Returns:
        a string about whether the text was grammatically correct or not
    Side effects: 
        None."""
    return <<grammar info str>>
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE
"""
Given a string starting with a lowercase letter:
    return False

Given an empty string:
    return "I cannot check what is not there"

Given a different data type, throws an error

"""

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
