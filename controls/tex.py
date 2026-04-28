def textos(opc):
    salida = ""
    
    if opc == 0:    #   energia = 0
        salida = """
            Energia nula o muy baja
        """  
        
    if opc == 1:    #   energia > 0.1 kwh
        salida = """
        0.1 kwh o más sirve ~ para:
        💻 Portátil → 2 horas
        📺 TV → 1 hora
        🌬️ Ventilador → 2 horas
        💡 LED → 10 horas
        """
        
    if opc == 2:    #   energia > 0.5 kwh
        salida = """
        0.5 kwh o más sirve ~ para:
        📺 TV → 5–6 horas
        💻 Laptop → 8–10 horas
        🌬️ Ventilador → toda la noche
        ☕ Cafetera → varias veces
        """     
        
    if opc == 3:    #   energia > 1 kwh
        salida = """
        1 kwh o más sirve ~ para:
        💡 Bombillo LED → ~100 horas
        💻 Laptop → 15–20 horas
        📱 ~100 cargas de celular
        🚲 Bicicleta eléctrica → 30–50 km
        """
        
    if opc == 4:    #   energia > 5 kwh
        salida = """
        5 kwh o más sirve ~ para:
        🍳 Cocina eléctrica → varias horas
        🚿 Ducha eléctrica → 1–2 usos 
        🧊 Nevera → 2–5 días
        """
        
    if opc == 5:    #   energia > 10 kwh
        salida = """
        10 kwh o más sirve ~ para:
        🏠 Casa pequeña → 1 día
        🧺 Lavadora y secadora → 1~3 usos
        ❄️ Aire acondicionado → 5–10 horas
        🚗 Auto eléctrico → ~50–70 km
        """
        
    if opc == 6:    #   energia > 20 kwh
        salida = """
        20 kwh o más sirve ~ para:
        🏠 Casa pequeña → 1–2 días
        🏢 Oficina pequeña → 1 día
        🎮 Sala gamer → muchas horas
        🚗 Auto eléctrico → ~100–150 km
        """
        
    if opc == 7:    #   energia > 50 kwh
        salida = """
        50 kwh o más sirve ~ para:
        🏠 Casa → 3–5 días
        🏪 Tienda pequeña → 1–2 días
        🥖 Panadería pequeña → varias horas
        🚗 Auto eléctrico → 250–300 km
        """
        
    if opc == 8:    #   energia > 100 kwh
        salida = """
        100 kwh o más sirve ~ para:
        🏠 Casa → ~1 semana
        🏫 Colegio pequeño → 1 día
        🏋️ Gimnasio → 1 día
        🧊 Cuarto frío pequeño → varias horas
        🎬 Cine pequeño → varias funciones
        """  
        
        
    return salida
        