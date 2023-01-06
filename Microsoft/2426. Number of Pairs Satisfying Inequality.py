class Solution:
    def numberOfPairs(self, X: List[int], Y: List[int], D: int) -> int:
        return (d := []) or sum((len(d)-bisect_left(d,y-x)) + bool(insort(d, y-x+D)) for x, y in zip(X, Y))