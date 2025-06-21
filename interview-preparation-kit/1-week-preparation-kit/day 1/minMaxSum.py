def minMaxSum(arr: list):
    arr = sorted(arr)
    
    print(f"{sum(arr[:len(arr) - 1])} {sum(arr) - arr[0]}")
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    
    minMaxSum(arr)