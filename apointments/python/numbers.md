# Python - Números

## 1. Tipos de Números em Python
Python trabalha principalmente com dois tipos numéricos básicos:

- int: número inteiro → 5, -10, 0

- float: número decimal → 5.0, -3.14, 0.400000

```
a = 10
b = 3
```
## 2. Operações Básicas

### Soma
    print(a + b)  # 13

### Subtração
    print(a - b)  # 7

### Multiplicação
    print(a * b)  # 30

### Divisão com ponto flutuante
    print(a / b)  # 3.3333333333333335

### Divisão inteira (sem casas decimais)
    print(a // b)  # 3

### Módulo (resto da divisão)
    print(a % b)  # 1

### Potência
    print(a ** b)  # 1000

## 3. Arredondamento

Arredondar para 2 casas decimais

    print(round(3.14159, 2))  # 3.14

## 4. Formatando com casas decimais exatas
Se você quer exibir exatamente 6 casas decimais, use format() ou f-strings:

➤ Com f-string (mais moderno):
    
    valor = 0.4
    print(f"{valor:.6f}")  # saída: 0.400000

➤ Com format():

    print("{:.6f}".format(valor))  # saída: 0.400000

## 5. Números decimais grandes (alta precisão)
Para cálculos com alta precisão decimal, você pode usar o módulo decimal.

```
from decimal import Decimal, getcontext

getcontext().prec = 50  # Define 50 casas decimais de precisão

a = Decimal("1.0") / Decimal("3.0")
print(a)  # 0.33333333333333333333333333333333333333333333333333
```

## 6. Infinito em Python
```
positivo_infinito = float('inf')
negativo_infinito = float('-inf')

print(positivo_infinito > 1e308)  # True
print(negativo_infinito < -1e308)  # True
```

## 7. NaN
Podemos representar valores indefinidos com NaN (Not a Number):

```
nan = float('nan')
print(nan != nan)  # True — NaN nunca é igual a si mesmo!
```