class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        mini = min(x, y)
        if x == y:
            return (mini * 2 + z) * 2
        return (mini * 2 + 1 + z) * 2