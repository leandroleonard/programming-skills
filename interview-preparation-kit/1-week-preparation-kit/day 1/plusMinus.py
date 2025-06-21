def plusMinus(n: int, arr: list):
    negatives = 0
    positives = 0
    zeros = 0
    
    for i in arr:
        if i == 0: zeros += 1
        elif i < 0: negatives += 1
        elif i > 0: positives += 1
        
    print(f"{(positives/n):.6f}")
    print(f"{(negatives/n):.6f}")
    print(f"{(zeros/n):.6f}")
    
    
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    
    plusMinus(n, arr)