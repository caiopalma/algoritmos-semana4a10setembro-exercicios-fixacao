
def prog1ea48():
    input_value = input(f"\nentre com seu peso, só a parte inteira: ")
    try:
        peso = int(input_value)
    except ValueError:
        peso = 0

    pesogramas = peso * 1000
    novopeso = pesogramas * 1.12

    print(f"\npeso em gramas: {pesogramas}"
          f"\nnovo peso: {novopeso}"
          "\n")

if __name__ == '__main__':
    prog1ea48()