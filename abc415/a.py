n = int(input())
list1 = list(map(int, input().split()))
x = int(input())

if x in list1:
    print("Yes")
else:
    print("No")