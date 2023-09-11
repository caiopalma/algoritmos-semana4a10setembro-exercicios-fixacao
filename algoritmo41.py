def prog1ea14():
    input_value = input(f"\nentre com 1 numero: ")
    try:
        a = float(input_value)
    except ValueError:
        a = 0.0
    input_value = input(f"\nentre com 2 numero: ")
    try:
        b = float(input_value)
    except ValueError:
        b = 0.0
    input_value = input(f"\nentre com 3 numero: ")
    try:
        c = float(input_value)
    except ValueError:
        c = 0.0
    input_value = input(f"\nentre com 4 numero: ")
    try:
        d = float(input_value)
    except ValueError:
        d = 0.0
    mp = (a*1 + b*2 + c*3 + d*4)/10.0
    print(f"\nmedia ponderada: {mp}"
          f"\n")

if __name__ == '__main__':
    prog1ea14()
