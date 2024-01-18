from typing import List
from queue import Queue

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        result = [[-1 for _ in range(n)] for _ in range(m)]

        myqueue = Queue()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    myqueue.put((i, j))
                    result[i][j] = 0

        cur_height = 0
        while not myqueue.empty():
            total = myqueue.qsize()

            for _ in range(total):
                pos = myqueue.get()

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for direction in directions:
                    new_pos_x, new_pos_y = pos[0] + direction[0], pos[1] + direction[1]
                    if (
                        0 <= new_pos_x < m
                        and 0 <= new_pos_y < n
                        and result[new_pos_x][new_pos_y] == -1
                    ):
                        myqueue.put((new_pos_x, new_pos_y))
                        result[new_pos_x][new_pos_y] = cur_height + 1

            cur_height += 1

        return result
