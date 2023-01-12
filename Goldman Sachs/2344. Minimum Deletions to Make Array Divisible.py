class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:        
        nums.sort()
        x = reduce(gcd, numsDivide)        
        count = 0
        for num in nums:
            if x%num == 0:
                return count
            count+=1
        return -1       