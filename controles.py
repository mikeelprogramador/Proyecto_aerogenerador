from operadores import Operations
import time

op = Operations()


class Controladores:
    
    def __init__(self):
        self.__Dv = "e" #  Direccion del viento
        self.velocidadViento = 0 #  variable predeterminada del viento
        self.temperatura = 0    #  variable predeterminada de la temperatura
        self.energia_total = 0    #  variable predeterminada de la energia total
        self.estado_color = ""  #   vaable para cambiar el fondo
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
           
           
        if self.__Dv == "e":
            #    comparacion de la velocidad del viento, para obtener la velocidad angular 
            if self.velocidadViento >= 25 and self.velocidadViento <= 100:
                self.angulo = op.velocidadAngular(self.velocidadViento)
                
            if (self.velocidadViento >= 0 and self.velocidadViento <25) or self.velocidadViento > 100 :
            
                if self.angulo > 0:
                    freno = self.angulo * 0.005
                    self.angulo -= freno
                    
                if self.angulo < 1:
                    self.angulo = 0
                
        else:
            self.angulo -= (self.angulo * 0.007) 
            if self.angulo < 1:
                self.angulo = 0
                    



        #print("Velocidad angular:",self.angulo)    #   Velocidad angular por milisegundos 
            
        return self.angulo

    def electricidad(self,etiqueta_canvas = None, etiqueta = None):
        tiempoInical = time.perf_counter()  #   tiempo incial 
        
        while True:
            
            #   potencia de la turbina, esta puede cambiar segun el veinto o su temperatura; afectando a la potencia electrica
            potencia_turbina = op.PotenciTurbina(self.velocidadViento,self.temperatura)
            
            time.sleep(1)   #   tiempo de espera x segundo
                        
            #   potencia eletrica segun el intervalo de tiempo inical y el tiempo de espera, con el tiemo final
            potencia_electrica = op.PotenciaElectrica(potencia_turbina)
    
    
            if self.__Dv == "e":
                #    comparacion de la velocidad del viento, para obtener la energia total  
                if self.velocidadViento >= 25 and self.velocidadViento <= 100:
                    #   eenrgia total generada en kwh
                    self.energia_total = op.EnergiaTotal(tiempoInical,potencia_electrica)
                
                if (self.velocidadViento >= 0 and self.velocidadViento <25) or self.velocidadViento > 100 :
                    
                    if self.energia_total > 0:
                        self.energia_total -= (self.energia_total * 0.1)
                        
                    if self.energia_total < 0.1:
                        self.energia_total = 0
                        
            else:
                self.energia_total -= (self.energia_total * 0.1) 
                if self.energia_total < 0.1:
                    self.energia_total = 0
                    

            if etiqueta_canvas != None:
                etiqueta_canvas.itemconfig(etiqueta, text=f"Energia generada: {round(float(self.energia_total),2)} kwh")
                
                
                
    def cambio_direccion(self, direccion):
        self.__Dv = direccion
        
        if direccion == "e":
            pass
            
        
        
                
    def cambio_color(self, etiqueta_canvas = None, etiqueta = None):
        
        while True:
            
            time.sleep(1)
            
            if self.energia_total > 1 and self.energia_total <= 10:
                etiqueta_canvas.itemconfig(etiqueta, fill="red")
            
            elif self.energia_total > 10 and self.energia_total <= 30:
                etiqueta_canvas.itemconfig(etiqueta, fill="yellow")
                
            elif self.energia_total > 30 and self.energia_total <= 60:
                etiqueta_canvas.itemconfig(etiqueta, fill="green")
                
            elif self.energia_total > 60 :
                etiqueta_canvas.itemconfig(etiqueta, fill="blue")
                
            elif self.energia_total < 1 :
                etiqueta_canvas.itemconfig(etiqueta, fill="white")
       
                
    def movimiento_aire(self, etiqueta_canvas, etiqueta ):
        etiqueta_canvas.itemconfig(self.img_id_corrienteAire, state="normal")