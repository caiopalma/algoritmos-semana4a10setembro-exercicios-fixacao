def prog1ea33():
    input_value = input(f"\nEntrar com o 1o termo: ")
    try:
        termo = int(input_value)
    except ValueError:
        termo = 0

    input_value = input(f"\nEntrar com a razao: ")
    try:
        razao = int(input_value)
    except ValueError:
        razao = 0

    dec = termo + (9.0 * razao)

    print(f"\nO 10 termo desta P.A. e: {dec}"
          f"\n")

if __name__ == '__main__':
    prog1ea33()