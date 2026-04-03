import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Collapse, halve, flip, compare
        x = re.sub(r'[^a-zA-Z0-9]', '', s)
        if len(x) % 2 != 0:
            x = x[0:len(x)//2] + x[len(x)//2 + 1 :len(x)]

        x1 = x[0:len(x)//2]
        x2 = x[len(x)//2:len(x)][::-1]

        return x1.lower() == x2.lower()