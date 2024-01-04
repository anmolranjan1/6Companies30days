from typing import List

class Solution:
    def __init__(self):
        self.res_ = []

    def dfs(self, temp, target, index, sum_, k):
        if len(temp) == k and sum_ == target:
            self.res_.append(temp[:])
        elif sum_ < target and len(temp) < k:
            for i in range(index, 10):
                temp.append(i)
                self.dfs(temp, target, i + 1, sum_ + i, k)
                temp.pop()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        temp = []
        self.dfs(temp, n, 1, 0, k)
        return self.res_
