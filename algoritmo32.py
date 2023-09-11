def prog1ea5():
    input_value = input(f"\n  entre com um numero: ")
    num = int(input_value) if input_value.isnumeric() else 0
    print(f"\n numero : {num} \n")

if __name__ == '__main__':
    prog1ea5()
