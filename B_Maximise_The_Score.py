import sys
input = sys.stdin.readline

t = int(input())
n = int(input().strip())
a = list(map(int, input().split()))

for _ in range(t):
            
        a.sort()
        
        ans = sum(a[::2])
        print(ans)