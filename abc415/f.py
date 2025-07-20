def maxConsecutiveString(s: str) -> int:
    max_count = 0
    current_count = 0
    previous_char = None

    for char in s:
        if char == previous_char:
            current_count += 1
        else:
            current_count = 1
            previous_char = char
        max_count = max(max_count, current_count)

    return max_count

n, q = map(int, input().rstrip().split())
s = input()

for _ in range(q):
    t, l, r = map(str, input().rstrip().split())
    
    if t == '1':
        s = s[:int(l)-1] + r + s[int(l):]
    elif t == '2':
        print(maxConsecutiveString(s[int(l)-1:int(r)]))