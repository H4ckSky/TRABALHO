import datetime

def main():
    # Obtém a data atual
    data_atual = datetime.datetime.now()

    # Formata a data para exibir apenas o dia, mês e ano
    data_formatada = data_atual.strftime("%d/%m/%Y")

    # Imprime o dia de hoje
    print("Hoje é:", data_formatada)

if __name__ == "__main__":
    main()