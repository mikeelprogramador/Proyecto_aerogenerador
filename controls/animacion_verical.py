from controls.operadores import Operations
import numpy as np

op = Operations()
angulo = 0

def anguloGiro(speed_viento):
    
    global angulo
    #    comparacion de la velocidad del viento, para obtener la velocidad angular 
    if speed_viento >= 25 and speed_viento <= 100:
        rpm = (op.velocidadAngular(speed_viento) * 60) / (2 * np.pi)
        angulo = rpm * 5
        
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
                
    return angulo


def electricidad_vertical (energia_total, speed_viento ,temperatura, tiempo_inical):
    
    max, min = velocidades()

    #   potencia de la turbina, esta puede cambiar segun el veinto o su temperatura; afectando a la potencia electrica
    potencia_turbina = op.PotenciTurbina(speed_viento, temperatura)
                
    #   potencia eletrica segun el intervalo de tiempo inical y el tiempo de espera, con el tiemo final
    potencia_electrica = op.PotenciaElectrica(potencia_turbina)
        
    #    comparacion de la velocidad del viento, para obtener la energia total  
    if speed_viento >= min and speed_viento <= max:
        #   energia total generada en kwh
        energia_total = op.EnergiaTotal(tiempo_inical,potencia_electrica)
    
    #  disminuye la energia total segun la velocidad del vient
    elif (speed_viento >= 0 and speed_viento < min) or speed_viento > max :
        
        if energia_total > 0:
            #/////////////////////////////////////////////////
            #   reduccion de la enerrgia generada, para una mejor animacion
            #   no tiene como una formula matematica, solo es un aproximado
            #////////////////////////////////////////////////
            energia_total -= (energia_total * 0.03)
            
        if energia_total < 0.1:
            energia_total = 0
         
    return energia_total


#   velocidades para los motores
def velocidades():
    velocidad_maxima = 90
    velocidad_minima = 25
    return velocidad_maxima, velocidad_minima