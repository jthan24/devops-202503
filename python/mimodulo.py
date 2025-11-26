#GENERAME FUNCIONES DE SUMA, RESTA, MULTIPLICACION, DIVISION Y MODULO Y UNAS EXTRAS BASICAS
def suma(a, b):
    return a + b    

def resta(a, b):
    return a - b    

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"  
      
def modulo(a, b):
    return a % b

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a >= 0:
        return a ** 0.5
    else:
        return "Error: Negative number"
    
def valor_absoluto(a):
    return abs(a)   

def maximo(a, b):
    return max(a, b)

def minimo(a, b):
    return min(a, b)

def promedio(lista):
    if len(lista) == 0:
        return "Error: Empty list"
    return sum(lista) / len(lista)
