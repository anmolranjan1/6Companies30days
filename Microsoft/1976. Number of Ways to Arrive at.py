from heapq import heappop, heappush
class Solution:
    def countPaths(self, N: int, roads: List[List[int]]) -> int:
        adj_list = defaultdict(list)       
        for u,v,t in roads:
            adj_list[u].append((v,t))
            adj_list[v].append((u,t))        
        dist = [float(inf)] * N
        ways = [1] * N       
        heap = [(0,0)]         
        while heap:
            d,node = heappop(heap)            
            for nei,t in adj_list[node]:
                if d + t < dist[nei]:
                    dist[nei] = d + t
                    ways[nei] = ways[node]
                    heappush(heap, (dist[nei], nei))
                elif d + t == dist[nei]:
                    ways[nei] = (ways[node] + ways[nei]) % (10**9 + 7)        
        return ways[N - 1]