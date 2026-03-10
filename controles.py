from operadores import Operations

op = Operations()

class Controladores:
    
    def __init__(self):
        self.velocidadViento = 0 #  variable predeterminada del viento
        self.temperatura = 0    #  variable predeterminada de la temperatura
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
            
        if(self.velocidadViento >= 0 and self.velocidadViento <25) or self.velocidadViento > 100 :
            
            if self.angulo > 0:
                freno = self.angulo*0.01
                self.angulo -= freno
                
            if self.angulo < 1:
                self.angulo = 0


        #print("Velocidad angular:",self.angulo)    #   Velocidad angular por milisegundos 
            
        return self.angulo

                
    