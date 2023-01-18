class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        arrSum = sum(nums)
        n = len(nums)
        if arrSum % k != 0:
            return False
        reqSum = arrSum // k
        nums.sort()
        @cache
        def dfs(currSum,arrState,k):
            if arrState == 0 and k == 0:
                return True
            for i in range(n):
                if currSum + nums[i] > reqSum:
                    return False
                elif arrState & (1 << (n - i - 1)) != 0:
                        arrState = arrState & ~(1 << (n - i - 1))
                        if currSum + nums[i] == reqSum:
                            if dfs(0,arrState,k-1):
                                return True
                        else:
                            if dfs(currSum + nums[i],arrState,k):
                                return True
                        arrState = arrState | (1 << (n - i - 1))
            return False
        arrState = (2**n) - 1
        return dfs(0,arrState,k)