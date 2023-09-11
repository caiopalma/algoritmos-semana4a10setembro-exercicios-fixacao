import math
def prog1ea23():
    input_value = input(f"\ndigite base: ")
    try:
        base = float(input_value)
    except ValueError:
        base = 0.0

    input_value = input(f"\ndigite altura: ")
    try:
        altura = float(input_value)
    except ValueError:
        altura = 0.0

    perimetro = 2.0 * (base + altura)
    area = base * altura
    diagonal = (base**2.0 + altura**2.0)**0.5

    print(f"\nperimetro = {perimetro}"
          f"\narea = {area}"
          f"\ndiagonal = {diagonal}"
          f"\n")

if __name__ == '__main__':
    prog1ea23()