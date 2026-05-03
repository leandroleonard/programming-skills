from collections import OrderedDict
N = int(input())

lst = OrderedDict()

for _ in range(N):
    word = input()
    
    lst[word] = lst.get(word, 0) + 1
    
print(len(lst))
print(*lst.values())