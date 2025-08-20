def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    resultado = 0
    resultado = a * b
    return resultado

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def potencia(base, exponente):
    resultado = 1
    for _ in range(exponente):
        resultado *= base
    return resultado

def raiz_cuadrada(numero):
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return numero ** 0.5   

def manejar_error(e):
    print(f"Error: {e}")

# Crear una función para crear un menú con las opciones de la calculadora
def menu():
    print("Calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Salir")
    
    opcion = input("Seleccione una opción (1-7): ")
    return opcion

# Crear una función para ejecutar la calculadora
def ejecutar_calculadora():
    while True:
        opcion = menu()
        
        if opcion == '7':
            print("Saliendo de la calculadora.")
            break
        
        if opcion in ['1', '2', '3', '4', '5']:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
        
        elif opcion == '6':
            numero = float(input("Ingrese un número para calcular su raíz cuadrada: "))
        
        if opcion == '1':
            print(f"Resultado: {suma(a, b)}")
        elif opcion == '2':
            print(f"Resultado: {resta(a, b)}")
        elif opcion == '3':
            print(f"Resultado: {multiplicacion(a, b)}")
        elif opcion == '4':
            try:
                print(f"Resultado: {division(a, b)}")
            except ValueError as e:
                print(e)
        elif opcion == '5':
            print(f"Resultado: {potencia(a, b)}")
        elif opcion == '6':
            try:
                print(f"Resultado: {raiz_cuadrada(numero)}")
            except ValueError as e:
                print(e)
        else:
            print("Opción no válida. Intente de nuevo.")

# Línea para ejecutar la calculadora
if __name__ == "__main__":
    ejecutar_calculadora()


