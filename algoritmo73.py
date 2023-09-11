import math

def prog1ea46():
    input_value = input(f"\nentre com um numero com parte fracionaria: ")
    try:
        num = float(input_value)
    except ValueError:
        num = 0.0

    numi = int(num)
    numfrac = num - numi
    numa = math.ceil(num) if numfrac >= 0.5 else math.trunc(num)

    print(f"\nparte inteira: {numi}")
    print("\nparte fracionaria {:.3}".format(numfrac + 0.00001))
    print(f"\nnumero arredondado: {numa}"
          "\n")

if __name__ == '__main__':
    prog1ea46()