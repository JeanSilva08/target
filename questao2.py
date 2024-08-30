def is_fibonacci_number(n):
    if n < 0:
        return False

    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False


def main():
    while True:
        user_input = input(
            "Informe um número para verificar se pertence à sequência de Fibonacci (ou digite 'sair' para encerrar): ")

        if user_input.lower() == 'sair':
            print("Encerrando o programa.")
            break

        try:
            number = int(user_input)
            if is_fibonacci_number(number):
                print(f"O número {number} pertence à sequência de Fibonacci.")
            else:
                print(f"O número {number} não pertence à sequência de Fibonacci.")
        except ValueError:
            print("Por favor, insira um número válido.")


if __name__ == "__main__":
    main()
