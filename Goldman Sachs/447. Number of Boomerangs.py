class Solution:
    def numberOfBoomerangs(self, p: List[List[int]]) -> int:
        out = 0
        for i in p:
            m = {}
            for j in p:
                d    = (i[0]-j[0])**2+(i[1]-j[1])**2
                m[d] = m[d]+1 if d in m else 0
                out += 2*m[d]
        return out