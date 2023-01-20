class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp, sm = [0 for _ in range(k + maxPts)], 0
        for i in range(k + maxPts - 1, k - 1, -1):
            if i <= n:
                dp[i] = 1
            sm += dp[i]
        for i in range(k - 1, -1, -1):
            dp[i] = sm / maxPts;
            sm += dp[i]
            sm -= dp[i + maxPts]
        return dp[0]