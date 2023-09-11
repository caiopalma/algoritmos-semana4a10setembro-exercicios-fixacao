def prog1ea37():
    input_value = input(f"\ndigite o valor da temperatura em graus centigrados: ")
    try:
        c = float(input_value)
    except ValueError:
        c = 0.0

    f = ( 9.0 * c + 160.0 ) / 5.0
    print(f"\no valor da temperatura em graus fahrenheit e = {f}"
          f"\n")

if __name__ == '__main__':
    prog1ea37()