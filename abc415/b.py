s = input()
positions = [i + 1 for i, c in enumerate(s) if c == '#']
for i in range(0, len(positions), 2):
    print(f"{positions[i]},{positions[i+1]}")
