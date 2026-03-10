from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from controles import Controladores

control = Controladores()

class ProgramPrincipal:
    def __init__(self):
        self.ventana = Tk()
        self.frame = ttk.Frame(self.ventana)
        self.frame.place(x=0, y=0, relwidth=1, relheight=1)#ajuste del frame para los lados x & y, ocupando el 100% de la pantalla
        self.__styleVentana()
        self.__variablesPrograma()
        self.__lienso()

        
    def __lienso(self):
        self.canvas = Canvas(self.ventana, width=360, bg="blue")
        self.canvas.place(relx=0.5,rely=0.5, anchor="center", relwidth=0.75, relheight=1)
        
        self.imgfondo = Image.open("img/fondo.png").resize((942,1064))
        self.imgTorre = Image.open("img/torreVertical.png").resize((1342,1364))
        self.imgAspas = Image.open("img/aspasVertical.png").resize((621,932)) #   inicialisar imagen y tamaño
        
        self.giro = 0   #   angulo de giro
        
        #   cargar la imagne a Tk
        self.imgTk_fondo = ImageTk.PhotoImage(self.imgfondo)
        self.imgTk_torre = ImageTk.PhotoImage(self.imgTorre)
        self.imgTk_aspas = ImageTk.PhotoImage(self.imgAspas)
 
        #   mostrar la imagen una sola vez en canvas 
        self.img_id_fondo = self.canvas.create_image(450, 500, image=self.imgTk_fondo, anchor="center")
        self.img_id_torre = self.canvas.create_image(500, 500, image=self.imgTk_torre)
        self.img_id_aspas = self.canvas.create_image(498, 260, image=self.imgTk_aspas, anchor="center")       

        self.rotar()
        

        
    def rotar(self):
        ms = 16 #   milisegundos
        
        velocidadAngular = control.anguloGiro()
        
        dt = ms / 1000  #   Tiempo entre frame
        
        self.giro += velocidadAngular * dt
        
        rotacionImg = self.imgAspas.rotate(self.giro, expand=TRUE)  #   rotacion de la imagen
        self.imgTk_aspas = ImageTk.PhotoImage(rotacionImg)    #   
        
        #Actualizar imagen
        self.canvas.itemconfig(self.img_id_aspas, image=self.imgTk_aspas)
        
        #print(self.giro)   #   el numero de giro por los milisegundos
        
        self.canvas.after(ms, self.rotar)   #   Ejecucion de la funcion por los milisegundos
        
    def __variablesPrograma(self):
        
        self.viento = ttk.Label(self.frame, text="V(viento): 0 km/h")
        self.viento.place(relx=0.02, rely=0.1) #posicion x & y en porcentaje
        
        self.variableAire = ttk.Scale(self.frame, from_=0, to=120, orient="horizontal", 
                                       command= lambda valor: control.mostrarScalar("km/h",self.viento, valor))
        self.variableAire.place(relx=0.02, rely=0.2)
        
        self.temperatura = ttk.Label(self.frame,text="Temperatura: 0°")
        self.temperatura.place(relx=0.02, rely=0.4)
        
        self.variableTemperatura = ttk.Scale(self.frame, from_=-20,to=100, orient="vertical", 
                                             command= lambda valor: control.mostrarScalar("°",self.temperatura,valor))
        self.variableTemperatura.place(relx=0.05, rely=0.5)
        
        ttk.Label(self.frame, text="Direccion del viento").place(relx=0.02, rely=0.7)
        
        self.izquierda = ttk.Button(self.frame, text="Izquierda")
        self.izquierda.place(relx=0.035, rely=0.75)
        
        self.derecha = ttk.Button(self.frame, text="derecha")
        self.derecha.place(relx=0.035, rely=0.8)
        
        #Botones para cambiar el esenario
        """"falta realizar la implementacion del cambio de esenario"""
        
        self.boton1 = ttk.Button(self.frame, text="Boton1")
        self.boton1.place(relx=0.9, rely=0.1)
        
        self.boton2 = ttk.Button(self.frame, text="Boton2")
        self.boton2.place(relx=0.9, rely=0.3)
        
        self.boton3 = ttk.Button(self.frame, text="Boton3")
        self.boton3.place(relx=0.9, rely=0.5)
        
        self.boton4 = ttk.Button(self.frame, text="Boton4")
        self.boton4.place(relx=0.9, rely=0.7)
        
    def __styleVentana(self):
        self.ventana.title("Simulador")
        self.ventana.geometry("1200x720")
        self.ventana.resizable(False,False)#Desabilita el agrandamienro de la pantalla
        
    def EjecucionPorgrama(self):
        self.ventana.mainloop()
        
        
