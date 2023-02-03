class Solution:
    def maxSumMinProduct(self, nums) -> int:
        mod = 10**9+7
        prefSum,res,l = [0],0,len(nums)
        for n in nums:
            prefSum.append(prefSum[-1]+n)
        stack = []
        for i,n in enumerate(nums):
            newStart = i
            while(len(stack) and stack[-1][1]>n):
                start,val = stack.pop()
                currSum = prefSum[i]-prefSum[start]
                res = max(res, currSum*val)
                newStart = start
            stack.append((newStart,n))
        for i,val in stack:
            currSum = prefSum[l]-prefSum[i]
            res = max(res,currSum*val)

        return res%mod