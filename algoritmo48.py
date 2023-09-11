import math
def prog1ea21():
    input_value = input(f"\nentre com o salário mínimo: ")
    try:
        sm = float(input_value)
    except ValueError:
        sm = 0.0
    input_value = input(f"\nentre com o salário mínimo: ")
    try:
        qtde = float(input_value)
    except ValueError:
        qtde = 0.0
    # divide por 7 para achar o preço de 100 Kw e por 100 para achar de 1 Kw
    preco = (sm / 700.0)
    vp = preco / qtde
    vd = vp * 0.9
    print(f"\npreço do quilowatt: {preco}"
          f"\n valor a ser pago: {vp}"
          f"\n valor com desconto: {vd}"
          f"\n")

if __name__ == '__main__':
    prog1ea21()
