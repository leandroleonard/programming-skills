def diagonalDifference(n: int, matrix: list) -> int :
    i = diagonalSum1 = diagonalSum2 = 0        
    
    while i < n:
        j = 0
        while j < n:
            if i == j:
                diagonalSum1 += matrix[i][j]
            if i + j == len(matrix) - 1:
                diagonalSum2 += matrix[i][j]
            j += 1
        i += 1
        
    return abs(diagonalSum1 - diagonalSum2)

if __name__ == '__main__':
    n = int(input())
    
    matrix = [list(map(int, input().rstrip().split())) for _ in range(n)]
    
    print(diagonalDifference(n, matrix))