
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


tenho o seguinte desafio: Desafio Você está desenvolvendo um sistema simples para um e-commerce que deseja registrar os valores das compras realizadas por um cliente ao longo de um único dia. O sistema deve primeiro receber a quantidade total de compras realizadas e, em seguida, solicitar o valor de cada uma dessas compras. Ao final, o sistema deve exibir o total gasto no dia e a média de valor por compra. Entrada A entrada deve receber: Um número inteiro N que indica a quantidade de compras realizadas no dia. Em seguida, N números do tipo double, cada um representando o valor de uma compra. Saída O programa deverá retornar: O total das compras com duas casas decimais A média de valor por compra com duas casas decima Se N for 0 (ou seja, nenhuma compra registrada), o programa deverá exibir: "Nenhuma compra registrada." o sistema me deu o seguinte código, que eu devo seguir para executar o programa, porém eu não sei como faço para inserir os dados necessários para esta codificação.


def main():
    purchase_count = int(input())

    if purchase_count == 0:
        print("Nenhuma compra registrada.")
    else:
        total_spent = 0.0
        i = 1

        while i <= purchase_count:
            try:
                purchase_value = float(input())
            except ValueError:
                continue  # ignora entrada inválida

            if purchase_value < 0:
                continue  # ignora valores negativos
            else:
                total_spent += purchase_value
                i += 1

        # Calcule a média
        average_purchase = total_spent / purchase_count

        print(f"{total_spent:.2f}")
        print(f"{average_purchase:.2f}")


if __name__ == "__main__":
    main()



