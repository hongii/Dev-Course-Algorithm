from itertools import chain
from collections import deque
def solution(storage, requests):
    row, col = len(storage), len(storage[0])
    graph = [['0']*(col+2)] + [list("0"+str+"0") for str in storage]+ [['0']*(col+2)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    def check_outside(x, y):
        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]
            if 0 <= x_ < row + 2 and 0 <= y_ < col + 2:
                if graph[x_][y_] == '0':
                    return True
        return False
    
    def bfs(target, remove_list):
        dq = deque()
        visited = [[False]*(col+2) for _ in range(row+2)]
        visited[0][0] = True
        dq.append((0, 0))
        
        while dq:
            x, y = dq.popleft()
            
            for i in range(4):
                x_ = x + dx[i]
                y_ = y + dy[i]
                if 0 <= x_ < row + 2 and 0 <= y_ < col + 2 and not visited[x_][y_]:
                    if  graph[x_][y_] == '0':
                        visited[x_][y_] = True
                        dq.append((x_, y_))
                    elif graph[x_][y_] == target and check_outside(x_, y_):
                        remove_list.append((x_, y_))
        for x, y in remove_list:
            graph[x][y] = '0'

    for str in requests:
        remove_list = [] 
        if len(str) > 1:
            target = str[0]
            bfs(target, remove_list)
            graph = [['0' if char == target else char for char in row] for row in graph]
        else:
            bfs(str, remove_list) 
        
    sentence = "".join(char for char in chain(*graph) if char != "0")      
    return len(sentence)