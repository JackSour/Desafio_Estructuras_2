
# Importar modulo sys
import sys

# Diccionario
precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

# Filtrar productos
def filtrar(umbral, operador='mayor'):
    if operador not in ('mayor', 'menor'):
        print("Lo sentimos, no es una operación válida")
        return
    
# Nuevo diccionario productos filtrados
    resultado = {producto: precio for producto, precio in precios.items() if (operador == 'mayor' and precio > umbral) or (operador == 'menor' and precio < umbral)}
    
# Imprimir resultado productos 
    if not resultado:
        print(f"No hay productos con precios {operador}es al umbral de {umbral}")
    else:
        print(f"Los productos {operador}es al umbral son:", ', '.join(resultado.keys()))

# Verificar script
if __name__ == "__main__":
    if len(sys.argv) == 2:
        umbral = int(sys.argv[1])
        filtrar(umbral)
    elif len(sys.argv) == 3:
        umbral = int(sys.argv[1])
        operador = sys.argv[2].lower()
        filtrar(umbral, operador)
    else:
        print("Por favor, ingrese el valor y opcionalmente el umbral (mayor o menor).")