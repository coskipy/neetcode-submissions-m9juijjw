class Solution:
    def isValid(self, s: str) -> bool:
        bracks = {')': '(', ']': '[', '}': '{'}
        to_close = []
        for char in s:
            if char in bracks.values(): # If an opening bracket
                to_close.append(char)
            elif char in bracks.keys():
                if not to_close or bracks[char] != to_close[-1]: # Disallowed close
                    return False
                to_close.pop()
        return len(to_close) == 0

