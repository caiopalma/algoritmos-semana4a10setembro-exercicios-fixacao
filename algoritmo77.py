
def prog1ea50():
    input_value = input(f"\ndigite 1 numero: ")
    try:
        a = float(input_value)
    except ValueError:
        a = 0.0

    input_value = input(f"\ndigite 2 numero: ")
    try:
        b = float(input_value)
    except ValueError:
        b = 0.0

    d = (a-b) ** 2.0
    q = (a ** 2.0) - (b ** 2.0)

    print(f"\no quadrado da diferenca = {d}"
          f"\ndiferenca dos quadrados = {q}"
          "\n")

if __name__ == '__main__':
    prog1ea50()