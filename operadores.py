import numpy as np

class Operations:
    __radio = 10 #   Radio del rotor o aspas
    __Dv = 0 #  Direccion del viento
    __Cp = 0.4 #    Coefiente de potencia
    __Pa = 101325 # Presion absoluta "pascas"(pa)
    __Ca = 287.05 # Constante del aire (J/kj*k)
    __Vp = 6 #  ambda o velocidad de la punta
    __Tk = 273.15 # Grados kelvin
    
    #   densidad del aire segun la temperatura
    def __densidadAire(self,temperatura):
        temperatura += self.__Tk
        return round(float(self.__Pa/(self.__Ca*temperatura)),2)
    
    #    area del rotor/aspas
    def __area(self):
        return round(float(np.pi*(self.__radio**2)),2)
    
    #  calcula la potenciad el veinto y la potcia de las turbinas
    def PotenciTurbina(self,velocidadV,temperatura):
        densidad = self.__densidadAire(temperatura)
        area = self.__area()
        Pv = round(float(0.5*densidad*area*(velocidadV**3)),2) # Potencia del viento
        return round(float(self.__Cp*Pv),2) #   Potencia de la turbina
    
    #   Velocidad angular
    def velocidadAngular(self,VelocidadV):
        velocidadEnAngulo = round(float((self.__Vp*VelocidadV)/self.__radio),2)
        velocidadRadianes = velocidadEnAngulo * ( 180 / np.pi ) #   Velocidad angular en radianes
        rpm = (velocidadRadianes * 60 ) / 360
        return rpm
    
    
    def PotenciaElectrica():
        pass # Pendiente hacer esta funcion 
    
    def EnergiaTotal():

        pass # Pendiente hacer esta funcion 
