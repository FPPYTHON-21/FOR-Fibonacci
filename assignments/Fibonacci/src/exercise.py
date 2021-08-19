import os
def main():
    #escribe tu código abajo de esta línea
    os.system("clear")
    
    print('El sistema te arroba el valor de la serie de Fibonacci de 3 en adelante')
    print('=======================================================================')
    valor=int(input("Dame el número de la secuencia que buscas: "))
    
    Primero = 0
    Segundo = 1
    Tercero = 0
    
    if valor>2 and valor<100:
        for n in range(2,valor+1):
            Tercero = Primero + Segundo
        
            if n==valor:
                print('El valor que buscas es:'+ str(Tercero))


            Primero = Segundo
            Segundo = Tercero
    elif valor<=2:
        print('Por desgracia no se aclaro que era de TRES! en adelante')
    elif valor>100:
        print('Tampoco te pases')    


if __name__=='__main__':
    main()
