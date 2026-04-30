import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class grafica:

    def __init__(self, ventana_padre):
        
        self.dato_save_live = False

        # ventana hija
        self.ventana = tk.Toplevel(ventana_padre)
        
        self.ventana.title("Gráfica aerogenerador")
        self.ventana.geometry("900x700")
        self.ventana.resizable(False,False) #   Desabilita el agrandamienro de la pantalla
        

        self.iniciar_grafica()



    def iniciar_grafica(self):

        # figura matplotlib
        self.fig = plt.figure()

        # eje 3D
        self.ax = self.fig.add_subplot(111, projection='3d')

        # integrar matplotlib en tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.ventana)

        self.canvas.draw()

        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        
        

    def datos_grafica(self, velocidad, radio):

        self.ax.clear()

        # datos velocidad
        v = np.linspace(0, velocidad, 50)

        # datos radio
        r = np.linspace(0.1, radio * 2, 50)

        V, R = np.meshgrid(v, r)

        # km/h -> m/s
        V_ms = V / 3.6
        velocidad_ms = velocidad / 3.6

        # potencia
        P = 0.5 * 1.225 * (np.pi * R**2) * V_ms**3

        # superficie
        self.ax.plot_surface(V, R, P)

        # punto usuario
        P_usuario = (0.5 * 1.225 * (np.pi * radio**2) * velocidad_ms**3)

        self.ax.scatter(velocidad, radio, P_usuario, s=60)

        self.ax.set_title("Potencia generada")
        self.ax.set_xlabel('Velocidad del viento (km/h)')
        self.ax.set_ylabel('Radio')
        self.ax.set_zlabel('Potencia (W)')

        # actualizar
        self.canvas.draw()
        



    def save_live(self, etiqueta, canvas):
        
        #   destruye la venta
        def cerrar():
            
            if etiqueta:
                canvas.after_cancel(etiqueta)
            self.ventana.destroy()
                
        
        self.ventana.protocol("WM_DELETE_WINDOW", cerrar)     #   protocolo que se ejecuta antes de cerrar la ventana
        self.ventana.wait_window()  # bloquo del código hasta el cierre de la ventana 
        

        
        
