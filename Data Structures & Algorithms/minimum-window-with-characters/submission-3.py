# Histogram Solution
# Get histogram of t
# Window starts left - len t
# Get histogram of Window
# If hist t not in hist window -> increase right
# If hist t in hist window -> update min with min(min, window substring) and increase left
# Stop stop when r = len(s) and hist t not in hist s

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Make histogram of t
        ht = defaultdict(int)
        for char in t:
            ht[char] += 1

        # Make histogram of s
        hs = defaultdict(int)
        for char in s[0:len(t)]:
            hs[char] += 1

        l, r = 0, len(t)
        min_substring = ""


        while r <= len(s):
            contains_sub = True
            for key, value in ht.items():
                if hs[key] < value: # Window does not contain substring, so increase right
                    if r < len(s):
                        hs[s[r]] += 1 # Add new char in window to hs
                    r += 1
                    contains_sub = False
                    break

            if not min_substring and contains_sub:
                min_substring = s[l:r]
            elif contains_sub:
                min_substring = min(s[l:r], min_substring, key=len)
                hs[s[l]] -= 1 # Remove char no longer in window from hs
                l += 1

        return min_substring