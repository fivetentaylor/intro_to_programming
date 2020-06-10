from taylor_generate_parentheses import generate_parentheses

# [1 2 3 2 1 0]
# [+ + + - - -]
# 1. if cumsum is ever negative it's not well formed
# 2. if it ends in anything but 0 it's not well formed

# The first opening paren can not move or it'd break #1
# The second opening paren can only move one spot otherwise it'd break #1
# The third opening paren can only move two spots otherwise it'd break #1


def test_generate_parentheses():
    assert list(generate_parentheses(0)) == []
    assert list(generate_parentheses(1)) == ['()']
    assert '(())' in set(generate_parentheses(2))
    assert '((()))' in set(generate_parentheses(3))
    assert '(((())))' in set(generate_parentheses(4))
    assert '((((()))))' in set(generate_parentheses(5))
