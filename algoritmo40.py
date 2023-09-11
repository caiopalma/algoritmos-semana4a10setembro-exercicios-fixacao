def prog1ea13():
    input_value = input(f"\nentre com o dividendo: ")
    try:
        val1 = int(input_value)
    except ValueError:
        val1 = 0
    input_value = input(f"\nentre com divisor: ")
    try:
        val2 = int(input_value)
    except ValueError:
        val2 = 1.0
    val2 = 1.0 if val2 == 0 else val2
    (quoc, rest) = divmod(val1, val2)
    print(f"\n\n\n"
          f"\ndividendo: {val1}"
          f"\ndivisor: {val2}"
          f"\nquociente: {quoc}"
          f"\nresto: {rest}"
          f"\n")

if __name__ == '__main__':
    prog1ea13()
