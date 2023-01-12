class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        a, b = [0] * n, 0
        a[0] = 1
        for i in range(1, n):
            a[i] = b + a[i-delay] - a[i-forget]
            b = a[i]
        return sum(a[n-forget:]) % 1000000007