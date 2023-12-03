'''
💡 Key
- line 1 : N(1<=N<=20)
- line 2 : intial status

🔑 Strategy
- 상, 하, 좌, 우 움직임 구현
- 이동에 따른 경우의 수에 따라 보드 블록 값이 최대가 될 수 있는 것을 찾기
    - 가능한 모든 경로를 탐색하는 DFS, BFS ...등등을 사용
    - 해를 찾아가는 중 더 이상 가지 않고 되돌아가는 backtracking 사용 (특정 조건을 만족하는~~) 

🔑 Feedback
- 그냥 풀 수는 있지만 어떤 알고리즘을 써야하고 어떻게 적용해야하는지 아직 구별을 잘 못한다!
- 알고리즘 구별하는 걸 연습하자 
'''
import sys, copy
from copy import deepcopy

# UP
def up(board):
    for j in range(n):
        pointer = 0
        for i in range(1, n):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                # 포인터가 가리키는 수가 0일 때
                if board[pointer][j] == 0:
                    board[pointer][j] = tmp
                # 포인터가 가리키는 수와 현재 위치의 수가 같음
                elif board[pointer][j]  == tmp:
                    board[pointer][j] *= 2
                    pointer += 1
                # 포인터가 가리키는 수와 현재 위치의 수가 다름
                else:
                    pointer += 1
                    board[pointer][j] = tmp
    return board

# DOWN
def down(board):
    for j in range(n):
        pointer = n - 1
        for i in range(n - 2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[pointer][j] == 0:
                    board[pointer][j] = tmp
                elif board[pointer][j]  == tmp:
                    board[pointer][j] *= 2
                    pointer -= 1
                else:
                    pointer -= 1
                    board[pointer][j] = tmp
    return board

# LEFT
def left(board):
    for i in range(n):
        pointer = 0
        for j in range(1, n):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][pointer] == 0:
                    board[i][pointer] = tmp
                elif board[i][pointer]  == tmp:
                    board[i][pointer] *= 2
                    pointer += 1
                else:
                    pointer += 1
                    board[i][pointer]= tmp
    return board

# RIGHT
def right(board):
    for i in range(n):
        pointer = n - 1
        for j in range(n - 2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][pointer] == 0:
                    board[i][pointer] = tmp
                elif board[i][pointer]  == tmp:
                    board[i][pointer] *= 2
                    pointer -= 1
                else:
                    pointer -= 1
                    board[i][pointer] = tmp
    return board


# DFS
def dfs(board, cnt):
    if cnt == 5:
        # 2차원 배열 요소 중 가장 큰 값을 결과로 반환
        return max(map(max, board))

    # 상, 하, 좌, 우로 움직여 리턴한 값들 중 가장 큰 값 반환
    # board를 꼭 deepcopy하여 함수를 거친 board값이 다음 함수의 input이 되지 않도록 주의
    return max(dfs(up(deepcopy(board)), cnt + 1), dfs(down(deepcopy(board)), cnt + 1), dfs(left(deepcopy(board)), cnt + 1), dfs(right(deepcopy(board)), cnt + 1))



if __name__ == "__main__":

    # get input
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    max_block = 0 #initializing
    print(dfs(board, 0))
    
    
