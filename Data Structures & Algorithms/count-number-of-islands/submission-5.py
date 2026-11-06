class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        dirs = {(1,0),(-1,0),(0,1),(0,-1)}
        def dfs(i, j):
            if grid[i][j] == "1":
                grid[i][j] = "0"
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if (0 <= x < len(grid)
                        and 0 <= y < len(grid[0])
                        and grid[x][y] == "1"):
                        dfs(x, y)
                return True
            return False

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if dfs(row, col): count += 1
        return count