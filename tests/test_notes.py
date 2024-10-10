from lib.notes import *


def test_check_if_function_returns_TODO():
    mynotes = {"#TODO":"Take the bins out", "#DONE": "Washing the dishes up"}
    result = notes_function(mynotes)
    assert result == {"#TODO": "Take the bins out"}

def test_check_if_function_returns_multiple_TODOS():
    mynotes = {"#TODO": "Take the bins out", "#TODO": "Paint the fence", "#DONE": "Wash the dishes up"}
    result = notes_function(mynotes)
    assert result == {"#TODO": "Take the bins out", "#TODO": "Paint the fence"}








#As a user
#So that I can find my tasks among all my notes
#I want to check if a line from my notes includes the string `#TODO`.