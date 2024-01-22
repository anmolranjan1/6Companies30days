from typing import List
from collections import Counter

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ans = 0
        count = Counter(ages)

        def request(ageA, ageB):
            return not (ageB <= 0.5 * ageA + 7 or ageB > ageA or (ageB > 100 and ageA < 100))

        for ageA, countA in count.items():
            for ageB, countB in count.items():
                if request(ageA, ageB):
                    if ageA == ageB:
                        ans += countA * (countB - 1)
                    else:
                        ans += countA * countB

        return ans
