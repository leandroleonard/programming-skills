if __name__ == '__main__':
    q = int(input())
    
    for _ in range(q):
        n = int(input())
        
        arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
        
        arr = sorted(arr, reverse=True)
        
        print(arr)
                
        