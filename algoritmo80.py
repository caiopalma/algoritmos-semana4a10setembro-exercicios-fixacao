
def prog1ea53():
    input_value = input(f"\nDigite a quantidade de fitas: ")
    try:
        quant = int(input_value)
    except ValueError:
        quant = 0

    input_value = input(f"\nDigite o valor do aluguel: ")
    try:
        valAluguel = float(input_value)
    except ValueError:
        valAluguel = 0.0

    fatAnual = (quant/3.0) * valAluguel * 12.0
    print(f"\nFaturamento anual : {fatAnual}")

    multas = valAluguel * 0.1 * (quant/3.0)/10.0
    print(f"\n Multas mensais : {multas}")

    quantFinal = quant - (quant * 0.02) + quant/10.0 #quant * 1.08
    print(f"\n Quantidade de fitas no final do ano : {quantFinal}"
          "\n")

if __name__ == '__main__':
    prog1ea53()