k = int(input())

paper = []
for i in range(k):
	arr = list(map(int, input().split()))
	paper.append(arr)

# 1) 종이가 모두 같은 수로 되어 있는지 확인
def isSameAllPapers(arr):
	numSet = set([num for row in arr for num in row])
	return len(numSet) == 1

def printPapers(res):
    print(res[-1])
    print(res[0])
    print(res[1])

# 2) 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서 1)의 과정을 반복
def divideConquer(paper, x1, y1, x2, y2, size):
    subPapers = [row[y1:y2+1] for row in paper[x1:x2+1]]
    
    if size == 1 or isSameAllPapers(subPapers):
        key = subPapers[0][0]
        counts[key] += 1
        return

    new_size = size // 3
    for i in range(3):
        for j in range(3):
            nx1 = x1 + i * new_size
            ny1 = y1 + j * new_size
            nx2 = nx1 + new_size - 1
            ny2 = ny1 + new_size - 1

            divideConquer(paper, nx1, ny1, nx2, ny2, new_size)

counts = {-1: 0, 0: 0, 1: 0}
if isSameAllPapers(paper):
  key = paper[0][0]
  counts[key] = 1
else:
  divideConquer(paper, 0, 0, k-1, k-1, k)

printPapers(counts)