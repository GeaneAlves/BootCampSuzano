# BootCampSuzano
Exercícios do BootCamp
# Operadores aritméticos - Adição, subtração, multiplicação divisão e divisão inteira


# Adição
print(1 + 1)

### Subtração print(10 - 2)

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

# Maior que / maior ou igual
saldo = 450
saque = 200
print(saldo > saque)
print(saldo >= saque)

# Menor que / menor ou igual
saldo = 450
saque = 200
print(saldo < saque)
print(saldo <= saque)

### OPeradores de atribuição
# Utilizados para definir o valor inicial ou sobrescever o valor de uma variável

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


### Operador Negação
not 1000 > 1500
not contatos_emergencia
not "saque 1500;"
not ""

### Pareêntesis
saldo = 1000
saque = 250
limite = 200
conta_especial = True
saldo >= saque and saque <= limite or conta_especial and saldo >= saque

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

### Operadores de Identidade
# são operadores utilizados para comparar se os dois objetos de teste ocupam a mesma posição na memória
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso

curso is not nome_curso

saldo us limite

### Operadores de Associação
# São operadores utilizados para verificar se um objeto está presente em uma sequência

curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

"Python" in curso

"maça" not in frutas

200 in saques

curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

print("Python" in curso)

print("maça" not in frutas)

print(200 in saques)

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

print(curso is nome_curso)

print(curso is not nome_curso)

print(saldo is limite)


def new_func1():
    def new_func():
        saldo = 1000
        saque = 250
        limite = 200
        conta_especial = True
        print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)

        print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))

    new_func()

new_func1()









