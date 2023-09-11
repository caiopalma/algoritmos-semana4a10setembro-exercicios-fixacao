import math

def prog1ea47():
    input_value = input(f"\nentre com o salario minimo: ")
    try:
        salmin = float(input_value)
    except ValueError:
        salmin = 0.0

    input_value = input(f"\nentre com o salario da pessoa: ")
    try:
        salpe = float(input_value)
    except ValueError:
        salpe = 0.0

    num = math.inf if salmin == 0.0 else salpe / salmin

    print(f"\na pessoa ganha {num} salarios minimos"
          "\n")

if __name__ == '__main__':
    prog1ea47()