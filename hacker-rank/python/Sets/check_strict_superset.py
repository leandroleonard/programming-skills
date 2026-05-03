def check_strict_superset(a, lst):
    for s in lst:
        if len(s) >= len(a):
            return False
        
        if a.difference(a.difference(s)) != s:
            return False
            
    return True
    
a = set(map(int, input().split()))
n = int(input())
lst = []
for _ in range(n):
    lst.append(set(map(int, input().split())))
    
print("True") if check_strict_superset(a, lst) else print("False")