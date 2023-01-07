from sortedcontainers import SortedList
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        a = {}
        for i in range(n):
            a[nums2[i]] = i
            b = []
        for j in nums1:
            b.append(a[j])
        c, d = SortedList(), SortedList()
        e, f = [], []
        for i in range(n):
            e.append(c.bisect_left(b[i]))
            c.add(b[i])
        for i in range(n - 1, -1, -1):
            f.append(len(d) - d.bisect_right(b[i]))
            d.add(b[i])
        g = 0
        for i in range(n):
            g += e[i] * f[n - 1 - i]
        return g