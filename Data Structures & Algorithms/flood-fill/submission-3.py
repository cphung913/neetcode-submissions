class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        num = image[sr][sc]
        if num == color:
            return image
        def fill(row, col):
            image[row][col] = color
            check = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for change in check:
                r = row + change[0]
                c = col + change[1]
                if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == num:
                    fill(r, c)
        fill(sr, sc)
        return image
        