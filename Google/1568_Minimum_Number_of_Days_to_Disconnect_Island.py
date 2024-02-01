class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        if self.disconnected(grid):
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if self.disconnected(grid):
                        return 1
                    grid[i][j] = 1

        return 2

    def disconnected(self, grid: List[List[int]]) -> bool:
        islands_count = 0
        seen = [[False] * len(grid[0]) for _ in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 or seen[i][j]:
                    continue
                if islands_count > 1:
                    return True
                islands_count += 1
                self.dfs(grid, i, j, seen)

        return islands_count != 1

    def dfs(self, grid: List[List[int]], i: int, j: int, seen: List[List[bool]]):
        seen[i][j] = True

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in dirs:
            x, y = i + dx, j + dy
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1 and not seen[x][y]:
                self.dfs(grid, x, y, seen)
