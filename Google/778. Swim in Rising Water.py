class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        Rows,Cols=len(grid),len(grid[0])
        minH=[[grid[0][0],0,0]]
        visited=set()
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        while minH:
            curr_time,curr_r,curr_c=heapq.heappop(minH)
            if curr_r==Rows-1 and curr_c==Cols-1:
                return curr_time
            visited.add((curr_r,curr_c))
            for dr,dc in directions:
                nei_r,nei_c=curr_r+dr,curr_c+dc
                if  nei_r in range(Rows) and nei_c in range(Cols) and (nei_r,nei_c) not in visited:
                    visited.add((nei_r,nei_c))
                    heapq.heappush(minH,[max(curr_time,grid[nei_r][nei_c]),nei_r,nei_c])
                