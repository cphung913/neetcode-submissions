class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0

        def dfs(r, c):
            grid[r][c] = "2"
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1":
                    dfs(nr, nc)

        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                if n == "1":
                    num += 1
                    dfs(i, j)

        return num
