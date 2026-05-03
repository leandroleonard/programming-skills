if __name__ == '__main__':
    n, m = map(int, input().split())

    numbers = []
    numbers = list(map(int, input().split()))

    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    
    happiness = sum((x in A) - (x in B) for x in numbers)
    
    print(happiness)
