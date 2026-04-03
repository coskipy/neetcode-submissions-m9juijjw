class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # value, index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                print(seen)
                return [seen[complement], i]
            else:
                seen[num] = i
                
