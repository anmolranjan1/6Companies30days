from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sorted_nums = sorted(nums)

        n = len(nums)
        mid_index = (n - 1) // 2
        last_index = n - 1

        for k in range(n):
            if k % 2 == 0:
                nums[k] = sorted_nums[mid_index]
                mid_index -= 1
            else:
                nums[k] = sorted_nums[last_index]
                last_index -= 1
