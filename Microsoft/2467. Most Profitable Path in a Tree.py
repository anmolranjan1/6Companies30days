import math
from collections import deque, defaultdict
import sys
sys.setrecursionlimit(10**5) 
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        visited = set()
        self.lvl = 0
        self.sum = 0
        self.max = -math.inf
        def remove_bob_income(src, bob, lvl):
            if src == bob:
                self.lvl = lvl
                amount[bob] = 0
                return True
            visited.add(src)
            for child in graph[src]:
                if child not in visited:
                    ans = remove_bob_income(child, bob, lvl + 1)
                    if ans:
                        if self.lvl & 1 and lvl == (self.lvl + 1)//2:
                            amount[src] //= 2
                        elif lvl > (self.lvl // 2):
                            amount[src] = 0
                        else:
                            self.sum += amount[src]   
                        return True
            return False
            visited.remove(src)       
        def dfs(src, income, visited):
            if len(graph[src]) == 1 and src != 0:
                self.max = max(self.max, income)
                return
            visited.add(src)
            for child in graph[src]:
                if child not in visited:
                    dfs(child, income + amount[child], visited)
            visited.remove(src)      
        remove_bob_income(0, bob, 1)
        dfs(0, amount[0], set())
        return self.max
            