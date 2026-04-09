import numpy as np
import time

class Operations:
    __radio = 10 #   Radio del rotor o aspas
    __Cp = 0.4 #    Coefiente de potencia
    __Pa = 101325 # Presion absoluta "pascas"(pa)
    __Ca = 287.05 # Constante del aire (J/kj*k)
    __Vp = 6 #  ambda o velocidad de la punta
    __Tk = 273.15 # Grados kelvin
    __Ee = 0.8  #   eficiencia d generador eléctrico y sistemas mecanico
    
    
    def setCp(self, coeficiente):
        self.__Cp = coeficiente 
    
    #   densidad del aire segun la temperatura
    def __densidadAire(self,temperatura):
        temperatura += self.__Tk
        
        return round(float(self.__Pa / (self.__Ca * temperatura ) ),2)
    
    
    
    #    area del rotor/aspas
    def __area(self):
        return round(float(np.pi * (self.__radio**2 ) ),2)
    
    def __aeraCilindro(self):
        diametro = 0.15 
        altura = 3
        return altura * diametro
    
    #  calcula la potenciad el veinto y la potcia de las turbinas
    def PotenciTurbina(self,velocidadV,temperatura, flag = None):
        velocidadV = round(float(velocidadV / 3.6 ),2)   #   comvertir la velocidad de km/h a m/s
        
        densidad = self.__densidadAire(temperatura)
        
        if flag == "cilindro":
            area = self.__aeraCilindro()
        else:
            area = self.__area()
            
        Pv = round(float(0.5 * densidad * area *(velocidadV**3 ) ),2) # Potencia del viento
        Pt = round(float( self.__Cp * Pv ),2) #   Potencia de la turbina
        
        return Pt 
    

    def velocidadAngular(self,VelocidadV):
        VelocidadV = round(float(VelocidadV / 3.6 ),2)
        
        velocidadEnAngulo = round(float((self.__Vp * VelocidadV )/ self.__radio ),2)
        
        velocidadRadianes = np.radians(velocidadEnAngulo)
        
        return velocidadRadianes
    
    
    def PotenciaElectrica(self,potencia_turbina):
        return round(float(potencia_turbina * self.__Ee ),2)
    
    
    def EnergiaTotal(self,tiempoInicial,potencia_electrica):
        tiempoFinal = time.perf_counter()   #   conteo final del intervalo del tiempo
        
        energia_j = potencia_electrica * (tiempoFinal - tiempoInicial ) #   energia genera en joules(J) ó J/s
        energia_kwj = energia_j / 3600000  #   energia generada en kilowatt/hora (kwh)
        
        return  energia_kwj
    
    def vibracion_ondas(self, VelocidadV, tiempoIncial):
        diametro = 0.15
        amplitud = (0.1 + 0.02 * VelocidadV) * diametro
        frecuencia = (0.2 * VelocidadV) /  diametro
        
        tiempoFinal = time.perf_counter()
        deltaTiempo = tiempoFinal - tiempoIncial

        x = amplitud * np.sin(2 * np.pi * frecuencia * deltaTiempo)
        
        print(x)
        return x 
    