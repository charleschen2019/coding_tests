# <!-- https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Given a string s, find the length of the longest
# substring
#  without repeating characters.


# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


# Constraints:


# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces. -->
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        max_s = 0
        while (left < len(s)) and (right < len(s)):
            subs = s[left : right + 1]
            # sets = set(subs)
            # print(left, right, subs, s[left], max_s)
            if right + 1 < len(s):
                if s[right + 1] in subs:
                    left += 1
                else:
                    right += 1
            else:
                left += 1
            max_s = max(max_s, len(subs))

        return max_s
