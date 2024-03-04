# https://leetcode.com/problems/integer-to-roman/description/

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.


# Example 1:

# Input: num = 3
# Output: "III"
# Explanation: 3 is represented as 3 ones.
# Example 2:

# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
# Example 3:

# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


# Constraints:

# 1 <= num <= 3999


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # if mod of 5 is 4 or 9, that will need to map the integer to a double letter combination
        # check whether the value is greater than 5
        # if so, that is
        # if it is 5 or 0, that will translate to a number directly
        # if it is 1, 2, 3 / 6, 7, 8, that will translater to multiple repetitive letters
        # triplet tuple ("mod of 5", "greater equal than 5", "decimal position", "decimal digit")
        i2rdict = {
            (0, False, 1, 0): "",
            (0, False, 2, 0): "",
            (0, False, 3, 0): "",
            (0, False, 4, 0): "",
            (1, False, 1, 1): "I",
            (2, False, 1, 2): "II",
            (3, False, 1, 3): "III",
            (4, False, 1, 4): "IV",
            (0, True, 1, 5): "V",
            (1, True, 1, 6): "VI",
            (2, True, 1, 7): "VII",
            (3, True, 1, 8): "VIII",
            (4, True, 1, 9): "IX",
            (1, False, 2, 10): "X",
            (2, False, 2, 20): "XX",
            (3, False, 2, 30): "XXX",
            (4, False, 2, 40): "XL",
            (0, True, 2, 50): "L",
            (1, True, 2, 60): "LX",
            (2, True, 2, 70): "LXX",
            (3, True, 2, 80): "LXXX",
            (4, True, 2, 90): "XC",
            (0, False, 3, 0): "",
            (1, False, 3, 100): "C",
            (2, False, 3, 200): "CC",
            (3, False, 3, 300): "CCC",
            (4, False, 3, 400): "CD",
            (0, True, 3, 500): "D",
            (1, True, 3, 600): "DC",
            (2, True, 3, 700): "DCC",
            (3, True, 3, 800): "DCCC",
            (4, True, 3, 900): "CM",
            (1, False, 4, 1000): "M",
            (2, False, 4, 2000): "MM",
            (3, False, 4, 3000): "MMM",
        }

        # breakdown the integer in to string list based on decimal base,
        # revert the sequence
        s = str(int(num))[::-1]
        # print(s)
        s_tps = []
        str_r_ls = []
        # scan the list of digits, check each digit,
        for i in range(len(s)):
            # print(i, s[i])
            s_n = int(s[i])
            s_tp = (s_n % 5, s_n >= 5, i + 1, int(s_n) * 10**i)
            # print(s_tp)
            sub_r = i2rdict[s_tp]
            str_r_ls.append(sub_r)
            # print(i, ':/t', s_tp, "|/t", sub_r, "|/t", str_r_ls)
        str_r = "".join(str_r_ls[::-1])
        return str_r
