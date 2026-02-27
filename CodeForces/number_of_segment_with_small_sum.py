import sys
input = sys.stdin.readline

n, s = map(int, input().split())
a = list(map(int, input().split()))

l = 0
current_sum = 0
count = 0

for r in range(n):
    current_sum += a[r]
    
    while current_sum > s:
        current_sum -= a[l]
        l += 1
   
    count += r - l + 1

print(count)

#time complexity : O(n)
#space complexity : O(1)
#time : 21 min