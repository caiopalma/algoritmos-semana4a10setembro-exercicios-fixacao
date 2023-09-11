import math
def prog1ea25():
    input_value = input(f"\ndigite o lado do quadrado: ")
    try:
        lado = float(input_value)
    except ValueError:
        lado = 0.0

    perimetro = 4.0 * lado
    area = lado ** 2.0
    diagonal = lado * ( 2.0 ** 0.5 )

    print(f"\nperimetro = {perimetro}"
          f"\narea = {area}"
          f"\ndiagonal = {diagonal}"
          f"\n")

if __name__ == '__main__':
    prog1ea25()