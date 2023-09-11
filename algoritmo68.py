import math
def prog1ea41():
    input_value = input(f"\ndigfgite 1 numero com ponto: ")
    try:
        a = float(input_value)
    except ValueError:
        a = 0.0

    input_value = input(f"\ndigite 2 numero com ponto: ")
    try:
        b = float(input_value)
    except ValueError:
        b = 0.0

    aux = a
    a = b
    b = aux
    print(f"\na = {a}"
          f"\nb = {b}"
          f"\n")

if __name__ == '__main__':
    prog1ea41()