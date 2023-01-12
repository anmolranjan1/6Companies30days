class Solution:
    def findKthNumber(self, n, k):
        if k == 1: return 1
        return self.denary(n, k)
    def denary(self, n, k):
        cur = 1  
        k -= 1 
        while k > 0:  
            counts = self.counts_lte(n, cur)
            if counts <= k:  
                k, cur = k - counts, cur + 1
            else: 
                k, cur = k - 1, cur * 10
        return cur  
    def counts_lte(self, n, num):  
        counts, limit = 0, num + 1
        while num <= n:  
            counts += min(n + 1, limit) - num  
            num, limit = num * 10, limit * 10 
        return counts