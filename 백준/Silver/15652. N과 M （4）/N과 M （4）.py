from itertools import combinations_with_replacement as cbr
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

# sol 1) 중복 조합 라이브러리 사용
cbrs = cbr(nums, m)
for cb in cbrs:
	print(" ".join(map(str, cb)))