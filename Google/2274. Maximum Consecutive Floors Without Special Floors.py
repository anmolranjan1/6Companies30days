class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        a,b = len(special),0
        low = special[0]-bottom
        high = top-special[a-1]
        for i in range(a-1):
            b = max(b,special[i+1]-special[i]-1)
        return max({b,low,high})