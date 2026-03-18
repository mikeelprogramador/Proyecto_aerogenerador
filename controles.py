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
    
    def mostrarScalar(self, flag, etiqueta, valor):
        
        #comparacion de medidas, para mostrarlas en pantalla
        if(flag == "km/h"):
            self.velocidadViento = round(float(valor),2)
            etiqueta.configure(text=f"V(viento): {self.velocidadViento} km/h")
        
        elif(flag == "°"):
            self.temperatura = round(float(valor),0)
            etiqueta.configure(text=f"Temperatura: {self.temperatura}°")
            
            
            
    def anguloGiro(self):
           
           
        if self.__Dv == "e":
            #    comparacion de la velocidad del viento, para obtener la velocidad angular 
            if self.velocidadViento >= 25 and self.velocidadViento <= 100:
                self.angulo = op.velocidadAngular(self.velocidadViento)
                
            elif (self.velocidadViento >= 0 and self.velocidadViento <25) or self.velocidadViento > 100 :
            
                if self.angulo > 0:
                    freno = self.angulo * 0.005
                    self.angulo -= freno
                    
                elif self.angulo < 1:
                    self.angulo = 0
                
        else:
            self.angulo -= (self.angulo * 0.007) 
            if self.angulo < 1:
                self.angulo = 0
                    
            
        return self.angulo
    
    
    
    def cambio_direccion(self, direccion):
        self.__Dv = direccion
        
    
    def get_windows(self, window):
        self.ventana = window
        
    def get_canvas(self, canvas):
        self.canvas = canvas
    
    

    def electricidad(self, etiqueta):
        
        ms = 200
        
        #   potencia de la turbina, esta puede cambiar segun el veinto o su temperatura; afectando a la potencia electrica
        potencia_turbina = op.PotenciTurbina(self.velocidadViento,self.temperatura)
                    
        #   potencia eletrica segun el intervalo de tiempo inical y el tiempo de espera, con el tiemo final
        potencia_electrica = op.PotenciaElectrica(potencia_turbina)
        


        if self.__Dv == "e":
            
            #    comparacion de la velocidad del viento, para obtener la energia total  
            if self.velocidadViento >= 25 and self.velocidadViento <= 100:
                #   eenrgia total generada en kwh
                self.energia_total = op.EnergiaTotal(self.tiempoInical,potencia_electrica)
            
            elif (self.velocidadViento >= 0 and self.velocidadViento <25) or self.velocidadViento > 100 :
                
                if self.energia_total > 0:
                    self.energia_total -= (self.energia_total * 0.03)
                    
                elif self.energia_total < 0.1:
                    self.energia_total = 0
                    
                    
        else:
            self.energia_total -= (self.energia_total * 0.03) 
            
            if self.energia_total < 0.1:
                self.energia_total = 0
                
                
        if self.energia_total == 0:
            self.tiempoInical = time.perf_counter()  #   tiempo incial
                
            

        self.canvas.itemconfig(etiqueta, text=f"Energia generada: {round(float(self.energia_total),2)} kwh")
            
        self.ventana.after(ms, self.electricidad, etiqueta)
                
       
                
        
                
    def cambio_color(self, etiqueta):
        
        ms = 500
            
        
        if self.energia_total > 1 and self.energia_total <= 10:
            self.canvas.itemconfig(etiqueta, fill="red")
        
        elif self.energia_total > 10 and self.energia_total <= 30:
            self.canvas.itemconfig(etiqueta, fill="yellow")
            
        elif self.energia_total > 30 and self.energia_total <= 60:
            self.canvas.itemconfig(etiqueta, fill="green")
            
        elif self.energia_total > 60 :
            self.canvas.itemconfig(etiqueta, fill="blue")
            
        elif self.energia_total < 1 :
            self.canvas.itemconfig(etiqueta, fill="white")
            
        self.ventana.after(ms, self.cambio_color, etiqueta)
       
                
                
                
    def animacion_movimiento_aire(self, etiqueta_e, etiqueta_w ):
        
        
        #   sacando la longitud del viento
        # v = int(self.velocidadViento)
        # v = len(str(v))
        
        #   calculando el tiempo segun la velocidad del aire
        #ms = int(self.velocidadViento ) / 100**int(v)
        
        ms = 33
        
        
        
        velocidad_e = 10
        velocidad_w = -10
        
            
        #   extraemos la poscion y el estado de la corriente de aire por izquierda
        x_actual_e, y_actual_e = self.canvas.coords(etiqueta_e)
        estado_actual_e = self.canvas.itemcget(etiqueta_e, "state")
        
        #   extraemos la poscion y el estado de la corriente de aire por derecha
        x_actual_w, y_actual_w = self.canvas.coords(etiqueta_w)
        estado_actual_w = self.canvas.itemcget(etiqueta_w, "state")
        

        
        #   si la direccion es por la izquierda
        if self.__Dv == "e":
            
            #   comprobar si el estado de la corriente de la derecha esta a la vista
            if estado_actual_w != "hidden":
                self.canvas.coords(etiqueta_w, 1100, 300)
                self.canvas.itemconfig(etiqueta_w, state="hidden")

            
            #   comparacion
            if self.velocidadViento > 0:
                
                if estado_actual_e != "normal":
                    self.canvas.itemconfig(etiqueta_e, state="normal")
                    
                #   movemos la imagen de izquerda a derecha  
                self.canvas.move(etiqueta_e, velocidad_e, 0)
                
            if x_actual_e > 1100 or self.velocidadViento < 1:
                
                if estado_actual_e != "hidden":
                    self.canvas.coords(etiqueta_e, 0, 300)
                    self.canvas.itemconfig(etiqueta_e, state="hidden")
                    
                            
        else:
            
            #   comprobar si el estado de la corriente de la izquiera esta a la vista
            if estado_actual_e != "hidden":
                self.canvas.coords(etiqueta_e, 0, 300)
                self.canvas.itemconfig(etiqueta_e, state="hidden")
            
            
            if self.velocidadViento > 0:
                
                if estado_actual_w != "normal":
                    self.canvas.itemconfig(etiqueta_w, state="normal")
                    
                #   movemos la imagen de derecha a izquiera 
                self.canvas.move(etiqueta_w, velocidad_w, 0)
            
            if x_actual_w < 0 or self.velocidadViento < 1:
                
                if estado_actual_w != "hidden":
                    self.canvas.coords(etiqueta_w, 1100, 300)   
                    self.canvas.itemconfig(etiqueta_w, state="hidden")
                    
                        
               
        self.ventana.after(ms, self.animacion_movimiento_aire, etiqueta_e, etiqueta_w)
                    
                
                    
             
                