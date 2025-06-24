def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2) - 1
    
    a[mid], a[n-1] = a[n-1], a[mid]
    
    a = a[:mid] + [a[mid]] + sorted(a[mid + 1:], reverse=True)
    
    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')


test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    
    findZigZagSequence(a, n)