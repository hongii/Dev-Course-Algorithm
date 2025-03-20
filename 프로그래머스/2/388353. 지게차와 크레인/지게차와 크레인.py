from collections import deque
def solution(storage, requests):
    row, col = len(storage), len(storage[0])
    graph = [['0']*(col+2)] + [list("0"+str+"0") for str in storage]+ [['0']*(col+2)]

    def check_outside(x, y, crane):
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]
            if 0 <= x_ < row + 2 and 0 <= y_ < col + 2:
                if crane:
                    if graph[x_][y_] == '0' or graph[x_][y_] == graph[x][y]:
                        return True
                elif graph[x_][y_] == '0':
                    return True
        return False
    
    def get_updated_value(val, target, check):
        if val == target:
            return '0' if check else '1'
        return val

    for str in requests:
        if len(str) > 1:
            target = str[0]
            graph = [
                [get_updated_value(val, target, check_outside(x, y, True)) for y, val in enumerate(row)]
                for x, row in enumerate(graph)
            ]
        else:
            remove_list = [] 
            for x in range(1, row+1):
                for y in range(1, col+1):
                    if str == graph[x][y] and check_outside(x, y, False):
                        remove_list.append((x, y))
                        
            while remove_list:
                a, b = remove_list.pop()
                graph[a][b] = '0'
                
    sentence = "".join(char for char in chain(*graph) if char != "0" and char != "1" )      
    return len(sentence)