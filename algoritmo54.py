def prog1ea27():
    input_value = input(f"\nEntre com a base: ")
    try:
        a = float(input_value)
    except ValueError:
        a = 0.0

    input_value = input(f"\nEntre a altura do um triângulo: ")
    try:
        b = float(input_value)
    except ValueError:
        b = 0.0

    print(f"\nArea = {(a * b) / 2.0}"
          f"\n")

if __name__ == '__main__':
    prog1ea27()