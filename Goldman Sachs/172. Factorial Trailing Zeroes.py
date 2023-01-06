class Solution:
    def trailingZeroes(self, n: int) -> int:
        a,b = 5,0
        while a<=n:
            b+=n//a
            a*=5
        return b