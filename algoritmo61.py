def prog1ea34():
    input_value = input(f"\nEntre com o 1o termo: ")
    try:
        termo = int(input_value)
    except ValueError:
        termo = 0

    input_value = input(f"\nEntre com a razao: ")
    try:
        razao = int(input_value)
    except ValueError:
        razao = 0

    quinto = termo * ( razao ** 4 )

    print(f"\nO 5o termo desta P.G. e: {quinto}"
          f"\n")

if __name__ == '__main__':
    prog1ea34()