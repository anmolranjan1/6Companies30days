class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0

        arr2.sort()

        for a in arr1:
            index = bisect_left(arr2, a)
            if ((index == len(arr2) or arr2[index] - a > d) and
                (index == 0 or a - arr2[index - 1] > d)):
                ans += 1

        return ans