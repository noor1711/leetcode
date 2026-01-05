class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        def getRowAndCol(val):
            return val // n, val % n
        
        def isValid(row, col):
            return 0 <= row < n and 0 <= col < n

        def isPossible(mat, row, col):
            if (any([mat[r][col] for r in range(n)]) or any([mat[row][c] for c in range(n)])):
                return False

            # check diagonals 
            for x, y in [[1, 1], [1, -1], [-1, -1], [-1, 1]]:
                r, c = row, col
                
                while isValid(r, c):
                    if mat[r][c]:
                        return False
                    r += x
                    c += y

            return True

        def mapToPiece(val):
            return "Q" if val else "."

        def mapToBoard(mat):
            return [''.join([mapToPiece(mat[row][col]) for col in range(n)]) for row in range(n)]

        def recurse(val, mat, total):
            if val == n * n:
                if total == n:
                    ans.append(mapToBoard(mat))
                return 

            row, col = getRowAndCol(val)
            if total + 1 < row:
                return 
        
            if isPossible(mat, row, col):
                matCopy = [[mat[r][c] for c in range(n)] for r in range(n)]
                matCopy[row][col] = True
                newVal = (row + 1) * n 
                recurse(newVal, matCopy, total + 1)

            recurse(val + 1, mat, total)
        
        recurse(0, [[False for c in range(n)] for r in range(n)], 0)
        return ans
