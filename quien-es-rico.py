# Validación del nombre
while True:
    nombre = input("Ingrese su nombre: ").strip()
    if nombre and nombre.replace(" ", "").isalpha():
        break
    print("Error: El nombre solo debe contener letras y no puede estar vacío.")

# Validación de la edad
while True:
    edad_input = input("Ingrese su edad (años): ").strip()
    try:
        edad = int(edad_input)
        if 0 < edad <= 120:
            break
        else:
            print("Error: La edad debe estar entre 1 y 120 años.")
    except ValueError:
        print("Error: Debe ingresar un número válido para la edad.")

print(f"Hola, {nombre} tu tienes {edad} años y eres rico")
