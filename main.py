#Codigo que que calcula y muestra la distribución de pagos de una empresa
#Definimos la funcion calcular_pagos
def calcular_pagos(num_piezas, precio_unitario):
    # Calcular el monto total de la compra
    monto_total = num_piezas * precio_unitario

# Bloque principal para solicitar datos de entrada y ejecutar la función
n_piezas = int(input("Ingrese el número de piezas a comprar: "))  # Solicitar número de piezas
precio = float(input("Ingrese el precio unitario de cada pieza: "))  # Solicitar precio unitario
calcular_pagos(n_piezas, precio)  # Llamar a la función con los datos ingresados
