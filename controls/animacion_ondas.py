from controls.operadores import Operations
import numpy as np

op = Operations()
angulo = 0

def anguloGiro(direction_viento, speed_viento):
    
    global angulo
    #   calcula el angulo de giro si la direccion del aire va hacia la izquierda
    if direction_viento == "e":
        #    comparacion de la velocidad del viento, para obtener la velocidad angular 
        if speed_viento >= 25 and speed_viento <= 100:
            rpm = (op.velocidadAngular(speed_viento) * 60) / (2 * np.pi)
            angulo = rpm * 50
            
        #   reduce elangulo de giro segun la velocidad del viento
        elif (speed_viento >= 0 and speed_viento <25) or speed_viento > 100 :
        
            if angulo > 0:
                #/////////////////////////////////////////////////
                #   reduccion del angulo de giro, para una mejor animacion
                #   no tiene como una formula matematica, solo es un aproximado
                #////////////////////////////////////////////////
                freno = angulo * 0.005 
                angulo -= freno
                
            if angulo < 1:
                angulo = 0
                
    #   disminuye el angulo de giro si la direccion del aire va hacia la derecha
    else:
        #/////////////////////////////////////////////////
        #   reduccion del angulo de giro, para una mejor animacion
        #   no tiene como una formula matematica, solo es un aproximado
        #////////////////////////////////////////////////
        angulo -= (angulo * 0.005) 
        if angulo < 1:
            angulo = 0
                
    return angulo


#   velocidades para los motores
def velocidades():
    velocidad_maxima = 0
    velocidad_minima = 0
    return velocidad_maxima, velocidad_minima