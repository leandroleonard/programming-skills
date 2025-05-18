n = int(input())
k = int(input())
arr = []

for _ in range(n):
	arr.append(int(input()))

arr.sort()
m = arr[-1]
left = 0
right = k - 1


while right < n:
	if abs(arr[left] - arr[right]) < m:
		m = abs(arr[left] - arr[right])
	left += 1
	right += 1

print(int(m))

