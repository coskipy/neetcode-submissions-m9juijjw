class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        filt = nums[:]
        filt = sorted(filt)

        print(filt, nums)
        i = 0
        j = len(filt) - 1
        while True:
            if filt[i] + filt[j] > target:
                j -= 1
            elif filt[i] + filt[j] < target:
                i += 1
            else:
                break

        print(i, j)
        a = []
        b = []
        for ind, num in enumerate(nums):
            if num == filt[i]:
                a.append(ind)
            if num == filt[j]:
                b.append(ind)

        return [min(a+b), max(a+b)]

        