
class Operadores:
    
    def mostrarScalar(llave,etiqueta,valor):
        if(llave == "km/h"):
            etiqueta.configure(text=f"V(viento): {float(valor):.2f} km/h")
        if(llave == "°"):
            etiqueta.configure(text=f"Temperatura: {float(valor):.0f}°")