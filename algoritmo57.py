import math


def prog1ea30():
    input_value = input(f"\ndigite pr1: ")
    try:
        pr1 = float(input_value)
    except ValueError:
        pr1 = 0

    input_value = input(f"\ndigite pr2: ")
    try:
        pr2 = float(input_value)
    except ValueError:
        pr2 = 0

    mf = ( pr1 + pr2 ) / 2.0

    print(f"\nmedia truncada = {int(mf)}"
          f"\nmedia arredondada = {math.ceil(mf)}")

if __name__ == '__main__':
    prog1ea30()