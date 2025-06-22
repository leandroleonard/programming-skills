def lonelyInteger(n: int, arr: list) -> int:
    revert = 1
    result = 0
    arr = sorted(arr)
    
    for i in arr:
        result += (i * revert)
        revert *= -1
        
    return result
    
    
if __name__ == '__main__':
    n = int(input())
    
    arr = list(map(int, input().rstrip().split()))
    
    print(lonelyInteger(n, arr))