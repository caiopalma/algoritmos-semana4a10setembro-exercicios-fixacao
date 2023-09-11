import math
def prog1ea19():
    input_value = input(f"\ndigite saldo: ")
    try:
        saldo = float(input_value)
    except ValueError:
        saldo = 0.0
    nsaldo = saldo * 1.01
    print(f"\nnovo saldo: {nsaldo}"
          f"\n")

if __name__ == '__main__':
    prog1ea19()
