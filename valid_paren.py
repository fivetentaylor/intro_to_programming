class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in "{[(":
                stack.append(p)
            elif (len(stack) != 0):
                if ((stack[-1] == '(') and (ord(stack[-1]) + 1) == ord(p)) or (ord(stack[-1]) + 2) == ord(p):
                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack) == 0