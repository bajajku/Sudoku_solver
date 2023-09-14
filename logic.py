import sys
import time


BOARD = [[7,8,0,4,0,0,1,2,0],
         [6,0,0,0,7,5,0,0,9],
         [0,0,0,6,0,1,0,7,7],
         [0,0,7,0,4,0,2,6,0],
         [0,0,1,0,5,0,9,3,0],
         [9,0,4,0,6,0,0,0,5],
         [0,7,0,3,0,0,0,1,2],
         [1,2,0,0,0,7,4,0,0],
         [0,4,9,2,0,6,0,0,7]]

def print_board(brd):
    for i in range(len(brd)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(len(brd[0])):
            if j % 3 == 0 and j != 0 :
                print("| ", end="")

            if j == 8:
                print(brd[i][j])
            else:
                print(str(brd[i][j]) + " ", end ="")

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

def solve(board):
    # BackTracking Algorithm used
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
        
    for i in range(1,10):
        if isValid(board, i, (row, col)):
            board[row][col] = i
            
            if solve(board):
                return True
            
            board[row][col] = 0
    return False

def main():
    print_board(BOARD)
    print()
    timer = 0
    loading = "Loading Solution: [-----]"
    backtrack = '\b'*len(loading)

    while timer < 6:
        sys.stdout.write(backtrack + loading)
        sys.stdout.flush()
        loading = loading.replace("-","=",1)
        time.sleep(1)
        timer += 1
    time.sleep(1)
    sys.stdout.write(backtrack)
    print(loading+" Complete!")

    solve(BOARD)
    print()
    print_board(BOARD)

main()


