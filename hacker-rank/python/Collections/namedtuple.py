from collections import namedtuple

N = int(input())
fields = input().split()

Students = namedtuple("Students", fields)

r = 0

for _ in range(N):
    s = Students(*input().split())
    r += int(s.MARKS)
    
print(f"{r / N:.2f}")


