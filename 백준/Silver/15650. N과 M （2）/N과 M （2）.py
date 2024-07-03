from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

# sol 1) 조합 라이브러리 사용
comb = combinations(nums, m)
for cb in comb:
  print(" ".join(map(str, cb)))

# sol 2) 백트래킹(완전 탐색)
# def combination(cb, start, cnt):
#   if cnt == 0:
#     print(" ".join(map(str, cb)))
#     return
  
#   for i in range(start, n):
#     cb.append(nums[i])
#     combination(cb, i+1, cnt-1)
#     cb.pop()

# combination([], 0, m)
