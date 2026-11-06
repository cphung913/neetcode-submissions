class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dirs = {(0,0),(1,0),(1, 1),(-1,0),(-1, 1),(0,-1),(-1,-1),(0,1),(1,-1)}
        boxes = [(1,1),(4,4),(7,7),(1,4),(1,7),(4,1),(7,1),(7,4),(4,7)]
        valid = {"1","2","3","4","5","6","7","8","9", "."}

        def check_row(row: int) -> bool:
            seen = set()
            for n in board[row]:
                if (n not in valid) or (n in seen and n != "."):
                    return False
                seen.add(n)
            return True
        
        def check_col(col: int) -> bool:
            seen = set()
            for i in range(9):
                n = board[i][col]
                if (n not in valid) or (n in seen and n != "."):
                    return False
                seen.add(n)
            return True
        
        def check_box(center: Tuple[int]) -> bool:
            seen = set()
            for dx, dy in dirs:
                n = board[center[0]+dx][center[1]+dy]
                if (n not in valid) or (n in seen and n != "."):
                    return False
                seen.add(n)
            return True
        
        for i in range(9):
            if not (check_row(i) and check_col(i) and check_box(boxes[i])):
                return False
        return True
