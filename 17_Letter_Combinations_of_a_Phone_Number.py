class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = []
        self.dfs(digits, 0, "", ans, digit_to_letters)
        return ans

    def dfs(self, digits: str, i: int, path: str, ans: List[str], digit_to_letters: List[str]) -> None:
        if i == len(digits):
            ans.append(path)
            return

        for letter in digit_to_letters[int(digits[i]) - int('0')]:
            self.dfs(digits, i + 1, path + letter, ans, digit_to_letters)