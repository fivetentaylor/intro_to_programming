from taylor_valid_parentheses import isValid

def test_min_time():
    assert isValid('({})') == True
    assert isValid('({)}') == False
