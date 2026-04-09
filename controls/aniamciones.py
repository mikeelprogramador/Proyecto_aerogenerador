from controls.operadores import Operations
import time

op = Operations() # instancia de las operacione


class Animations:
    
    def __init__(self):
        self.__Dv = "e" #  Direccion del viento
        self.velocidadViento = 0 #  variable predeterminada del viento
        self.temperatura = 0    #  variable predeterminada de la temperatura
        self.energia_total = 0    #  variable predeterminada de la energia total
        self.estado_color = ""  #   varible para cambiar el fondo
        self.tiempoInical = 0   
    
    def mostrarScalar(self, flag, etiqueta, valor):
        
        #   actura y lectura de valor/Scalar del viento
        if(flag == "km/h"):
            self.velocidadViento = round(float(valor),2)
            etiqueta.configure(text=f"V(viento): {self.velocidadViento} km/h")
        
        #   actura y lectura de valor/Scalar de la temperatura
        elif(flag == "°"):
            self.temperatura = round(float(valor), 0)
            etiqueta.configure(text=f"Temperatura: {self.temperatura}°")
           
            
      
    #   lectura de la direccion del aire
    def cambio_direccion(self, direccion, flag = False):
        self.__Dv = direccion
        if self.__Dv == "w" and flag :
            self.activate = True
        else:
            self.activate = False
        
    def direction_viento(self):
        return self.__Dv
    
    #   lectura de la ventana en ejecucion
    def get_windows(self, window):
        self.ventana = window
        
    #   lectura del canvas
    def get_canvas(self, canvas):
        self.canvas = canvas
    
    

    def electricidad(self, etiqueta, flag):
        
        ms = 200
        
        if flag == "horizontal":
            from controls.animacion_horizo import electricidad_horizontal
            self.energia_total = electricidad_horizontal(self.energia_total, self.velocidadViento, self.temperatura, self.__Dv, self.tiempoInical)
            salida = round(float(self.energia_total),2)
         
        if flag == "vertical": 
            from controls.animacion_verical import electricidad_vertical
            self.energia_total = electricidad_vertical(self.energia_total, self.velocidadViento, self.temperatura, self.tiempoInical)
            salida = round(float(self.energia_total),2)           
        
        if flag == "ondas":
            from controls.animacion_ondas import electricidad_ondas
            self.energia_total = electricidad_ondas(self.energia_total, self.velocidadViento, self.temperatura, self.tiempoInical) 
            salida = round(float(self.energia_total),5)
                
        #   reinica el tiempo inical si la energia es cero  
        if self.energia_total == 0:
            self.tiempoInical = time.perf_counter()  #   tiempo incial
                
        #   modifica la lectura de la energia total
        self.canvas.itemconfig(etiqueta, text=f"Energia generada: {salida} kwh")
            
        self.ventana.after(ms, self.electricidad, etiqueta,flag)
                
       
                
        
                
    def cambio_color(self, etiqueta):
        
        """_resumen_
        Modificador de color, teniendo en cuanta la energía total generada
        """
        
        ms = 200
            
        
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
        
        #/////////////////////////////////////////
        #   "calculo matematico" 
        #   para la velocidad del movimiento del aire
        #////////////////////////////////////////
        #   sacando la longitud del viento
        # v = int(self.velocidadViento)
        # v = len(str(v))
        
        #   calculando el tiempo segun la velocidad del aire
        #ms = int(self.velocidadViento ) / 100**int(v)
        
        ms = 33
        
        
        
        velocidad_e = 10    #   movimiento en pixeles cuando el viento va hacia la izquierda
        velocidad_w = -10   #   movimiento en pixeles cuando el viento va hacia la derecha
        
            
        #   guardamos posicon x & y de la aniamcion
        x_actual_e, y_actual_e = self.canvas.coords(etiqueta_e)
        estado_actual_e = self.canvas.itemcget(etiqueta_e, "state") #   extracion del estado actual de la animacion
        
        #   guardamos posicon x & y de la aniamcion
        x_actual_w, y_actual_w = self.canvas.coords(etiqueta_w)
        estado_actual_w = self.canvas.itemcget(etiqueta_w, "state") #   extracion del estado actual de la animacion
        

        
        #   animacion del viento si este va hacia la izquierda
        if self.__Dv == "e":
            
            #   comprueba si la animacion opuesta a la derecha esta desactivada
            if estado_actual_w != "hidden":
                self.canvas.coords(etiqueta_w, 1100, 300)   #   regresa la animacion a la posicion original
                self.canvas.itemconfig(etiqueta_w, state="hidden")  #   oculta la animacion

            
            #   animacion del vieto si la velocidad es mayor a cero
            if self.velocidadViento > 0:
                
                #   compruba si la animacion esta activada
                if estado_actual_e != "normal":
                    self.canvas.itemconfig(etiqueta_e, state="normal")  #   activa la animacion
                    
                #   aniamcion del aire, movimiento de izquerda a derecha  
                self.canvas.move(etiqueta_e, velocidad_e, 0)
                
            #   compruba si la animacion supero su limite maximo o la velocidad del viento es mejor a 1
            if x_actual_e > 1100 or self.velocidadViento < 1:
                
                #   verifica si la animacin esta desactivada
                if estado_actual_e != "hidden":
                    self.canvas.coords(etiqueta_e, -200, 300)  #   regresa la animacion a su lugar original
                    self.canvas.itemconfig(etiqueta_e, state="hidden")  #   desaciva la animacion
                    
        #   animacion del viento si este va hacia la derecha                  
        else:
            
            #   comprueba si la animacion opuesta a la izquierda esta desactivada
            if estado_actual_e != "hidden":
                self.canvas.coords(etiqueta_e, -200, 300)  #   regresa la animacion a la posicion original
                self.canvas.itemconfig(etiqueta_e, state="hidden")  #   oculta la animacion
            
            #   animacion del vieto si la velocidad es mayor a cero
            if self.velocidadViento > 0:
                
                #   compruba si la animacion esta activada
                if estado_actual_w != "normal":
                    self.canvas.itemconfig(etiqueta_w, state="normal")  #   activa la animacion
                    
                #   aniamcion del aire, movimiento de derecha a izquierda
                self.canvas.move(etiqueta_w, velocidad_w, 0)
            
             #   compruba si la animacion supero su limite maximo o la velocidad del viento es mejor a 1
            if x_actual_w < -180 or self.velocidadViento < 1:
                
                #   verifica si la animacin esta desactivada
                if estado_actual_w != "hidden":
                    self.canvas.coords(etiqueta_w, 1100, 300)  #   regresa la animacion a su lugar original
                    self.canvas.itemconfig(etiqueta_w, state="hidden")  #   desaciva la animacion
                    
                        
               
        self.ventana.after(ms, self.animacion_movimiento_aire, etiqueta_e, etiqueta_w)
                    
                
                    
             
                