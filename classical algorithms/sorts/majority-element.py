# https://leetcode.com/problems/majority-element/description/

# Given an array of size , return the majority element.numsn

# The majority element is the element that appears more than times. You may assume that the majority element always exists in the array.⌊n / 2⌋


# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109


# Follow-up: Could you solve the problem in linear time and in space?O(1)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Sort this array and take the element at index = n / 2
        l = len(nums)
        p_compare = 0
        for i in range(1, l):
            if (p_compare < l) and (nums[p_compare] != nums[i]):
                nums[p_compare + 1], nums[i] = nums[i], nums[p_compare + 1]
                p_compare += 2
            # print(f"""p_compare={p_compare}, i={i}""")
            # print(f"""nums={nums}""")
        major = nums[-1]
        return major
