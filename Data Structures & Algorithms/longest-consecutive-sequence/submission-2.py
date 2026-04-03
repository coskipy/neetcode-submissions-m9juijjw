class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        numset = set()
        for num in nums:
            if num not in numset:
                numset.add(num)

        ordered = sorted(numset)
        print(ordered)

        longest = 1
        curr_longest = 1
        for i in range(1, len(ordered)):
            if ordered[i] == ordered[i-1] + 1:
                curr_longest += 1
            else:
                longest = max(longest, curr_longest)
                curr_longest = 1

        return max(longest, curr_longest)