from functools import lru_cache
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        @lru_cache(None)
        def dp(r, c, k):
            if r < 0 or r >= N or c < 0 or c >= N:
                return 0
            elif k <= 0:
                return 1
            res = 0
            for a, b in [(2, 1), (-2, -1), (2, -1), (-2, 1)]:
                res += dp(r + a, c + b, k - 1)
                res += dp(r + b, c + a, k - 1)
            return res / 8
        
        return dp(r, c, K)