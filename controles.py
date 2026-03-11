from operadores import Operations
import time

op = Operations()

class Controladores:
    __Dv = 0 #  Direccion del viento
    
    def __init__(self):
        self.velocidadViento = 0 #  variable predeterminada del viento
        self.temperatura = 0    #  variable predeterminada de la temperatura
        self.energia_total = 0    #  variable predeterminada de la energia total
        self.angulo = 0 #  variable predeterminada de la velocidad gular
    
    def mostrarScalar(self,llave,etiqueta,valor):
        
            #comparacion de medidas, para mostrarlas en pantalla
        if(llave == "km/h"):
            self.velocidadViento = round(float(valor),2)
            etiqueta.configure(text=f"V(viento): {self.velocidadViento} km/h")
        
        if(llave == "°"):
            self.temperatura = round(float(valor),0)
            etiqueta.configure(text=f"Temperatura: {self.temperatura}°")
            
    def anguloGiro(self):
           
        #    comparacion de la velocidad del viento, para obtener la velocidad angular 
        if self.velocidadViento >= 25 and self.velocidadViento <= 100:
            self.angulo = op.velocidadAngular(self.velocidadViento)
            
        if (self.velocidadViento >= 0 and self.velocidadViento <25) or self.velocidadViento > 100 :
            
            if self.angulo > 0:
                freno = self.angulo*0.01
                self.angulo -= freno
                
            if self.angulo < 1:
                self.angulo = 0


        #print("Velocidad angular:",self.angulo)    #   Velocidad angular por milisegundos 
            
        return self.angulo

    def electricidad(self):
        tiempoInical = time.perf_counter()  #   tiempo incial 
        
        while True:
            
            #   potencia de la turbina, esta puede cambiar segun el veinto o su temperatura; afectando a la potencia electrica
            potencia_turbina = op.PotenciTurbina(self.velocidadViento,self.temperatura)
            
            time.sleep(1)   #   tiempo de espera x segundo
                        
            #   potencia eletrica segun el intervalo de tiempo inical y el tiempo de espera, con el tiemo final
            potencia_electrica = op.PotenciaElectrica(potencia_turbina)
            
            #    comparacion de la velocidad del viento, para obtener la energia total  
            if self.velocidadViento >= 25 and self.velocidadViento <= 100:
                #   eenrgia total generada en kwh
                self.energia_total = op.EnergiaTotal(tiempoInical,potencia_electrica)
            
            if (self.velocidadViento >= 0 and self.velocidadViento <25) or self.velocidadViento > 100 :
                
                if self.angulo > 0:
                    self.energia_total -= 0.1
                    
                if self.energia_total < 0.1:
                    self.energia_total = 0

            
            print(self.energia_total)
                
    