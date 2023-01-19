class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:       
        def sieve(n):
            prime = [True] * (n+1)
            for i in range(2, n//2):
                if prime[i]:
                    for jj in range(2*i, n+1, i):
                        prime[jj] = False
            return [i for i in range(2, n+1) if prime[i]]        
        primes = sieve(right)
        inRange = False
        minDiff = float("inf")
        ans = [-1, -1]       
        for ind in range(0, len(primes)-1):
            if not inRange:
                if primes[ind] >= left:
                    inRange = True                
            if inRange:
                l = primes[ind]
                r = primes[ind+1]
                if (r-l) < minDiff:
                    minDiff = r-l
                    ans = [l, r]
        return ans
                
            
        
        