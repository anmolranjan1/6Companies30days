class Solution:
  def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
    dp = [0] * len(nums)
    dq = collections.deque()

    for i, num in enumerate(nums):
      if dq:
        dp[i] = max(dq[0], 0) + num
      else:
        dp[i] = num
      while dq and dq[-1] < dp[i]:
        dq.pop()
      dq.append(dp[i])
      if i >= k and dp[i - k] == dq[0]:
        dq.popleft()

    return max(dp)