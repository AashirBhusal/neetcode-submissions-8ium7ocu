class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        condition_one = self.same_rowcheck(board)

        print(condition_one)

        condition_two = self.same_colcheck(board)

        condition_three = self.subbox_check(board)

        if condition_one and condition_two and condition_three:
            return True
        else:
            return False


    def same_rowcheck(self, board: List[List[str]]) -> bool:


        

        for i in range(len(board)):
            row = []
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue

                
                if board[i][j] not in row:
                    row.append(board[i][j])
                else:
                    return False
        
        return True

    def same_colcheck(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            col = []
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue

                
                if board[j][i] not in col:
                    col.append(board[j][i])
                else:
                    return False
        
        return True

    def subbox_check(self, board: List[List[str]]) -> bool:
       

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):

                box = []

                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):

                        if board[i][j] == ".":
                            continue

                        if board[i][j] not in box:
                            box.append(board[i][j])
                        else:
                            return False

        return True
        
        



        



