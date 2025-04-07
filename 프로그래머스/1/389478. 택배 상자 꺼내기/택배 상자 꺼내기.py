import math
def solution(n, w, num):
    row_cnt = math.ceil(n/w)
    cur = 1
    arr = []
    for r in range(row_cnt):
        if r == row_cnt - 1:
            line = list(range(cur, n+1))
            line += [0] * (w - len(line))
        else:
            line = list(range(cur, cur+w))
        
        if r % 2 == 1:
            line.reverse()

        arr.append(line)
        cur += w

    for r, row in enumerate(arr):
        if num in row:
            c = row.index(num)
            break

    count = 0
    for line in reversed(arr):
        if line[c] == num:
            break
        if line[c] != 0:
            count += 1

    return count + 1