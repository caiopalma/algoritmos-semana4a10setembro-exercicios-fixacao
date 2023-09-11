def prog1ea11():
    input_value = input(f"\n  entre com um numero com ponto: ")
    try:
        num = float(input_value)
    except ValueError:
        num = 0.0
    print(f"\na terça parte e: {num/3.0}"
          f"\n")

if __name__ == '__main__':
    prog1ea11()
