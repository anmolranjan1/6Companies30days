from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self._wordBreak(s, set(wordDict), {})

    def _wordBreak(self, s: str, wordSet: set, memo: dict) -> bool:
        if s in wordSet:
            return True
        if s in memo:
            return memo[s]

        for i in range(1, len(s)):
            prefix = s[:i]
            suffix = s[i:]
            if prefix in wordSet and self._wordBreak(suffix, wordSet, memo):
                memo[s] = True
                return True

        memo[s] = False
        return False
