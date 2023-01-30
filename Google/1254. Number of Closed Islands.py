class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)] 
        def is_valid(r, c):
            return 0 <= r < R and 0 <= c < C       
        def is_border(r, c):
            return r == 0 or r == R-1 or c == 0 or c == C-1        
        def dfs(r, c):
            if not is_valid(r, c) or grid[r][c] != 0:
                return
            grid[r][c] = 1
            for dr, dc in directions:
                dfs(r+dr, c+dc)
        
        for r in range(R):
            for c in range(C):
                if is_border(r, c) and grid[r][c] == 0:
                    dfs(r, c)

        res = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    dfs(r, c)
                    res += 1
        return res
        