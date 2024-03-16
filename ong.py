
# Calcula factorial
def calcular_factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Calcula productoria
def calcular_productoria(lista):
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado

# Controlar factorial y productoria según los argumentos proporcionados
def calcular(**kwargs):  
    for key, value in kwargs.items():
        if 'fact' in key:
            n = int(value)
            print(f"El factorial de {n} es {calcular_factorial(n)}")
        elif 'prod' in key:
            print(f"La productoria de {value} es {calcular_productoria(value)}")
        else:
            print(f"El argumento {key} no es válido")

# Invocar función mediante argumentos especificados
calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)
