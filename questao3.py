import json


def process_faturamento(filename):

    with open(filename, 'r') as file:
        data = json.load(file)

    faturamento_diario = data['faturamento_diario']


    faturamentos = [entry['faturamento'] for entry in faturamento_diario if entry['faturamento'] > 0]

    if not faturamentos:
        print("Não há faturamentos para calcular.")
        return


    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)


    media_mensal = sum(faturamentos) / len(faturamentos)


    dias_acima_da_media = sum(1 for faturamento in faturamentos if faturamento > media_mensal)


    print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
    print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")


if __name__ == "__main__":
    filename = 'faturamento.json'
    process_faturamento(filename)
