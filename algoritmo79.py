
def prog1ea52():
    input_value = input(f"\ndigite o valor da aplicacao: ")
    try:
        p = float(input_value)
    except ValueError:
        p = 0.0

    input_value = input(f"\ndigite a taxa( 0 - 1): ")
    try:
        i = float(input_value)
    except ValueError:
        i = 0.0

    input_value = input(f"\ndigite o número de meses: ")
    try:
        n = int(input_value)
    except ValueError:
        n = 0

    va = p * (((1.0 + i) ** float(n))-1.0) / i

    print(f"\no valor acumulado: {va}"
          "\n")

if __name__ == '__main__':
    prog1ea52()