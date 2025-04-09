# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_As a user_
_So that I can manage my time_
_I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute._

## 2. Design the Function Signature


```python
def time_estimation(text_to_read):
    """Creates an estimation of how long it will take to read a string
    Parameters: 
        text_to_read: a string containing words
    Returns:
        the estimated time it would take the user to read in minutes (assuming they read 200 wpm)
    Side effects: 
        None."""
    return <<time estimation in minutes>>
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE
"""
Given a string of 200 words, returns the integer 1.

Given an empty string, returns 'less than one minute'

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
