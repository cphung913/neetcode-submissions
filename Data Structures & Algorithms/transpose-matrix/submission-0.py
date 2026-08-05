class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new = []
        for col in range(len(matrix[0])):
            new.append([])
            for row in range(len(matrix)):
                new[col].append(matrix[row][col])
        return new
        