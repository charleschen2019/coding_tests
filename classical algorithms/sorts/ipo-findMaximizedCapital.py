# https://leetcode.com/problems/ipo/description/

# Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

# You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

# Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

# Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

# The answer is guaranteed to fit in a 32-bit signed integer.


# Example 1:

# Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
# Output: 4
# Explanation: Since your initial capital is 0, you can only start the project indexed 0.
# After finishing it you will obtain profit 1 and your capital becomes 1.
# With capital 1, you can either start the project indexed 1 or the project indexed 2.
# Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
# Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
# Example 2:

# Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
# Output: 6


# Constraints:

# 1 <= k <= 105
# 0 <= w <= 109
# n == profits.length
# n == capital.length
# 1 <= n <= 105
# 0 <= profits[i] <= 104
# 0 <= capital[i] <= 109


class Solution:
    def findMaximizedCapital1(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        profiles = [{"capital": c, "profit": p} for c, p in zip(capital, profits)]
        w_current = w
        k_current = k
        while (len(profiles) > 0) and (k_current > 0):
            available_profile = [
                profile["profit"]
                for profile in profiles
                if profile["capital"] <= w_current
            ]
            if len(available_profile) == 0:
                break
            max_profit = max(available_profile)
            chosen_profile = [
                (i, profile)
                for i, profile in enumerate(profiles)
                if profile["profit"] == max_profit
            ]
            if len(chosen_profile) > 0:
                k_current -= 1
                w_current += chosen_profile[0][1]["profit"]
                profiles.pop(chosen_profile[0][0])
            else:
                break

        return w_current

    def findMaximizedCapital2(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        import heapq

        pq = []
        pcs = [[p, c] for c, p in zip(capital, profits)]
        pcs.sort()
        k_finished = 0
        w_current = w
        i = 0
        # print(f"""k_finished={k_finished}, w_current={w_current}, i={i}, pq={pq}""")
        while k_finished < k:
            while i < len(pcs):
                pc = pcs[i]
                if pc[1] <= w_current:
                    heapq.heappush(pq, (-pc[0], pc[1]))
                    i += 1
                else:
                    if len(pq) > 0:
                        break
                    else:
                        return w_current
                # print(f"""k_finished={k_finished}, w_current={w_current}, i={i}, pq={pq}""")
            if len(pq) > 0:
                top_pc = heapq.heappop(pq)
                w_current -= top_pc[0]
                k_finished += 1
                # print(f"""k_finished={k_finished}, w_current={w_current}, i={i}, pq={pq}""")
            elif (i == 0) or (i == len(pcs)):
                break
        return w_current

    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        import heapq

        pq = []
        pcs = [[int(p), int(c)] for c, p in zip(capital, profits)]
        pcs.sort()
        n = len(pcs)
        print(f"""n={n}""")
        # print(f"""pcs={pcs}""")
        j = 0
        for i in range(k):
            while (j < n) and pcs[j][1] <= w:
                print("here 1")
                heapq.heappush(pq, (-pcs[j][0], pcs[j][1]))
                print(f"""k={k}, w={w}, i={i}, pq={pq}""")
                j += 1
            if pq:
                w -= heapq.heappop(pq)[0]
                print(f"""k={k}, w={w}, i={i}, pq={pq}""")
        return w


aa = Solution()
# k = 3
# w = 0
# profits = [1,2,3]
# capital = [0,1,2]
k = 2
w = 0
profits = [1, 2, 3]
capital = [0, 9, 10]
aa.findMaximizedCapital(k, w, profits, capital)
