def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

def calcular(operacion, a, b):
    if operacion == "sumar":
        return sumar(a, b)
    elif operacion == "restar":
        return restar(a, b)
    elif operacion == "multiplicar":
        return multiplicar(a, b)
    elif operacion == "dividir":
        return dividir(a, b)
    else:
        return "Operación no válida"
