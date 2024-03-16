
# Calcular promedio velocidades
def calcular_promedio(velocidades):
    return sum(velocidades) / len(velocidades)

# Evaluar velocidades sobre el promedio
def posiciones_sobre_promedio(velocidades):
    promedio = calcular_promedio(velocidades)
    posiciones = [int for int, any in enumerate(velocidades) if any > promedio]
    return sorted(posiciones)

# Velocidades y posiciones
if __name__ == "__main__":
    velocidad = [25, 12, 19, 16, 11, 11, 24, 1, 14, 14, 16, 10, 6, 23, 13, 25, 4, 19, 14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2, 14, 23, 19, 23, 9, 18, 20, 22, 14, 1, 10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5, 11, 10, 18, 10, 14, 5, 23, 20, 23, 21]
    posiciones = posiciones_sobre_promedio(velocidad)
    
    print(posiciones)
    