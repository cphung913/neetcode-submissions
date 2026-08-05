class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        num = image[sr][sc]
        if num == color:
            return image
        def fill(row, col, matrix):
            matrix[row][col] = color
            check = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for change in check:
                r = row + change[0]
                c = col + change[1]
                if 0 <= r < len(image) and 0 <= c < len(image[0]) and matrix[r][c] == num:
                    matrix = fill(r, c, matrix)
            return matrix
        return fill(sr, sc, image)
        