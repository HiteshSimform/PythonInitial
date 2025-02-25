from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        for i in range(len(nums)):
            if(nums[i][i]=='0'):
                res.append('1')
            else:
                res.append('0')
        return ''.join(res)

nums = ["111","011","001"]
sol = Solution()
print(sol.findDifferentBinaryString(nums))
