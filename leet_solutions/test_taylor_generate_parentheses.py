import pudb
from taylor_generate_parentheses import generate_parentheses

# [1 2 3 2 1 0]
# [+ + + - - -]
# 1. if cumsum is ever negative it's not well formed
# 2. if it ends in anything but 0 it's not well formed

# The first opening paren can not move or it'd break #1
# The second opening paren can only move one spot otherwise it'd break #1
# The third opening paren can only move two spots otherwise it'd break #1


def test_generate_parentheses():
    pudb.set_trace()
    parens = list(generate_parentheses(0))
    parens = list(generate_parentheses(1))
    parens = list(generate_parentheses(2))
    parens = list(generate_parentheses(3))
    parens = list(generate_parentheses(4))
    parens = list(generate_parentheses(5))
    x = 0
