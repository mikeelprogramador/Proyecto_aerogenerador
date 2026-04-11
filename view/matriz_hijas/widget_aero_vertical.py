from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import numpy as np
from controls.aniamciones import Animations
from controls.animacion_verical import anguloGiro

control = Animations()

class Programa_aero_vertical:
    def __init__(self, matrizPadre):
        self.flag = False
        self.ventana = Toplevel(matrizPadre)    #   matriz hija
        self.frame = ttk.Frame(self.ventana)
        self.frame.place(x=0, y=0, relwidth=1, relheight=1)#ajuste del frame para los lados x & y, ocupando el 100% de la pantalla
        self.__styleVentana()
        self.__variablesPrograma()
        self.giro = 0   #   angulo de giro
        self.__lienso()

        
    def __lienso(self):
        #   creando en lienso o canvas
        self.canvas = Canvas(self.ventana, width=360)
        self.canvas.place(relx=0.5,rely=0.5, anchor="center", relwidth=0.75, relheight=1)
        control.get_canvas(self.canvas)
        
        #   inicialisar imagen y tamaño
        self.imgfondo = Image.open("img/fondo_oceano_anocheser.png").resize((1064,1064))
        self.imgTorre = Image.open("img/aero_vertical_torre.png").resize((500,500))
        self.imgCorrienteAire_e = Image.open("img/corriente-aire-e.png").resize((586,400))
        self.imgCorrienteAire_w = Image.open("img/corriente-aire-w.png").resize((586,400))
        self.imgAspas = Image.open("img/aero_vertical_aspas.png").resize((380,380))

        
        #   cargar la imagne con PIL y Tk
        self.imgTk_fondo = ImageTk.PhotoImage(self.imgfondo)
        self.imgTk_torre = ImageTk.PhotoImage(self.imgTorre)
        self.imgTk_corrienteAire_e = ImageTk.PhotoImage(self.imgCorrienteAire_e)
        self.imgTk_corrienteAire_w = ImageTk.PhotoImage(self.imgCorrienteAire_w)
        self.imgTk_aspas = ImageTk.PhotoImage(self.imgAspas)
 
        #   mostrar la imagen en el lienso
        self.img_id_fondo = self.canvas.create_image(450, 500, image=self.imgTk_fondo, anchor="center")
        self.img_id_torre = self.canvas.create_image(480, 450, image=self.imgTk_torre)
        self.img_id_corrienteAire_e = self.canvas.create_image(-200, 300, image=self.imgTk_corrienteAire_e)
        self.img_id_corrienteAire_w = self.canvas.create_image(1100, 300, image=self.imgTk_corrienteAire_w)
        self.img_id_aspas = self.canvas.create_image(485, 335, image=self.imgTk_aspas, anchor="center")
        
        #   estado de la imagen
        self.canvas.itemconfig(self.img_id_corrienteAire_e, state="hidden")
        self.canvas.itemconfig(self.img_id_corrienteAire_w, state="hidden")
        
        #   textos
        self.text_energia = self.canvas.create_text(170,50, text="Energia generada: 0.0 kwh", font=("Arial", 18), fill=("white"))
        
        #   rectangulo
        self.caja_color = self.canvas.create_rectangle(650, 30, 850, 70, fill="white")
    
    
        """_resumen_
        En esta sección están las animaciones de movimiento y cambio de texto 
        """
        
        #    animacion muestra la energia generada
        control.electricidad(self.text_energia, "vertical")
        
        #    animacion cambia de color segun  la energia generada
        control.cambio_color(self.caja_color)
        
        #    animacion movimiento del aire
        control.animacion_movimiento_aire(self.img_id_corrienteAire_e, self.img_id_corrienteAire_w)
        
        #   animacion movimiento para las aspas
        self.__animacion_aspas()

        
        
    def __animacion_aspas(self):
        """_resumen_
        Esta función obtiene la velocidad angular y realiza la “animación /rotación” 
        de las aspas actualizando cada frame
        """
        #   milisegundos
        ms = 33 
        
        dato = self.variableAire.get()
        
        if dato > 0 and not self.flag:
            self.flag = True
            
        #   filtro  del reinico para la animacion
        if self.flag:
            self.velocidadAngular = anguloGiro(control.velocidadViento)

            #   tiempo entre frame
            dt = ms / 1000  
            
            self.giro += self.velocidadAngular * dt

            filtro_giro = self.giro % ( 2 * np.pi)
            
            escala = abs(np.cos(filtro_giro))
            
            nuevo_ancho = int(self.imgAspas.width * escala )
        
            img_transformada = self.imgAspas.resize((max(1, nuevo_ancho), self.imgAspas.height))
            

            self.imgTk_aspas = ImageTk.PhotoImage(img_transformada)
            
            #   actualizar imagen
            self.canvas.itemconfig(self.img_id_aspas, image=self.imgTk_aspas)
            
        else:
            self.canvas.coords(self.img_id_aspas, 485, 335)    

        
        self.canvas.after(ms, self.__animacion_aspas)
        
        
    def __variablesPrograma(self):
        
        """_resumen_
        Valor/Scalar mostrando la lectura de la temperatura
        """
        #   letura del aire
        self.viento = ttk.Label(self.frame, text="V(viento): 0 km/h")
        #   posicion x & y en porcentaje
        self.viento.place(relx=0.02, rely=0.1)
        
        #   valor/scalar del aire
        self.variableAire = ttk.Scale(self.frame, from_=0, to=120, orient="horizontal", 
                                       command= lambda valor: control.mostrarScalar("km/h",self.viento, valor))
        self.variableAire.place(relx=0.02, rely=0.2)
        
        
        """_resumen_
        Valor/Scalar mostrando la lectura de la temperatura
        """
        #   lectura de la temperatura
        self.temperatura = ttk.Label(self.frame,text="Temperatura: 0°")
        #   posicion x & y en porcentaje
        self.temperatura.place(relx=0.02, rely=0.4)
        
        #   valor/scalar de la temperatura
        self.variableTemperatura = ttk.Scale(self.frame, from_=-20,to=100, orient="vertical", 
                                             command= lambda valor: control.mostrarScalar("°",self.temperatura,valor))
        self.variableTemperatura.place(relx=0.05, rely=0.5)
        
        
        """_resumen_
        Lectura de la dirección del aire
        """
        #   texto
        ttk.Label(self.frame, text="Direccion del viento").place(relx=0.02, rely=0.7)
        
        #   lectura de dirracion mediante un boton
        self.izquierda = ttk.Button(self.frame, text="Izquierda", command= lambda: control.cambio_direccion("e"))
        self.izquierda.place(relx=0.035, rely=0.75)
        
        #   lectura de dirracion mediante un boton
        self.derecha = ttk.Button(self.frame, text="derecha", command= lambda: control.cambio_direccion("w"))
        self.derecha.place(relx=0.035, rely=0.8)
        
    
    def reinico(self):
        self.variableAire.set(0)
        self.flag = False
        control.energia_total = 0
        
    def __styleVentana(self):
        self.ventana.title("Simulador Aerogerador Vertical Darrieus")
        self.ventana.geometry("1200x720")
        self.ventana.resizable(False,False) #   Desabilita el agrandamienro de la pantalla
        control.get_windows(self.ventana)
        
        
        
