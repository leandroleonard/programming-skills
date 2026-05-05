cube = lambda x: x*x*x

def fibonacci(n):
    numbers = []
    a, b = 0, 1
    
    for _ in range(n):
        numbers.append(a)
        a, b = b, a + b
        
    return numbers
        
if __name__ == '__main__':
    n = int(input())
    
    print(list(map(cube, fibonacci(n))))