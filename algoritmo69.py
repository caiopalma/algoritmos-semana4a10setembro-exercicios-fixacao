import math
def prog1ea42():
    input_value = input(f"\ndigite numerador: ")
    try:
        num = int(input_value)
    except ValueError:
        num = 0

    input_value = input(f"\ndigite denominador: ")
    try:
        denom = int(input_value)
    except ValueError:
        denom = 1

    print(f"\ndecimal: {float(num/denom)}"
          f"\n")

if __name__ == '__main__':
    prog1ea42()