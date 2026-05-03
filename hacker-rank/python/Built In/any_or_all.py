n = int(input())
numbers = list(map(int, input().split()))
print(all(n > 0 for n in numbers) and any(str(n) == str(n)[::-1] for n in numbers))
