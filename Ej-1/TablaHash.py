import numpy as np

class TablaHash:
    __factorCarga=None
    __claves= None
    __datos= None


    def __init__(self,cantidadClaves,primo=True):
        if primo: #Pregunto si toma en cuenta los números primos o no
            self.__factorCarga = 0.7
            self.__claves = self.EsPrimo(int(cantidadClaves/self.__factorCarga))
        else:
            self.__claves = cantidadClaves
        self.__datos = np.full(self.__claves,None)

    def prueba(self, clave):
        posInicial= self.PosInicial(clave)
        posInsercion=self.PosInsercion(posInicial, clave)

        print(posInicial)
        print(posInsercion)
    def Insertar(self, clave):
        posInicial= self.PosInicial(clave) #Traemos la posición inicial de donde se va a insertar
        posInsercion= self.PosInsercion(posInicial, clave) #Para traer la posición donde se va a insertar

        if posInsercion != -1:
            self.__datos[posInsercion]= clave
        else: #Este sería el peor caso, es decir que recorre todo y no encuentra posición disponible
            print("Error, no existe posición disponible para almacenar la clave ingresada.")

    def BuscaClave(self, posicion):
        if posicion >= 0 and posicion < self.__claves:
            dato= self.__datos[posicion]
        else:
            dato="Error con la posición ingresada."
        return dato

    def BuscaPos(self, clave): #Busca la posición
        posInicial= self.PosInicial(clave)
        posInsercion= self.PosInsercion(posInicial, clave, True) #Lleva el "true" a Posición de inserción para escribir la longitud
        dato= -1

        if posInsercion != -1:
            if self.__datos[posInsercion] == clave:
                dato= posInsercion
        return dato

    def EsPrimo(self, num):
        bandera=False
        while not bandera:
            i=2
            primo= True
            while primo and i < num:
                if num % i == 0:
                    primo= False
                i+=1
            if primo:
                bandera= True
            else:
                num += 1
        return num

    def PosInsercion(self, pos, valor, muestraLong=False): # Retorna la posición donde debe ir el elemento, con prueba lineal
        posIns= -1
        cantP= 0 #Cantidad de pruebas, para cálculo de longitud de la secuencia de prueba

        #Ver lo del if para insertar la clave en un lugar

        while posIns == -1 and cantP < self.__claves:
            if self.__datos[pos] == None or self.__datos[pos] == valor:
                posIns= pos
            else:
                pos= (pos+1)%self.__claves #Cuando pos = clave, entonces dará resto 0 y reseteamos la posicion a 0
                cantP += 1
        if muestraLong: #En caso de que llegue en verdadero, se escribe lo de abajo. Sirve para el punto.
            print("Longitud de la secuencia de prueba: {}" .format(cantP))
        return posIns

    def PosInicial(self, clave): #Por método de la division, retorna el índice dentro del arreglo
        return clave % self.__claves

    def getDatos(self):
        return self.__datos
    def getClaves(self):
        return self.__claves
