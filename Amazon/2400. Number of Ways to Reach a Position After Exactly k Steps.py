class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        cache = {}
        MOD = 10**9+7
        def dfs(num, x):
            if (num, x) in cache:
                return cache[(num, x)]
            if x > k:
                cache[(num, x)] = 0
                return 0
            if x == k and num == endPos:
                cache[(num, x)] = 1
                return 1
            cache[(num, x)] = (dfs(num+1, x+1) + dfs(num-1, x+1)) % MOD
            return cache[(num, x)]
        
        
        return dfs(startPos, 0)