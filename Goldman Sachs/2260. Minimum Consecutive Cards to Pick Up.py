class Solution:
    def minimumCardPickup(self, s: List[int]) -> int:
        n = len(s)
        i, res, start = 0, float("inf"), 0
        seen = set()
        while i < n:
            while s[i] in seen:
                res = min(res, i-start+1)
                seen.remove(s[start])
                start += 1
            seen.add(s[i])
            i += 1    
        return -1 if res == float("inf") else res