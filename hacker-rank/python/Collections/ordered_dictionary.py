from collections import OrderedDict

N = int(input())

lst = OrderedDict()

for _ in range(N):
    item = input().split()
    price = int(item[-1])
    item_name = " ".join(item[0: -1])
    
    if item_name not in lst:
        lst[item_name] = price
    else:
        lst[item_name] += price

for items in lst:
    print(f"{items} {lst[items]}")