import math
def prog1ea17():
    input_value = input(f"\nentre com o logaritmando: ")
    try:
        num = float(input_value)
    except ValueError:
        num = 0.0
    input_value = input(f"\nentre com a base: ")
    try:
        base = float(input_value)
    except ValueError:
        base = 0.0
    logaritmo = math.log(num)/math.log(base)
    print(f"\no logaritmo deb: {base} bna baseb:b {logaritmo}"
          f"\n")

if __name__ == '__main__':
    prog1ea17()
