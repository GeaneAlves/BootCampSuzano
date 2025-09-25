
Desafio proposto:

"Acesso permitido" → se tiver permissão e idade ≥ 18

"Acesso negado" → se não tiver permissão

"Idade insuficiente" → se tiver permissão, mas idade < 18

def main():
    # Entrada de dados do usuário
    has_permission = input().lower() == "true"
    age = int(input())

    # Verifique condições de acesso
    if has_permission and age >= 18:
        print("Acesso permitido")
    elif has_permission and age < 18:
        print("Idade insuficiente")
    else:
        print("Acesso negado")


if __name__ == "__main__":
    main()



    Entrada (linha 1 = permissão, linha 2 = idade)	Condição avaliada	Saída esperada
true
20	Tem permissão e idade >= 18	Acesso permitido
false
25	Sem permissão, mesmo com idade	Acesso negado
true
16	Tem permissão mas idade < 18	Idade insuficiente
false
15	Sem permissão e ainda menor de idade	Acesso negado


Rodando direto os 4 cenários de teste da tabela, sem precisar digitar mais nada

def verificar_acesso(has_permission: bool, age: int):
    if has_permission and age >= 18:
        return "Acesso permitido"
    elif has_permission and age < 18:
        return "Idade insuficiente"
    else:
        return "Acesso negado"


def main():
    # Lista de cenários (permissão, idade)
    testes = [
        (True, 20),   # deve dar "Acesso permitido"
        (False, 25),  # deve dar "Acesso negado"
        (True, 16),   # deve dar "Idade insuficiente"
        (False, 15),  # deve dar "Acesso negado"
    ]

    for i, (perm, idade) in enumerate(testes, start=1):
        resultado = verificar_acesso(perm, idade)
        print(f"Teste {i}: {resultado}")


if __name__ == "__main__":
    main()

Criei a função verificar_acesso que recebe permissão e idade e retorna a mensagem.

No main() montei uma lista com os 4 cenários de teste.

O for executa cada cenário e mostra o resultado.

A saida será assim:
Teste 1: Acesso permitido
Teste 2: Acesso negado
Teste 3: Idade insuficiente
Teste 4: Acesso negado


Boa 👍 então vamos deixar o código interativo como o do desafio, mas com a possibilidade de rodar vários testes seguidos até você digitar "sair".

def verificar_acesso(has_permission: bool, age: int):
    if has_permission and age >= 18:
        return "Acesso permitido"
    elif has_permission and age < 18:
        return "Idade insuficiente"
    else:
        return "Acesso negado"


def main():
    print("=== Controle de Acesso ===")
    print("Digite 'sair' a qualquer momento para encerrar.\n")

    while True:
        # Entrada de permissão
        entrada_perm = input("O visitante tem permissão (true/false)? ").lower()
        if entrada_perm == "sair":
            break
        has_permission = entrada_perm == "true"

        # Entrada de idade
        entrada_idade = input("Idade do visitante: ")
        if entrada_idade.lower() == "sair":
            break
        age = int(entrada_idade)

        # Verifica acesso
        resultado = verificar_acesso(has_permission, age)
        print("Resultado:", resultado, "\n")


if __name__ == "__main__":
    main()


O programa fica em loop.

Você digita true/false para permissão e a idade em seguida.

Ele mostra a resposta (Acesso permitido, Idade insuficiente ou Acesso negado).

Se digitar sair, o programa encerra.


=== Controle de Acesso ===
Digite 'sair' a qualquer momento para encerrar.

O visitante tem permissão (true/false)? true
Idade do visitante: 20
Resultado: Acesso permitido 

O visitante tem permissão (true/false)? true
Idade do visitante: 16
Resultado: Idade insuficiente 

O visitante tem permissão (true/false)? false
Idade do visitante: 25
Resultado: Acesso negado 

O visitante tem permissão (true/false)? sair



