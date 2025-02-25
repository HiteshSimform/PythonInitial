from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left=0
        right=len(height)-1

        while left < right:
            minimumHeight = min(height[left],height[right])
            res = max(res, minimumHeight * (right - left))
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return res
    
s=Solution()
height = [1,8,6,2,5,4,8,3,7]
print(s.maxArea(height))