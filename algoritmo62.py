def prog1ea35():
    input_value = input(f"\nEntre com o 1o termo: ")
    try:
        preco = float(input_value)
    except ValueError:
        preco = 0.0

    npreco = preco * 0.91

    print(f"\npreco com desconto: {npreco}"
          f"\n")

if __name__ == '__main__':
    prog1ea35()