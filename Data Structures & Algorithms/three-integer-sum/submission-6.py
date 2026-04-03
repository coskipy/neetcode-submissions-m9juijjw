class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        # Two pointer over sorted list focused on i
        for i in range(len(nums) - 2): #len - 2 to avoid final unnecessary left and right collision
            focus = nums[i]
            left = i + 1
            right = len(nums) - 1

            # Skip duplicate nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                threesum = focus + nums[left] + nums[right]
                if threesum == 0:
                    triplets.append([focus, nums[left], nums[right]])

                    # Ensure pointers are fresh for next loop to avoid duplicates
                    while left < right and nums[left] == nums[left + 1]: left += 1
                    left += 1

                elif threesum > 0:
                    right -= 1
                else:
                    left += 1

        return triplets