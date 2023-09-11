import math


def prog1ea31():
    input_value = input(f"\nEntrar com 1 valor: ")
    try:
        xnum1 = float(input_value)
    except ValueError:
        xnum1 = 0

    input_value = input(f"\nEntrar com 2 valor: ")
    try:
        xnum2 = float(input_value)
    except ValueError:
        xnum2 = 0

    input_value = input(f"\nEntrar com 3 valor: ")
    try:
        xnum3 = float(input_value)
    except ValueError:
        xnum3 = 0

    x = xnum1 + ( xnum2 / (xnum3 + xnum1) ) + ( 2.0 * (xnum1 - xnum2) + math.log(64.0) / math.log(2.0) )

    print(f"\nX = {x}"
          f"\n")

if __name__ == '__main__':
    prog1ea31()