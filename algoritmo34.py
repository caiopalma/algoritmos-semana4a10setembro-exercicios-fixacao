def prog1ea7():
    input_value = input(f"\n  entre com um numero: ")
    numero = int(input_value) if input_value.isnumeric() else 0
    ant = numero - 1
    suc = numero + 1
    print(f"\no sucessor e b: {suc} b o antecessor e b {ant}")

if __name__ == '__main__':
    prog1ea7()
