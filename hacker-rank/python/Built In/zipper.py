students, n = map(int, input().split())

X = list()

for _ in range(n):
    X += [map(float, input().split())]

Z = zip(*X)

for i in Z:
    print(sum(i)/n)