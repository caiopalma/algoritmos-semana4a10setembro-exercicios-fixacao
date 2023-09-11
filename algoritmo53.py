def prog1ea26():
    input_value = input(f"\nentre com a base: ")
    try:
        a = float(input_value)
    except ValueError:
        a = 0.0

    input_value = input(f"\nentre com a altura: ")
    try:
        b = float(input_value)
    except ValueError:
        b = 0.0

    input_value = input(f"\nentre com a profundidade: ")
    try:
        c = float(input_value)
    except ValueError:
        c = 0.0

    diagonal = ( ( a ** 2.0 ) + (b ** 2.0) + (c ** 2.0) ) ** 0.5

    print(f"\ndiagonal = {diagonal}"
          f"\n")

if __name__ == '__main__':
    prog1ea26()