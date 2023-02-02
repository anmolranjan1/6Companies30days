class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = [[] for _ in range(n + 1)]
        for edge in times:
            adjList[edge[0]].append([edge[1], edge[2]])
        queue = {}
        dist = [float('inf')] * (n + 1)
        for vertex in range(n):
            queue[vertex] = float('inf')
        dist[k] = 0
        queue[k] = 0
        while (len(queue) > 1):
            v = min(queue, key = queue.get)
            queue.pop(v)
            if dist[v] == float('inf'): break
            for w in adjList[v]:
                if (w[0] == k): continue
                newDist = dist[v] + w[1]
                if (newDist < dist[w[0]]):
                    dist[w[0]] = newDist
                    queue[w[0]] = newDist
        if float('inf') in dist[1:]: return -1
        return max(dist[1:])