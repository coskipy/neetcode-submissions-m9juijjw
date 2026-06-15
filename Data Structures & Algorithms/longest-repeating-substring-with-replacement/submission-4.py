from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1

        l, r = 0, 1
        longest = 1
        while r <= len(s):
            part = s[l:r]
            hist = Counter(part)
            non_uniform = sum([value for value in hist.values()]) - max(hist.values())

            if k >= non_uniform:
                longest = max(longest, r - l)
            else:
                l += 1

            r += 1
        return longest