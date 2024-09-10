from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            set_of_nums = set()
            for item in row:
                if item == ".":
                    continue
                elif int(item) in set_of_nums:
                    return False
                set_of_nums.add(int(item))
            set_of_nums.clear()

        for i in range(9):
            set_of_nums_2 = set()
            for row in board:
                if row[i] == ".":
                    continue
                elif int(row[i]) in set_of_nums_2:
                    return False
                set_of_nums_2.add(int(row[i]))
            set_of_nums_2.clear()

        def check_square(k,s):
            for i in range(3):
                for j in range(3):
                    if board[k+i][s+j] == ".":
                        continue
                    elif board[k+i][s+j] in square:
                        return False
                    else:
                        square.add(board[k+i][s+j])
            

        square = set()
        for k in range(0, 9, 3):
            for s in range(0, 9, 3):
                output = check_square(k,s)
                if output == False:
                    return False
                square.clear()
        return True
        
                        

                   
            






solution = Solution()
answer = solution.isValidSudoku(
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
)

print(answer)