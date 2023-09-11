import math


def prog1ea38():
    input_value = input(f"\ndigite a altura da lata: ")
    try:
        altura = float(input_value)
    except ValueError:
        altura = 0.0

    input_value = input(f"\ndigite o raio da lata: ")
    try:
        raio = float(input_value)
    except ValueError:
        raio = 0.0

    volume = math.pi * ( raio ** 2.0 ) * altura
    print(f"\no valor da temperatura em graus fahrenheit e = {volume}"
          f"\n")

if __name__ == '__main__':
    prog1ea38()