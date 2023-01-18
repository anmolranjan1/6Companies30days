class Solution:
    def findInMountainArray(self, target: int, ma: 'MountainArray') -> int:
        self.d, self.ma, L = {}, ma, ma.length()  
        mxi = self.findmaxindex(0, L-1)
        if self.ma.get(mxi) < target: return -1        
        ans1 = self.query(0,mxi,target)
        ans2 = self.query(mxi+1,L-1,target, up=False)       
        ans = min(ans1,ans2)
        return ans if ans != math.inf else -1        
    def query(self, l, r, t, up=True):        
        while l<r:
            m = (l+r+1)//2
            if t == self.ma.get(m):
                return m      
            if self.ma.get(m) < t:
                if up: l = m
                else: r = m-1
            else:                
                if not up: l = m
                else: r = m-1                   
        return l if self.ma.get(l) == t else math.inf       
    def findmaxindex(self, l, r):
        if l==r: return l
        cur = (l+r+1)//2
        return self.findmaxindex(l, cur-1) if self.ma.get(cur) < self.ma.get(cur-1) else self.findmaxindex(cur, r)