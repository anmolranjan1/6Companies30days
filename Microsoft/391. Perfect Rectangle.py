class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        m=0
        a=set()
        b = lambda: (d-e) * (f-g)
        for g, e, f, d in rectangles:
            m += b()
            a ^= {(g, e), (g, d), (f, e), (f, d)}   
        if len(a) != 4:
            return False
        g, e = min(a, key=lambda g: g[0] + g[1])
        f, d = max(a, key=lambda g: g[0] + g[1])
        return m == b()

