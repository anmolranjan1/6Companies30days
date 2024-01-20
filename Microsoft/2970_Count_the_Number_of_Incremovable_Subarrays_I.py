class Solution:
  def incremovableSubarrayCount(self, nums: List[int]) -> int:
    n = len(nums)
    startIndex = self._getStartIndexOfSuffix(nums)
    if startIndex == 0:
      return n * (n + 1) // 2

    ans = n - startIndex + 1

    for i in range(startIndex):
      if i > 0 and nums[i] <= nums[i - 1]:
        break
      ans += n - bisect.bisect_right(nums, nums[i], startIndex) + 1

    return ans

  def _getStartIndexOfSuffix(self, nums: List[int]) -> int:
    for i in range(len(nums) - 2, -1, -1):
      if nums[i] >= nums[i + 1]:
        return i + 1
    return 0