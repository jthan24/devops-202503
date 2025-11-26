# IMPORTA MI ARCHIVO MIMODULO.PY CON LAS OPERACIONES QUE ESTAN AHI
from mimodulo import suma, resta, multiplicacion, division, modulo
# solicita que ingresen dos numeros y luego usalos con las funciones importadas e imprime resultados
def main():
    try:
        a = float(input("Ingresa el primer numero: "))
        b = float(input("Ingresa el segundo numero: "))
        
        print(f"Suma: {suma(a, b)}")
        print(f"Resta: {resta(a, b)}")
        print(f"Multiplicacion: {multiplicacion(a, b)}")
        print(f"Division: {division(a, b)}")
        print(f"Modulo: {modulo(a, b)}")
    except ValueError:
        print("Error: Por favor ingresa numeros validos.")  


if __name__ == "__main__":
    main()
