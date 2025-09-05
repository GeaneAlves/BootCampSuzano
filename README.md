# BootCampSuzano
Exercícios do BootCamp
# Operadores aritméticos - Adição, subtração, multiplicação divisão e divisão inteira


# Adição
print(1 + 1)

###Subtração print(10 - 2)

# Multiplicação
print(4 * 3)

# Divisão e Divisão inteira
print(12 / 3)
print(12 // 2)

# Módulo e Exponenciação
print(10 % 3)
print(2 ** 3)

### Precedência de operadores. 
# regra de resolução: 
- Parêntesis
- Expoentes
- Multiplicação e divisão (da esquerda para a direita)
- Soma e Subtração (da esquerda para a direita)

print(10 - 5 * 2)
print((10 - 5) * 2)
print(10 ** 2 * 2)
print(10 ** (2 * 2))
print(10 / 2 * 4)


### Operadores de Comparação
# Compara dois valores ou mais
#Igualdade
saldo = 450
saque = 200
print(saldo == saque)

#Diferença
saldo = 450
saque = 200
print(saldo != saque)

#Maior que / maior ou igual
saldo = 450
saque = 200
print(saldo > saque)
print(saldo >= saque)

#Menor que / menor ou igual
saldo = 450
saque = 200
print(saldo < saque)
print(saldo <= saque)

###OPeradores de atribuição
#Utilizados para definir o valor inicial ou sobrescever o valor de uma variável

# Atrubuição simples
saldo = 500
print(saldo)

# Atribuição com adição
saldo = 500
saldo += 200
print(saldo)

# Atribuição com subtração
saldo = 500
saldo -= 100
print(saldo)

# Atribuição com multiplicação
saldo = 500
saldo *= 2
print(saldo)

# Atribuição com divisão
saldo = 500
saldo /= 5
print(saldo)

saldo = 500
saldo //= 5
print(saldo)

# Atribuição com módulo
saldo = 500
saldo %= 480
print(saldo)

# Atribuição com exponenciação
saldo = 80
saldo **= 2
print(saldo)

### Operadores Lógicos
# Utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica. Ao ser usado, o resultado retornado é um booleano, podemos combinar operadores de compoaração com os operadores lógicos.
# op_comparacao + op_logico + op_comparacao ... N ...

saldo = 1000
saque = 200
limite = 100

saldo >= saque

saldo <= limite

### Operador E
saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite


### Operador OU
saldo = 1000
saque = 200
limite = 100

saldo >= saque or saque <= limite




