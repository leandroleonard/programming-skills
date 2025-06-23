def max_upper_left_submatrix(matrix):
    n = len(matrix) // 2
    total = 0
    
    for i in range(n):
        for j in range(n):
            val1 = matrix[i][j]
            val2 = matrix[i][2*n-1-j]
            val3 = matrix[2*n-1-i][j]
            val4 = matrix[2*n-1-i][2*n-1-j]
            total += max(val1, val2, val3, val4)
    
    return total

# Exemplo de uso:
# matrix = [
#     [3, 4, 1, 5],
#     [4, 6, 0, 3],
#     [9, 6, 2, 7],
#     [0, 4, 1, 8]
# ]
matrix = [
    [112, 42, 83, 119],
    [56, 125, 56, 49],
    [15, 78, 101, 43],
    [62, 98, 114, 108]
]

print(max_upper_left_submatrix(matrix)) 