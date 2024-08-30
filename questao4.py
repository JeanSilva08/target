def calcular_percentuais(faturamento_estados):

    total_mensal = sum(faturamento_estados.values())


    percentuais = {estado: (faturamento / total_mensal) * 100 for estado, faturamento in faturamento_estados.items()}

    return percentuais


def main():

    faturamento_estados = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }

    percentuais = calcular_percentuais(faturamento_estados)

    print("Percentual de representação de cada estado no faturamento total mensal:")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")


if __name__ == "__main__":
    main()
