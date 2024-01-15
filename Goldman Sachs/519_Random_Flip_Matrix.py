from typing import List

class Solution:

    def __init__(self, m: int, n: int):
        self.rows = m
        self.cols = n
        self.total = m * n
        self.used = set()

    def flip(self) -> List[int]:
        if len(self.used) == self.total:
            return []
        index = random.randint(0, self.total - 1)
        while index in self.used:
            index = (index + 1) % self.total
        self.used.add(index)
        return [index // self.cols, index % self.cols]

    def reset(self) -> None:
        self.used = set()

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
