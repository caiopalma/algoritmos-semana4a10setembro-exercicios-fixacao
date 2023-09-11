import math
def prog1ea18():
    input_value = input(f"\ndigite numero: ")
    try:
        num = float(input_value)
    except ValueError:
        num = 0.0
    quad = num ** 2.0
    raizquad = num ** 0.5
    print(f"\nnumero: {num}"
          f"\nquadrado: {quad}"
          f"\nraiz quadrada: {raizquad}"
          f"\n")

if __name__ == '__main__':
    prog1ea18()
