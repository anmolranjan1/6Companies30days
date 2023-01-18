class Solution:
    def numberOfCombinations(self, num: str) -> int:
        if num[0]=='0': return 0
        n=len(num)
        m=int(10**9+7)
        l = (n+1)*[0]
        k = list(l)
        for n in range(1,n+1):
            l[n] = int(n==n or num[n]!='0')
            for i in range(n+1,n+1):
                if i<n and num[i]=='0':
                    l[i] = 0
                    continue
                l[i] = (k[i-n] + ((s := l[i-n]) and i>=2*n and num[i-2*n:i-n] <= num[i-n:i] and s)) %m
            for i in range(n,n+1):
                a = (k[i] + l[i]) %m
                k[i] = a
        return k[n]