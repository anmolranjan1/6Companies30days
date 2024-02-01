from typing import List
from itertools import accumulate

class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        n = 1 << len(primes)
        maxNum = max(nums)
        dp = [0] * n
        count = [0] * (maxNum + 1)

        dp[0] = 1

        for num in nums:
            count[num] += 1

        def getPrimesMask(num, primes):
            primesMask = 0
            for i in range(len(primes)):
                if num % primes[i] == 0:
                    primesMask |= 1 << i
            return primesMask

        def modPow(x, n):
            if n == 0:
                return 1
            if n % 2 == 1:
                return x * modPow(x % Solution.kMod, (n - 1)) % Solution.kMod
            return modPow(x * x % Solution.kMod, n // 2) % Solution.kMod

        for num in range(2, maxNum + 1):
            if count[num] == 0:
                continue
            if num % 4 == 0 or num % 9 == 0 or num % 25 == 0:
                continue
            numPrimesMask = getPrimesMask(num, primes)
            for primesMask in range(n):
                if (primesMask & numPrimesMask) > 0:
                    continue
                nextPrimesMask = primesMask | numPrimesMask
                dp[nextPrimesMask] += dp[primesMask] * count[num]
                dp[nextPrimesMask] %= Solution.kMod

        return (pow(2, count[1], Solution.kMod) *
                (sum(dp[1:]) % Solution.kMod)) % Solution.kMod

    kMod = 10**9 + 7
