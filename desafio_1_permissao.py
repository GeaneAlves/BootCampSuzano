
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
