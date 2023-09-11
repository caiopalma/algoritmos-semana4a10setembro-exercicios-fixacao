def prog1ea28():
    input_value = input(f"\nMedida da diagonal maior: ")
    try:
        diagmaior = float(input_value)
    except ValueError:
        diagmaior = 0.0

    input_value = input(f"\nMedida da diagonal menor: ")
    try:
        diagmenor = float(input_value)
    except ValueError:
        diagmenor = 0.0

    area = (diagmaior * diagmenor) / 2.0

    print(f"\narea = {area}"
          f"\n")

if __name__ == '__main__':
    prog1ea28()