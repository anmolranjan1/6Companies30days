class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(st,seen):
            mx=0    
            for i in range(len(st)):
                if st[:i+1] in seen:
                    continue
                mx=max(mx , 1 + dfs(st[i+1:],seen | {st[:i+1]}))         
            return mx   
        return dfs(s,set())


