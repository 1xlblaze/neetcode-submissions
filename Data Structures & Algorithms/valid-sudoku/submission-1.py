class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cell = [[set() for _ in range(len(board[0]))] for m in range(len(board))]
        row = [set() for _ in range (9)]
        column = [set() for _ in range (9)]

        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                elif board[i][j] in row[i] or board[i][j] in column[j] or board[i][j] in cell[i//3][j//3]:
                    return False
                else:
                    row[i].add(board[i][j])
                    column[j].add(board[i][j])
                    cell[i//3][j//3].add(board[i][j])
        return True

        