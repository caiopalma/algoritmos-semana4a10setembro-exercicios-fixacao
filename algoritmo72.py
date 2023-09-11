def prog1ea45():
    input_value = input(f"\nentre com depósito: ")
    try:
        deposito = float(input_value)
    except ValueError:
        deposito = 0.0

    input_value = input(f"\nentre coma taxa de juros: ")
    try:
        taxa = float(input_value)
    except ValueError:
        taxa = 0.0

    valor = deposito * taxa / 100.0
    total = deposito + valor
    print(f"\nRendimentos: {valor}"
          f"\nTotal: {total}"
          "\n")

if __name__ == '__main__':
    prog1ea45()