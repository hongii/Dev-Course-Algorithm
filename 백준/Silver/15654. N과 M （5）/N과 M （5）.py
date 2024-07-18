from itertools import permutations as pm
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

# sol 1) 순열 라이브러리 사용
pms = list(pm(nums, m))
pms.sort()
for p in pms:
  print(" ".join(map(str, p)))