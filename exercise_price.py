def price():
    """
    Ejercicio 8 - Cálculo de Precio Final

    Dado un precio base, calcular e imprimir:
    1. El monto del impuesto (21%)
    2. El subtotal (precio base + impuesto)
    3. El monto de la propina (10% del subtotal)
    4. El precio final (subtotal + propina)
    """

    preciobase= 100
    impuesto= preciobase * 0.21
    subtotal= preciobase + impuesto
    propina= subtotal *0.1
    preciofinal= subtotal + propina
    print(preciofinal)
    print(subtotal)
    print(preciobase)
    print(impuesto)
    print(propina)
price()
