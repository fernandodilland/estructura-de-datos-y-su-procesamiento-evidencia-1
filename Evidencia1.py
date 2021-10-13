"""
Evidencia #1, Estructura de datos y su procesamiento.

Fernando Dilland Mireles Cisneros.
 Andrea Aracely Cantú Cisneros. """


from collections import namedtuple

print("Bienvenido(a) al negocio de ventas de llantas")

Venta = namedtuple("Venta",["folioUnico","fechaVenta","descripcionArticulo","cantidadPiezasVendidas","precioVenta"])
DiccionarioVentas = {'folioUnico': '1', 'fechaVenta': '12/05/1999'}


while True:
    
    opcion = int(input("Menú de opciones:\n1)Registrar una venta\n2)Consultar una venta\n3)Salir\n> "))
    
    if opcion == 1:
        tamanioDiccionarioVentas = len(DiccionarioVentas)
        print("tamaño es:", tamanioDiccionarioVentas)
        print(dict(DiccionarioVentas['folioUnico']))
    elif opcion == 2:
        True

    elif opcion == 3: # Salida del menú
        break
    
