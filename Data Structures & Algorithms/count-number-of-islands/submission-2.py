class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        h, w = len(grid), len(grid[0]) 
        count = 0
        def bfs(r, c):
            q = collections.deque([])
            q.append((r, c))
            while q:
                i, j = q.popleft()
                grid[i][j] = "0"
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    row, col = i + dr, j + dc
                    if 0<=row<h and 0<=col<w and grid[row][col] == "1":
                        q.append((row, col))
        
        for arr in range(h):
            for n in range(w):
                if grid[arr][n] == "1":
                    count += 1
                    bfs(arr, n)
        return count