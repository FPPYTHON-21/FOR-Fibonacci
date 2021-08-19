import os
def main():
    #escribe tu código abajo de esta línea
    os.system("clear")
    x = 0.5

    print(f"{'x':>8}{'y':>8}{'z':>8}")
    print("------------------------------")

    while x <= 10:
        y = 3 * x ** 2 + 7 * x - 15
        z = y - 2 * x ** 2

        print(f"{x:8.2f}{y:8.2f}{z:8.2f}")

        x += 0.5

if __name__=='__main__':
    main()
