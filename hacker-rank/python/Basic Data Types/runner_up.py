if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(set(arr))
    print(sorted(arr, reverse=True)[1])
