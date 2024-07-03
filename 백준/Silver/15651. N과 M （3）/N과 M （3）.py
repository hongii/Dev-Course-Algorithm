from itertools import product
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

# sol 1) 중복 순열 라이브러리 사용
# perm = product(nums, repeat=m)
# for pm in perm:
# 	print(" ".join(map(str, pm)))

# sol 2) 백트래킹(완전 탐색)
def permutation(pm, cnt):
  if cnt == 0:
    print(" ".join(map(str, pm)))
    return
  
  for i in range(n):
    pm.append(nums[i])
    permutation(pm, cnt-1)
    pm.pop()

permutation([], m)