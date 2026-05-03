n = int(input())

students_a = set(map(int, input().split()))

n = int(input())

students_b = set(map(int, input().split()))

print(len(students_a.difference(students_b)))
