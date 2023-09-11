import math
def prog1ea16():
    input_value = input(f"\nentre com o logaritmando: ")
    try:
        num = float(input_value)
    except ValueError:
        num = 0.0
    logaritmo = math.log(num)/math.log(10.0)
    print(f"\nlogaritmo: {logaritmo}"
          f"\n")

if __name__ == '__main__':
    prog1ea16()
