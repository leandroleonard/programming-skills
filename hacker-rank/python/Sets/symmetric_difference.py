a = int(input())
set_a = set(map(int, input().split()))

b = int(input())
set_b = set(map(int, input().split()))

lst = list(set_a.difference(set_b).union(set_b.difference(set_a)))

for i in sorted(lst):
    print(i)
