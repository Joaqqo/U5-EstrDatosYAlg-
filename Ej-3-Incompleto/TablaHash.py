import numpy as np
#from random import sample,seed
from ListaE import ListaE
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


    def InsertarMALOAAA(self, clave):
        posInicial= self.PosInicial(clave) #Traemos la posición inicial de donde se va a insertar
        posInsercion= self.PosInsercion(posInicial, clave) #Para traer la posición donde se va a insertar
        return posInsercion

    
    def Insertar(self, clave):
        pos=self.PosInicial(clave)
        if self.__datos[pos] == None:
            self.__datos[pos]=ListaE()
        self.__datos[pos].Insertar(clave, 0)
        
    def BuscaClave(self, posicion):
        listaClaves=None
        if posicion >=0 and posicion < self.__claves:
            listaClaves= self.__datos[posicion]
        listaClaves.Recorrer()

    def BuscaPos(self, clave): #Busca la posición
        posInicial= self.PosInicial(clave)
        if self.__datos[posInicial] == None:
            posInicial= -1
            indiceLista= -1
        else:
            indiceLista= self.__datos[posInicial].Buscar(clave)
        return posInicial, indiceLista

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




    def PosInicialDos(self, clave):
        return clave % self.__claves

    def PosInicial(self, clave): #Por método plegado, retorna el índice dentro del arreglo
        claveC=str(clave) #Clave en cadena
        valores=[]
        for i in range(0, len(claveC), 2): #Para pasar de a dos
            if i+1 < len(claveC):
                valores.append(int(claveC[i:i+2])) #Agregaría el valor de i y el que le sigue
            else:
                valores.append(int(claveC[i]))
        posIni= sum(valores) #Suma el valor de los elementos de la lista


        if posIni >= self.__claves: #Por las dudas de que se excedan las listas disponibles
            posIni=self.PosInicialDos(posIni)
        return posIni

    def PosInicialExtraccion(self, clave): #Por método de extracción
        cantDigitos= len(str(self.__claves)) #Cantidad de digitos a extraer = cantidad de digitos de claves
        claveString=str(clave) #Transformamos a string la clave
        posicion= int(claveString[-cantDigitos:]) #Hacemos una "indexación negativa" para extraer los últimos dígitos

        #En caso de que la posición quede fuera del rango de0 a claves-1
        if posicion >= self.__claves:
            posicion= self.PosInicialDos(clave)
        return posicion

    def getDatos(self):
        return self.__datos

    def getClaves(self):
        return self.__claves
