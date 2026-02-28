import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    s = input().strip()

    first_half = s[:len(s)//2]

    if len(set(first_half)) > 1:
        print("YES")
    else:
        print("NO")

        
