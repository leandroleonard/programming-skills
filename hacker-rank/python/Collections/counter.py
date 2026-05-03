from collections import Counter

n = int(input())

shoe_sizes = Counter(map(int, input().split()))

x = int(input())
revenue = 0

for _ in range(x):
    size, price = map(int, input().split())
    
    if shoe_sizes[size] > 0:
        revenue += price
        shoe_sizes[size] -= 1 

print(revenue)