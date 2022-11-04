global N
N=4

def printboard(board):
    for i in range(N):
        for j in range(N):
             print(board[i][j],end=' ')
        print()
        
def issafe(board,row,col):
    for i in range(col):
        if board[row][i]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    for i,j in zip(range(row,N,1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    return True
def solution(board,col):
    if col>=N:
        return True
    for i in range(N):
          if issafe(board,i,col)==True:
             board[i][col]=1
             if solution(board,col+1)==True:
                return True
             board[i][col]=0
    return False
def solve():
    board=[[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]
           ]
    if solution(board,0)==False:
        print("sorry")
    printboard(board)
    return True
solve()

        
        
    
    
            
            
