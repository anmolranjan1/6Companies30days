class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        a = 0
        b = [0]*12
        for i in range(2**12):
            c = 0
            d = [0]*12
            bobPoints = 0
            for j in range(12):
                if ((1<<j)&i)>0:
                    c+=aliceArrows[j]+1
                    bobPoints+=j
                    d[j]=aliceArrows[j]+1
            if c>numArrows:
                continue
            if bobPoints>a:
                a = bobPoints
                d[0]+=numArrows-c
                b = d[:]
        return b