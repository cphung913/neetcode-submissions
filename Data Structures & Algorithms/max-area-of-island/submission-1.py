from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        def bfs(current): # current: (row, col)
            q = deque([current])
            area = 0
            while len(q) > 0:
                r, c = q.popleft()
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    area += 1
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                            q.append((nr, nc))

            return area
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                max_area = max(max_area, bfs((i, j)))
        return max_area