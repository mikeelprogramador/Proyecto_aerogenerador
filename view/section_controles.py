def window_padre():
    """_resumen_
    Método que instancia y ejecuta la matriz padre
    """
    from .matriz_padre.widget_aero_horizonal import Programa_aero_horizontal
    matriz_padre = Programa_aero_horizontal()
    matriz_padre.ejecucionPorgrama()
    
state_window = False
    
def window_hijas(flag, matrizPadre):
    """_resumen_
    Método que ejecuta las matriz hijas
    """
      
    global state_window 

    #   ventana hija para el aerogenerado vertical
    if flag == "vertical":
        from .matriz_hijas.widget_aero_vertical import Programa_aero_vertical
        
        #  termina la ejecucion el metodo si la ventana esta abierta
        if state_window:
            return
        
        state_window = True
        matriz_hija = Programa_aero_vertical(matrizPadre)
        ventana_hija = matriz_hija.ventana   #   se guarda la matriz hija en un variable 
        
        #//////////////////////////
        #   destruye la ventana hija
        #   reteseando el estado de la ventana para permitir su ejecucion
        #/////////////////////////
        def cerrar():
            global state_window
            state_window = False
            ventana_hija.destroy()   #   destruye la venta 
        
        ventana_hija.protocol("WM_DELETE_WINDOW", cerrar)    #   protocolo que se ejecuta antes de cerrar la ventana
        
        ventana_hija.wait_window() # bloquo del código hasta el cierre de la ventana 
    
    
    #   ventana hija para el aerogenerado de vibraciones
    elif flag == "ondas":
        from .matriz_hijas.widget_aero_ondas import Programa_aero_ondas
        
        #  termina la ejecucion el metodo si la ventana esta abierta
        if state_window:
            return
        
        state_window = True
        matriz_hija = Programa_aero_ondas(matrizPadre)
        ventana_hija = matriz_hija.ventana   #   se guarda la matriz hija en un variable 
        
        #//////////////////////////
        #   destruye la ventana hija
        #   reteseando el estado de la ventana para permitir su ejecucion
        #/////////////////////////
        def cerrar():
            global state_window
            state_window = False
            ventana_hija.destroy()   #   destruye la venta
        
        ventana_hija.protocol("WM_DELETE_WINDOW", cerrar)     #   protocolo que se ejecuta antes de cerrar la ventana
        
        ventana_hija.wait_window()  # bloquo del código hasta el cierre de la ventana 