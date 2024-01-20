class Solution:
    def maxProduct(self, s: str) -> int:
        ans = [0]  # Using a list to store the result as a mutable container

        def dfs(i, s1, s2):
            if i == len(s):
                if self.isPalindrome(s1) and self.isPalindrome(s2):
                    ans[0] = max(ans[0], len(s1) * len(s2))
                return

            dfs(i + 1, s1 + s[i], s2)
            dfs(i + 1, s1, s2 + s[i])
            dfs(i + 1, s1, s2)

        dfs(0, "", "")
        return ans[0]

    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
