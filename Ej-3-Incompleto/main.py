from TablaHash import TablaHash
from random import randint, seed
import os




def menu(tabla, acum, cont):
    salir = False
    opcion = 0
    while not salir:
        print('\n----------------------MENU DE OPCIONES---------------------')
        print('\n 1-Cargar tabla')
        print('\n 2-Mostrar tabla')
        print('\n 3-Buscar clave')
        print('\n 4- Salir')
        opcion = int(input('\n Ingrese una OPCION: '))
        if(opcion == 1):
            seed(10) #Seed sirve para que siempre den los mismos valores
            claves=[] #La uso para evitar valores repetidos
            for i in range(cantClaves):
                nclave= randint(4000,9000)
                while nclave in claves:
                    nclave= randint(4000,9000)
                claves.append(nclave)
                tabla.Insertar(nclave)
            print("TABLA CARGADA EXITOSAMENTE")
#-----------------------------------------------------------------------------------
        if(opcion == 2):
            #acum=0
            #cont=0
            datos=tabla.getDatos()
            for i in range(len(datos)):
                if datos[i] !=None:
                    print("{} - {} - {}" .format(i, datos[i].Elementos(), datos[i].Tamanio()))
                    acum += datos[i].Tamanio()
                    cont += 1
                else:
                    print("{} - {}" .format(i, datos[i]))
            print(acum)
            print(cont)
#-----------------------------------------------------------------------------------
        if(opcion == 3):
            clave=int(input("Ingrese la clave a buscar:  "))
            pos=tabla.BuscaPos(clave)
            if pos == -1:
                print("Error con la posición ingresada.")
            else:
                print("Posición: {} y su índice en la lista: {}" .format(pos[0], pos[1]))
#-----------------------------------------------------------------------------------
        if(opcion == 4):
            print("EN CONTSTRUCCIÓN")
            datos=tabla.getDatos()
            promedio= acum // cont
            cantListas=0
            for i in range(len(datos)):
                if datos[i] != None:
                    if datos[i].Tamanio() <= promedio+3 and datos[i].Tamanio() >= promedio-3:
                        cantListas+=1
            print("Longitud promedio de las listas: {} " .format(promedio))
            print("Cantidad de listas que registran una longitud que varía hasta 3 unidades: {} " .format(cantListas))
#-----------------------------------------------------------------------------------
        if(opcion == 5):
            print("\n FINALIZA EL PROGRAMA \n")
            salir = True
        os.system('cls')

if __name__ == '__main__':
    cantClaves=1000
    tabla=None
    print("1-El tamaño de la tabla Hash no es un número primo.")
    print("2-El tamaño de la tabla Hash sí es un número primo.")
    siono=int(input("Elija:  "))
    while siono < 1 or siono > 2:
        print("ERROR, por favor elija 1 o 2")
        siono=int(input("Elija:  "))

    if siono == 1:
        tabla= TablaHash(cantClaves, False)
    elif siono == 2:
        tabla= TablaHash(cantClaves)

    menu(tabla,0,0)

