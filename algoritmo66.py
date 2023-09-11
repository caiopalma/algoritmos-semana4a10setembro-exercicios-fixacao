import math
def prog1ea39():
    input_value = input(f"\ndigite o tempo gasto: ")
    try:
        tempo = float(input_value)
    except ValueError:
        tempo = 0.0

    input_value = input(f"\ndigite a velocidade media: ")
    try:
        vel = float(input_value)
    except ValueError:
        vel = 0.0

    dist = tempo * vel
    litros = dist / 12.0

    print(f"\nvelocidade = {vel},"
          f"\ntempo = {tempo}, "
          f"\ndistancia = {dist},"
          f"\nlitros = {litros}"
          f"\n")

if __name__ == '__main__':
    prog1ea39()