class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        been = []
        for i in nums:
            if i in been:
                return True
            else:
                been.append(i)
        return False


        