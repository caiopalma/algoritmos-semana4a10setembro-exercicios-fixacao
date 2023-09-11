def prog1ea9():
    input_value = input(f"\n  entre com um numero: ")
    num1 = int(input_value) if input_value.isnumeric() else 0
    input_value = input(f"\n  entre com outro numero: ")
    num2 = int(input_value) if input_value.isnumeric() else 0
    soma = num1 + num2
    print(f"\nSoma: {soma}\n")

if __name__ == '__main__':
    prog1ea9()
