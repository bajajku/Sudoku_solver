BOARD = [[7,8,0,4,0,0,1,2,0],
         [6,0,0,0,7,5,0,0,9],
         [0,0,0,6,0,1,0,7,7],
         [0,0,7,0,4,0,2,6,0],
         [0,0,1,0,5,0,9,3,0],
         [9,0,4,0,6,0,0,0,5],
         [0,7,0,3,0,0,0,1,2],
         [1,2,0,0,0,7,4,0,0],
         [0,4,9,2,0,6,0,0,7]]

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
    for j in range(len(board[0])):
        if j % 3 == 0 and j != 0 :
            print("| ", end="")

        if j == 8:
            print(board[i][j])
        else:
            print(str(board[i][j]) + " ", end ="")

# function to find empty values in board which this program will solve
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)
    return None


def isValid(board, number, pos):
    
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == number and pos[1] != i:
            return False
    
    # Check columns
    for i in range(len(board)):
        if board[i][pos[1]] == number and pos[0] != i:
            return False
        
    # Check 3 x 3 box
    box_X = pos[1] // 3 # 0
    box_Y = pos[0] // 3 # 2
    
    for i in range(box_Y * 3, box_Y *3 + 3): # range(6,9)
        for j in range(box_X * 3, box_X * 3 + 3): # range(0,3)
            if board[i][j] == number and (i,j) != pos:
                return False
    
    return True

