from collections import deque

def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())
        cubes = deque(map(int, input().split()))

        top = float('inf')
        possible = True

        while cubes:
            left = cubes
            right = cubes[-1]

            if left >= right:
                tmp = cubes.popleft()
            else:
                tmp = cubes.pop()

            if tmp > top:
                possible = False
                break
            
            top = tmp

        if possible:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    solve()