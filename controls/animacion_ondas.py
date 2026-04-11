from controls.operadores import Operations
import time

op = Operations()
vibracion = 0
tiempoInical = time.perf_counter()

def movimiento_vibracion(speed_viento):
    
    global vibracion, tiempoInical

    #    comparacion de la velocidad del viento, para obtener la velocidad angular 
    if speed_viento >= 11 and speed_viento <= 200:
        vibracion = op.vibracion_ondas(speed_viento, tiempoInical)
        
    #   reduce la vibracion segun la velocidad del viento
    elif (speed_viento >= 0 and speed_viento <11) or speed_viento > 200 :
    
        if vibracion > 0:
            freno = vibracion * 0.005 
            vibracion -= freno
            
        if vibracion < 1:
            vibracion = 0
                
    return vibracion



def electricidad_ondas (energia_total, speed_viento ,temperatura, tiempo_inical):
    
    max, min = velocidades()
    op.setCp(0.2)

    #   potencia de la turbina, esta puede cambiar segun el veinto o su temperatura; afectando a la potencia electrica
    potencia_generador = op.PotenciTurbina(speed_viento, temperatura, "cilindro")
    potencia_generador *= 50
    
    
    #    comparacion de la velocidad del viento, para obtener la energia total  
    if speed_viento >= min and speed_viento <= max:
        #   energia total generada en kwh
        energia_total = op.EnergiaTotal(tiempo_inical,potencia_generador)
    
    #  disminuye la energia total segun la velocidad del vient
    elif (speed_viento >= 0 and speed_viento < min) or speed_viento > max :
        
        if energia_total > 0:
            #/////////////////////////////////////////////////
            #   reduccion de la enerrgia generada, para una mejor animacion
            #   no tiene como una formula matematica, solo es un aproximado
            #////////////////////////////////////////////////
            energia_total -= (energia_total * 0.03)
            
        if energia_total < 0.01:
            energia_total = 0
                
      
    return energia_total


#   velocidades para los motores
def velocidades():
    velocidad_maxima = 120
    velocidad_minima = 11
    return velocidad_maxima, velocidad_minima