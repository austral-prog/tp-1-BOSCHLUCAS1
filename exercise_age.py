def age():
    """
    Ejercicio 10 - Conversión de Edad a Tiempo

    Dada una edad en años, calcular e imprimir:
    1. La edad en meses (1 año = 12 meses)
    2. La edad en días (1 año = 365 días)
    3. La edad en horas (1 día = 24 horas)
    4. La edad en minutos (1 hora = 60 minutos)
    """

    edadanos = 25
    edadmeses = edadanos*12
    edaddias = edadanos*365
    edadhoras = edaddias*24
    edadminutos = edadhoras*60
    print(edadanos)
    print(edadmeses)
    print(edaddias)
    print(edadhoras)
    print(edadminutos)

age()