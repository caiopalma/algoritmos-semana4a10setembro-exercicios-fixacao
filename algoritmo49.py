import math
def prog1ea22():
    nome = input(f"\nentre com nome: ")
    print(f"\ntodo nome: {nome}"
          f"\nprimeiro caractere: {nome[0]}"
          f"\nultimo caractere: {nome[-1]}"
          f"\nprimeiro ao terceiro caractere: {nome[:3]}"
          f"\nquarto caractere: {nome[3]}"
          f"\ntodos menos o primeiro: {nome[1:]}"
          f"\nos dois últimos: {nome[len(nome)-2:len(nome)]}"
          f"\n")

if __name__ == '__main__':
    prog1ea22()