# https://leetcode.com/problems/roman-to-integer/description/

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.


# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


# Constraints:

# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].


class Solution(object):
    def romanToInt1(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        sum_s = 0
        # scan the whole string
        for i in range(len(s)):
            # print(i, '|', sum_s)
            if i < len(s) - 1:
                # check whether the next letter value is greater than the current letter value
                if s_dict[s[i + 1]] > s_dict[s[i]]:
                    # print("s_dict[s[i+1]] > s_dict[s[i]]")
                    # if so, that means the current letter should be a negative value
                    sum_s -= s_dict[s[i]]
                # if not the current letter will be added into the sum
                else:
                    # print("s_dict[s[i+1]] <= s_dict[s[i]]")
                    sum_s += s_dict[s[i]]
            else:
                # print("last digit plus")
                sum_s += s_dict[s[i]]
        # return the sum
        return sum_s

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "CM": 900,
            "CD": 400,
            "XC": 90,
            "XL": 40,
            "IX": 9,
            "IV": 4,
        }

        sum_s = 0
        i = 0
        # scan the whole string with counter to specify the starting point
        while i < len(s):
            # firstly examine whether the first two successive letters are in the dict
            if (i < len(s) - 1) and (s[i : i + 2] in s_dict):
                # if so, add the mapped value into sum and then shift the cursor 2 letters
                sum_s += s_dict[s[i : i + 2]]
                i += 2
            else:
                # if not, add add the mapped value into sum and then shift the cursor 1 letters
                sum_s += s_dict[s[i : i + 1]]
                i += 1
        # return the sum
        return sum_s
