from collections import Counter

s = input()

freq = Counter(s)

sorted_chars = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

for char, count in sorted_chars[:3]:
    print(char, count)