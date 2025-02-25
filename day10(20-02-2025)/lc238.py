# from typing import List

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         ans = [1] * n  # Initialize with 1s
#         left_product = 1

#         # Left to right pass
#         for i in range(n):
#             ans[i] = left_product
#             left_product *= nums[i]

#         right_product = 1

#         # Right to left pass
#         for i in range(n - 1, -1, -1):
#             ans[i] *= right_product
#             right_product *= nums[i]

#         return ans

# # Example usage:
# nums = [1, 2, 3, 4]
# solution = Solution()
# result = solution.productExceptSelf(nums)
# print(result)  # Output: [24, 12, 8, 6]

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n  # Initialize with 1s
        left_product = 1

        # Left to right pass
        print("Left to Right Pass:")
        for i in range(n):
            ans[i] = left_product
            print(f"i: {i}, ans: {ans}, left_product: {left_product}")
            left_product *= nums[i]
            print(f"Updated left_product after multiplying with nums[{i}] ({nums[i]}): {left_product}")

        right_product = 1

        # Right to left pass
        print("\nRight to Left Pass:")
        for i in range(n - 1, -1, -1):
            ans[i] *= right_product
            print(f"i: {i}, ans: {ans}, right_product: {right_product}")
            right_product *= nums[i]
            print(f"Updated right_product after multiplying with nums[{i}] ({nums[i]}): {right_product}")

        return ans

# Example usage:
nums = [1, 2, 3, 4]
solution = Solution()
result = solution.productExceptSelf(nums)
print("\nFinal Result:", result)  # Output: [24, 12, 8, 6]
