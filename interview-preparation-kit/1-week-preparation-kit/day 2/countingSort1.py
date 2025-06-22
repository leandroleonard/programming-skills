def countingSort(n, arr)-> list :
    counting = [0] * 100
    arr = sorted(arr)
    
    for i in arr:
        counting[i] += 1
    
    return counting
    


if __name__ == '__main__':
    n = int(input())
    
    arr = list(map(int, input().rstrip().split()))
    
    for i in countingSort(n, arr):
        print(i, end=' ')