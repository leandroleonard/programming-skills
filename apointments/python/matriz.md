# Manipulando matriz em python

### 1. Criando Matrizes em Python
Uma matriz (ou array 2D) é apenas uma lista de listas:

```
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Acessar elementos:
```
print(matriz[0][1])  # 2 (linha 0, coluna 1)
```

### 2. Gerar Matriz com valores padrão
# Matriz 3x4 preenchida com zeros
```
rows, cols = 3, 4
matrix = [[0 for _ in range(cols)] for _ in range(rows)]
```
### 3. Percorrendo matrizes
Com indice
```
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j])
```

com valores
```
for linha in matriz:
    for valor in linha:
        print(valor)
```
### 4. Leitura de matriz
```
n, m = map(int, input().split())  # número de linhas e colunas
matriz = []

for _ in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)
```

## Tips
```
n = 3
matriz = [list(map(int, input().split())) for _ in range(n)]
```