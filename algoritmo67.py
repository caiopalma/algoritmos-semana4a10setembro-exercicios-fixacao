import math
def prog1ea40():
    input_value = input(f"\ndigite o valor da prestação: ")
    try:
        valor = float(input_value)
    except ValueError:
        valor = 0.0

    input_value = input(f"\ndigite a taxa: ")
    try:
        taxa = float(input_value)
    except ValueError:
        taxa = 0.0

    input_value = input(f"\ndigite o tempo(numero de meses): ")
    try:
        tempo = int(input_value)
    except ValueError:
        tempo = 0

    prest = valor + (valor * (taxa / 100.0) * float(tempo) )

    print(f"\no valor da prestação em atraso e = {prest},"
          f"\n")

if __name__ == '__main__':
    prog1ea40()