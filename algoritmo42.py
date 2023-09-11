import math
def prog1ea15():
    input_value = input(f"\ndigite um angulo em graus: ")
    try:
        angulo = float(input_value)
    except ValueError:
        angulo = 0.0
    rang = angulo*math.pi/180.0
    print(f"\nseno: {math.sin(rang)}"
          f"\nco-seno: {math.cos(rang)}"
          f"\ntangente: {math.tan(rang)}"
          f"\nco-secante: {1/math.sin(rang)}"
          f"\nsecante: {1/math.cos(rang)}"
          f"\ncotangente: {1/math.tan(rang)}"
          f"\n")

if __name__ == '__main__':
    prog1ea15()
