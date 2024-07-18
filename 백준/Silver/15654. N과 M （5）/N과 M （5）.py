from itertools import permutations as pm
import sys
import os
sys.stdin = open(os.getcwd() + "\\input.txt", "rt")
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

# sol 1) 순열 라이브러리 사용
pms = list(pm(nums, m))
pms.sort()
for p in pms:
  print(" ".join(map(str, p)))

# sol 2) 백트래킹(완전 탐색)
# def permutation(pm, cnt):
#   if cnt == 0:
#     print(" ".join(map(str, pm)))
#     return
  
#   for i in range(n):
#     if(pm and nums[i] in pm):
#       continue
  
#     pm.append(nums[i])
#     permutation(pm, cnt-1)
#     pm.pop()

# nums.sort()
# permutation([], m)
