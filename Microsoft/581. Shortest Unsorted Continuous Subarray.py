class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l = r = -1
        max_val = nums[0]
        for i in range(1, len(nums)):
            if max_val <= nums[i]:
                max_val = nums[i]
            else:
                r = i
                if l == -1:
                    l = i - 1
                while (l > 0) and (nums[l-1] > nums[i]):
                    l -= 1
        return r - l + 1 if l != r else 0