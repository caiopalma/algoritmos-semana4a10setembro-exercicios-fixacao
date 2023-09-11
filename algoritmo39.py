def prog1ea12():
    input_value = input(f"\ndigite 1a nota: ")
    try:
        nota1 = float(input_value)
    except ValueError:
        nota1 = 0.0
    input_value = input(f"\ndigite 2a  nota: ")
    try:
        nota2 = float(input_value)
    except ValueError:
        nota2 = 0.0
    media = (nota1 + nota2) / 2.0
    print(f"\nmedia: {media}"
          f"\n")

if __name__ == '__main__':
    prog1ea12()
