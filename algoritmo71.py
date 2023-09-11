def prog1ea44():
    input_value = input(f"\nentre com hora atual: ")
    try:
        hora = int(input_value)
    except ValueError:
        hora = 0

    input_value = input(f"\nentre com minutos: ")
    try:
        minuto = int(input_value)
    except ValueError:
        minuto = 0

    tminuto = (hora * 60) + minuto
    print(f"\nAte agora se passaram: {tminuto} minutos"
          "\n")

if __name__ == '__main__':
    prog1ea44()