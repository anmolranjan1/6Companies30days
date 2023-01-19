from heapq import *
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:        
        g = collections.defaultdict(list)       
        for i , j , w in edges:
            g[i].append((j,w))
            g[j].append((i,w))        
        def neighbours(i):         
            heap = [(0,i)]
            d = {}
            while heap:
                distance , node = heappop(heap)
                if node in d:
                    continue
                if node != i:
                    d[node] = distance
                for nei,w in g[node]:           
                    if nei in d:
                        continue
                    if distance+w <= distanceThreshold:
                        heappush(heap,(distance+w,nei))             
            return len(d)                    
        return max([(neighbours(city), city) for city in range(n)], key=lambda x: (-x[0], x[1]))[-1]
        