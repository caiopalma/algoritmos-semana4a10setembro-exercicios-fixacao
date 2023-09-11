import math
def prog1ea24():
    input_value = input(f"\ndigite raio: ")
    try:
        raio = float(input_value)
    except ValueError:
        raio = 0.0

    perimetro = 2.0 * math.pi * raio
    area = math.pi * (raio ** 2.0)

    print(f"\nperimetro = {perimetro}"
          f"\narea = {area}"
          f"\n")

if __name__ == '__main__':
    prog1ea24()