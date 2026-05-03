t = int(input())

for _ in range(t):
    try:
        a, b = map(int, input().split())
        
        print(a // b)
    except ValueError as e:
        print("Error Code:", e)
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
        