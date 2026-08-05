class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new = [[0 for y in range(len(matrix))] for x in range(len(matrix[0]))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                new[col][row] = matrix[row][col]
        return new
