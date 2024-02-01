from typing import List
from collections import deque

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        size = R * C
        arr = [[0] * C for _ in range(R)]
        res = [None] * size
        i = 0

        arr[r0][c0] = 1
        queue = deque([(r0, c0)])

        while queue:
            t = queue.popleft()
            v = arr[t[0]][t[1]]
            res[i] = list(t)
            i += 1

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for d in directions:
                x, y = t[0] + d[0], t[1] + d[1]
                if 0 <= x < R and 0 <= y < C and arr[x][y] == 0:
                    arr[x][y] = v + 1
                    queue.append((x, y))

        return res