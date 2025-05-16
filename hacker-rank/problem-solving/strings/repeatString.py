def repeat_string(s, n):
    return (s.count("a")) * (n//len(s)) + s[:n%len(s)].count("a")

s = input()
n = int(input())

print(repeat_string(s, n))