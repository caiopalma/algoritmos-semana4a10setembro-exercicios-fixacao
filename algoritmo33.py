def prog1ea6():
    input_value = input(f"\n  entre com um numero: ")
    num1 = int(input_value) if input_value.isnumeric() else 0
    input_value = input(f"\n  entre com outro numero: ")
    num2 = int(input_value) if input_value.isnumeric() else 0
    print(f"\n numero 1 : {num1} ")
    print(f"\n numero 2 : {num2} \n")

if __name__ == '__main__':
    prog1ea6()
