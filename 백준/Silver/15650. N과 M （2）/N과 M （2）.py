from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

comb = combinations(nums, m)
for cb in comb:
	print(" ".join(map(str, cb)))
