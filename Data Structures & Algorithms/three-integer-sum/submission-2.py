class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)
        triplets = []

        # Two pointer over sorted list focused on i
        for i in range(0, len(snums) - 1):
            focus = snums[i]
            left = 0
            right = len(snums) - 1

            while left < right:
                if left == i: 
                    left += 1
                    continue
                if right == i:
                    right -= 1
                    continue

                threesum = focus + snums[left] + snums[right]
                if threesum == 0:
                    triplets.append([focus, snums[left], snums[right]])
                    left += 1 # In case i is a part of multiple combinations
                elif threesum > 0:
                    right -= 1
                else:
                    left += 1

        # Output unique combos
        output = []
        for i in range(0, len(triplets) - 1):
            if sorted(triplets[i]) not in output:
                output.append(triplets[i])       

        return output