s = input()

def sort_key(c):
    if c.islower():
        return (0, c)
    elif c.isupper():
        return (1, c)
    elif c.isdigit():
        return (2 if int(c) % 2 != 0 else 3, c)
    return (4, c)

r = sorted(s, key=sort_key)

print("".join(r))