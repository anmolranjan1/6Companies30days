from functools import cache
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        @cache
        def dfs(k):
            if k == 1: return 0
            res = 1/k
            for i in range(1, k):
                res += 1/k*dfs(k - i)
            return res
        if n == 1: return 1.0
        return dfs(n)