def prog1ea29():
    nome = input(f"\nMedida da diagonal maior: ")

    input_value = input(f"\nMedida da diagonal menor: ")
    try:
        idade = int(input_value)
    except ValueError:
        idade = 0

    # a linha abaixo é para dar uma separação entre a entrada e a saída
    print(f"\n\n"
          f"\nnome = {nome}"
          f"\nidade = {idade}")

if __name__ == '__main__':
    prog1ea29()