def inverter_string(s):

    string_invertida = ""


    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]

    return string_invertida


def main():
    while True:

        user_input = input("Informe uma string para inverter (ou digite 'sair' para encerrar): ")


        if user_input.lower() == 'sair':
            print("Encerrando o programa.")
            break


        string_invertida = inverter_string(user_input)
        print(f"String invertida: {string_invertida}")


if __name__ == "__main__":
    main()
