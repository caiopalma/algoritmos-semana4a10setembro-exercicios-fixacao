def prog1ea36():
    input_value = input(f"\nhoras trabalhadas: ")
    try:
        na = int(input_value)
    except ValueError:
        na = 0

    input_value = input(f"\nValor da hora-aula: ")
    try:
        vha = float(input_value)
    except ValueError:
        vha = 0.0

    input_value = input(f"\npercentual de desconto: ")
    try:
        pd = float(input_value)
    except ValueError:
        pd = 0.0

    sb = na * vha
    td = ( pd / 100.0 ) * sb
    sl = sb - td

    print(f"\nsalario liquido: {sl}"
          f"\n")

if __name__ == '__main__':
    prog1ea36()