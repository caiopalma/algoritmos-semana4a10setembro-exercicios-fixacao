def prog1ea43():
    input_value = input(f"\ndigite numerador: ")
    try:
        cres = float(input_value)
    except ValueError:
        cres = 0.0

    cgorj = cres * 1.1
    print("\nO valor da conta com a gorjeta sera {:.2f}:\n".format(cgorj))

if __name__ == '__main__':
    prog1ea43()