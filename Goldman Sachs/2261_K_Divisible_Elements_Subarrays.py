from typing import List

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        uniqueSubarrays = set()
        numSize = len(nums)

        for startIdx in range(numSize):
            divisibleCount = 0
            subarrayStr = ""

            for endIdx in range(startIdx, numSize):
                if nums[endIdx] % p == 0:
                    divisibleCount += 1
                    if divisibleCount > k:
                        break

                subarrayStr += str(nums[endIdx]) + ","
                uniqueSubarrays.add(subarrayStr)

        return len(uniqueSubarrays)
