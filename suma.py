def calcular_velocidad_final(velocidad_inicial, tiempo):   
    g = 9.8    
    velocidad_final = velocidad_inicial + g * tiempo

    return velocidad_final

velocidad_inicial = float(input("Ingresa la velocidad inicial (m/s): "))
tiempo = float(input("Ingresa el tiempo (segundos): "))

velocidad_final = calcular_velocidad_final(velocidad_inicial, tiempo)

print("La velocidad final es:", velocidad_final, "m/s")