#Codigo que que calcula y muestra la distribución de pagos de una empresa
#Definimos la funcion calcular_pagos
def calcular_pagos(num_piezas, precio_unitario):
    # Calcular el monto total de la compra
    monto_total = num_piezas * precio_unitario

    # Determinar la distribución del pago según el monto total
    if monto_total > 500000:
        inversion_empresa = monto_total * 0.55  # 55% de la empresa
        prestamo_banco = monto_total * 0.30  # 30% del banco
        credito_fabricante = monto_total * 0.15  # 15% al fabricante
    else:
        inversion_empresa = monto_total * 0.70  # 70% de la empresa
        prestamo_banco = 0  # No se solicita préstamo al banco
        credito_fabricante = monto_total * 0.30  # 30% al fabricante


    # Calcular los intereses del crédito al fabricante (20%)
    intereses = credito_fabricante * 0.20
    total_credito_fabricante = credito_fabricante + intereses

    #Mostrar los resultado:
    print("Número de piezas a comprar:", n_piezas)
    print("Precio unitario de cada pieza:", precio_unitario)
    print("Monto total de la compra:", monto_total)
    print("Inversión de la empresa:", inversion_empresa)
    print("Préstamo al banco:", prestamo_banco)
    print("Crédito al fabricante (con intereses):", total_credito_fabricante)




# Bloque principal para solicitar datos de entrada y ejecutar la función
n_piezas = int(input("Ingrese el número de piezas a comprar: "))  # Solicitar número de piezas
precio = float(input("Ingrese el precio unitario de cada pieza: "))  # Solicitar precio unitario
calcular_pagos(n_piezas, precio)  # Llamar a la función con los datos ingresados
