class Solution:
        def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
            if not left:
                left = [0]
            if not right:
                right = [n]
            max_to_left = max(left)
            max_to_right = max([n - r for r in right])
            return max(max_to_left, max_to_right)