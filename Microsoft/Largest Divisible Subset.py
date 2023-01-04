class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)
        dp=[1 for i in range(n)]
        hash=[i for i in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i]%nums[j]==0 and dp[i]<1+dp[j]:
                    dp[i]=1+dp[j]
                    hash[i]=j
        maxi=1
        max_ind=0
        for i in range(n):
            if dp[i]>maxi:
                maxi=max(maxi,dp[i])
                max_ind=i
        temp=[]
        temp.append(nums[max_ind])
        while hash[max_ind]!=max_ind:
            max_ind=hash[max_ind]
            temp.append(nums[max_ind])
        temp.reverse()
        return temp