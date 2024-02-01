from typing import List

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        numOfNumbers = len(nums)
        trimmedNumbers = []
        answer = []

        for query in queries:
            k = query[0]
            trimLength = query[1]

            for i in range(numOfNumbers):
                trimmedNumbers.append((nums[i][-trimLength:], i))

            trimmedNumbers.sort()
            answer.append(trimmedNumbers[k - 1][1])
            trimmedNumbers.clear()
        return answer
