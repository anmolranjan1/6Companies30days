class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n=len(nums)
        s=sum(nums)
        ans=F=sum([i*nums[i] for i in range(n)])
        for i in range(1,n):
            F=F+s-(n*nums[-i])
            ans=max(ans,F)
        return ans