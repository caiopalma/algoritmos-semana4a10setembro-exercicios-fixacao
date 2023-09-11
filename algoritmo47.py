import math
def prog1ea20():
    input_value = input(f"\ndigite saldo: ")
    try:
        num = int(input_value)
    except ValueError:
        num = 0.0
    c = (num / 100)
    d = int(num % 100) / 10
    u = int(num % 10)
    num1 = u*100 + d*10 + c
    print(f"\nnúmero: {num}"
          f"\ninvertido: {num1}"
          f"\n")
    print(f"invertendo os índices da string: {input_value[::-1]}")
if __name__ == '__main__':
    prog1ea20()
