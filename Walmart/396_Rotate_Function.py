class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        a, b, n = 0, 0, len(nums)
        for i,j in enumerate(nums):
            b += (i * j)
            a += j
        m = b
        for k in range(1,n):
            b = b + a - (n * nums[n-k])
            m = max(m, b)
        return m