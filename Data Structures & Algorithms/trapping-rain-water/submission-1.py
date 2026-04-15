"""
Row by row bottom up, if enclosed, add to area
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        max_height = max(height)
        row = 1 # Bottom to top starting at 1
        water = 0

        while row <= max_height:
            # Consider each row individually
            row_map = []
            for i in range(len(height)):
                if height[i] >= row:
                    row_map.append(1)
                else:
                    row_map.append(0)

            left_edge = 0
            for x in row_map:
                if x == 0:
                    left_edge += 1
                else:
                    break
            
            right_edge = 0
            for x in row_map[::-1]:
                if x == 0:
                    right_edge += 1
                else:
                    break
            
            walls = 0
            for x in row_map:
                if x == 1:
                    walls += 1

            water += len(height) - left_edge - right_edge - walls

            row += 1

        return water
