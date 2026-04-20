class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        # Early exit edge cases
        if len(s) <= 1: return len(s)

        left, right = 0, 1

        while right < len(s) + 1:
            if len(s[left:right]) == len(set(s[left:right])):
                max_len = max(max_len, right - left)
                right += 1
            else:
                left += 1
                right += 1


        return max_len