
def prog1ea49():
    input_value = input(f"\ndigite numero: ")
    try:
        num = int(input_value)
    except ValueError:
        num = 0

    print(f"\nsucessor: {(num + 1) % 61}"
          "\n")

if __name__ == '__main__':
    prog1ea49()