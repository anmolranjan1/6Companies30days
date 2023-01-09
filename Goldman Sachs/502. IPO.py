class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        a, q = sorted([(-p, c) for p, c in zip(profits, capital)], key=lambda x: x[1], reverse=True), []
        while k > 0:
            while a and a[-1][1] <= w: heappush(q, a.pop())
            if not q: break
            w -= heappop(q)[0]
            k -= 1
        return w