class Solution:
    def isValid(self, s: str) -> bool:
        active = []
        for c in s: 
            if (c == '(' or c == '{' or c == '['):
                active.append(c)
            elif c == ')':
                if not active or active.pop() != '(':
                    return False
            elif c == '}':
                if not active or active.pop() != '{':
                    return False
            elif c == ']':
                if not active or active.pop() != '[':
                    return False
        if len(active) == 0:
            return True 
        else: 
            return False

        