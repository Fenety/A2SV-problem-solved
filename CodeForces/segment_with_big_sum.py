import sys
input = sys.stdin.readline

n, s = map(int, input().split())
a = list(map(int, input().split()))

l = 0
curr_sum = 0
min_length = float('inf')

for r in range(n):
    curr_sum += a[r]
    
    while curr_sum >= s:
        min_length = min(min_length, r - l + 1)

        curr_sum -= a[l]
        l += 1

if min_length == float('inf'):
    print(-1)
else:
    print(min_length)

#time complexity : O(n)
#space complexity : O(1)
#time : 25 min