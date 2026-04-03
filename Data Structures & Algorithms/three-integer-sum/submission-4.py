class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)
        triplets = []

        # Two pointer over sorted list focused on i
        for i in range(0, len(snums) - 1):
            focus = snums[i]
            left = i + 1
            right = len(snums) - 1

            # Skip duplicate snums[i]
            if i > 0 and snums[i] == snums[i - 1]:
                continue

            while left < right:
                threesum = focus + snums[left] + snums[right]
                if threesum == 0:
                    triplets.append([focus, snums[left], snums[right]])

                    # Ensure pointers are fresh for next loop to avoid duplicates
                    while left < right and snums[left] == snums[left + 1]: left += 1
                    while left < right and snums[right] == snums[right - 1]: right -= 1
                    left += 1
                    right -= 1

                elif threesum > 0:
                    right -= 1
                else:
                    left += 1

        return triplets