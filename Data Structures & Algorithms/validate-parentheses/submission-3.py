class Solution:
    def isValid(self, s: str) -> bool:
        closed_bracks = [')', ']', '}']

        to_close = []
        
        for char in s:
            if char == '(':
                    to_close.insert(0, char)
            elif char =='[':
                    to_close.insert(0, char)
            elif char == '{':
                    to_close.insert(0, char)

            elif char in closed_bracks and len(to_close) == 0:
                return False

            elif char == ')':
                if to_close[0] != '(':
                    return False
                else:
                    to_close.pop(0)

            elif char == ']':
                if to_close[0] != '[':
                    return False
                else:
                    to_close.pop(0)

            elif char == '}':
                if to_close[0] != '{':
                    return False
                else:
                    to_close.pop(0)   
        
        return len(to_close) == 0
