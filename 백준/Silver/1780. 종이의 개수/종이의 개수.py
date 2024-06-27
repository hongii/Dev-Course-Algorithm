import sys
input = sys.stdin.readline

k = int(input())

paper = []
for i in range(k):
	arr = list(map(int, input().split()))
	paper.append(arr)

def printPapers(res):
    print(res[-1])
    print(res[0])
    print(res[1])

def divideConquer(x, y, size):
    paperNum = paper[x][y]

    for i in range(x, x+size):
        for j in range(y, y+size):
            if(paper[i][j] != paperNum):
              new_size = size//3

              for ni in range(3):
                  for nj in range(3):
                      nx = x + ni * new_size
                      ny = y + nj * new_size
                      divideConquer(nx, ny, new_size)
              return
            
    if paperNum == -1:
        counts[-1] += 1
    elif paperNum == 0:
        counts[0] += 1
    elif paperNum == 1:
        counts[1] += 1

counts = {-1: 0, 0: 0, 1: 0}
divideConquer(0, 0, k)
printPapers(counts)