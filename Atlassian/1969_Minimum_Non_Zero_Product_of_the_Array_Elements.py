class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        n = 1 << p
        half_count = n // 2 - 1
        return self.mod_pow(n - 2, half_count) * ((n - 1) % Solution.kMod) % Solution.kMod

    kMod = 1_000_000_007

    def mod_pow(self, x: int, n: int) -> int:
        if n == 0:
            return 1
        x %= Solution.kMod
        if n % 2 == 1:
            return x * self.mod_pow(x, n - 1) % Solution.kMod
        return self.mod_pow(x * x, n // 2) % Solution.kMod
