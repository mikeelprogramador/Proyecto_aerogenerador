import numpy as np
import matplotlib.pyplot as plt

def mostrar_grafica(velocidad, radio):

    if velocidad <= 0:
        print("No hay viento para generar gráfica")
        return

    #llega exactamente hasta la velocidad del slider
    v = np.linspace(0, velocidad, 50)

    r = np.linspace(0.1, radio * 2, 50)

    V, R = np.meshgrid(v, r)

    # convertir km/h -> m/s
    V_ms = V / 3.6
    velocidad_ms = velocidad / 3.6

    # potencia
    P = 0.5 * 1.225 * (np.pi * R**2) * V_ms**3

    # gráfica
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(V, R, P)

    # punto del usuario
    P_usuario = 0.5 * 1.225 * (np.pi * radio**2) * velocidad_ms**3
    ax.scatter(velocidad, radio, P_usuario, s=60)

    ax.set_title("Potencia generada")
    ax.set_xlabel('Velocidad del viento (km/h)')
    ax.set_ylabel('Radio')
    ax.set_zlabel('Potencia (W)')

    plt.show()