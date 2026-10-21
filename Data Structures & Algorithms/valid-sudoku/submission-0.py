class Solution:



    def isValidSudoku(self, board: List[List[str]]) -> bool:


        def check_section(x, y) -> bool:
            print("section")
            cur = set()
            for i in range(3):
                for j in range(3):
                    if board[x + i][y + j] in cur:
                        return False
                    if board[x + i][y + j] != '.':
                        cur.add(board[x + i][y + j])
            return True
                    


        # check each row
        for i in range(9):
            cur_row, cur_col = set(), set()
            for j in range(9):
                if board[i][j] in cur_row:
                    return False
                if board[j][i] in cur_col:
                    return False
                
                if board[i][j] != '.':
                    cur_row.add(board[i][j])
                if board[j][i] != '.':
                    cur_col.add(board[j][i])
        
        for i in range(3):
            for j in range(3):
                if(not check_section(i * 3, j * 3)):
                    return False
        return True



        # check each section