from typing import List
from collections import defaultdict

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        ans = 0
        seen = set()

        def getMask(s):
            mask = 0
            for c in s:
                mask ^= 1 << (ord(c) - ord('a'))
            return mask

        for w in startWords:
            seen.add(getMask(w))

        for w in targetWords:
            mask = getMask(w)
            for c in w:
                if (mask ^ (1 << (ord(c) - ord('a')))) in seen:
                    ans += 1
                    break

        return ans
