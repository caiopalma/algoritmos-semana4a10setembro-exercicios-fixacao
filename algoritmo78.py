
def prog1ea51():
    input_value = input(f"\ndigite o numero de lados do poligono: ")
    try:
        n = int(input_value)
    except ValueError:
        n = 0

    nd = n * (n - 3.0) / 2.0

    print(f"\nnumero de diagonais: {nd}"
          "\n")

if __name__ == '__main__':
    prog1ea51()