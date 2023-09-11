def prog1ea32():
    input_value = input(f"\nEntrar com 1 cateto: ")
    try:
        b = float(input_value)
    except ValueError:
        b = 0.0

    input_value = input(f"\nEntrar com 2  cateto: ")
    try:
        c = float(input_value)
    except ValueError:
        c = 0.0

    a = ( (b ** 2.0) + (c ** 2.0) ) ** 0.5

    print(f"\nA hipotenusa e: {(a * b) / 2.0}"
          f"\n")

if __name__ == '__main__':
    prog1ea32()