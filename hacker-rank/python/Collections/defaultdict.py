from collections import defaultdict

n, m = map(int, input().split())
A = defaultdict(list)

for i in range(1, n + 1):
    A[input()].append(i)
    
for i in range(1, m + 1):
    value = input()
    if value in A.keys():
        print(*(A[value]))
    else:
        print(-1)
