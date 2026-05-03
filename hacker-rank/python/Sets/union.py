n = int(input())

class_a = set(map(int, input().split()))

n = int(input())

class_b = set(map(int, input().split()))

print(len(class_a.union(class_b)))
