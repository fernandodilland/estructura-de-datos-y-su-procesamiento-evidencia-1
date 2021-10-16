# Evidencia 1, Estructura de datos y su procesamiento.

from collections import namedtuple
from datetime import datetime

Venta = namedtuple('Ventas', ('descripcion', 'cantidadVenta', 'precioVenta', 'fechaVenta'))
DiccionarioVentas = {}
ListaVentas = []
separador = ('-' * 45)
subtotal = 0

print('Bienvenido(a) al negocio de ventas de llantas')
print(separador)

def Menu():
    opcion = int(input('Menú de opciones:\n[1] Registrar una venta\n[2] Consultar una venta\n[3] Salir\n» '))
    return opcion

def RegistrarVenta():
    ListaVentas=[] # Limpieza de la lista
    print('\n--------- Registro de venta ---------')
    while True:
        folio = int(input(f'Introduzca folio de venta de llanta(s)\n» '))
        if folio in DiccionarioVentas.keys():
            print('Error, ya existe una venta con ese folio de venta')
        else:
            break
    while True:
        descripcion = input('Introduzca descripción del tipo de llanta\n» ')
        cantidadVenta = int(input('Introduzca cantidad a vender del tipo de llanta mencionado\n» '))
        precioVenta = int(input('Introduzca precio (sin iva) del tipo de llanta (por unidad)\n» $'))
        print(separador)
        subtotal = (cantidadVenta * precioVenta)
        print(f'Subtotal (sin iva) de las llantas tipo {descripcion}:','${:.2f}'.format(subtotal))
        print(separador)
        fechaActual = datetime.now()
        fechaActualFormato = fechaActual.strftime('%d/%m/%Y a las %H:%M:%S')
        organizacionVenta = Venta(descripcion,cantidadVenta, precioVenta, fechaActualFormato)
        ListaVentas.append(organizacionVenta)
        DiccionarioVentas[folio] = ListaVentas
        agregaOtraLlantaMismaVenta = int(input('¿Desea agregar otra(s) venta(s) de llanta(s) a la misma venta?\n[1] Si \n[2] No\n» '))
        if agregaOtraLlantaMismaVenta == 2:
            dimensionVentas, acumuladoVentas = 0 , 0
            while dimensionVentas < len(DiccionarioVentas[folio]):
                aculumador = (int(DiccionarioVentas[folio][dimensionVentas].precioVenta) * int(DiccionarioVentas[folio][dimensionVentas].cantidadVenta))
                acumuladoVentas =  aculumador + acumuladoVentas
                dimensionVentas += 1
            print(separador)
            print('Subtotal: ${:.2f}'.format(acumuladoVentas),'\nIVA:','${:.2f}'.format(acumuladoVentas * .16))
            print('-' * 16,'\n\nTotal: ${:.2f}'.format(acumuladoVentas*1.16, 2),f'\nVenta realizada el: {fechaActualFormato}\n')
            print(separador)
            break

def ConsultarVenta():
    consulta = int(input('Folio a consultar: '))
    dimension, totalVentas = 0 , 0
    if consulta in DiccionarioVentas.keys():
        while dimension < len(DiccionarioVentas[consulta]):
            print(separador)
            print(f'Descripción del tipo de llanta: {DiccionarioVentas[consulta][dimension].descripcion}')
            print(f'Cantidad de llantas: {DiccionarioVentas[consulta][dimension].cantidadVenta}')
            print('Precio: ${:.2f}'.format(DiccionarioVentas[consulta][dimension].precioVenta, 2))
            print(f'Fecha: {DiccionarioVentas[consulta][dimension].fechaVenta}')
            totalVentas = (int(DiccionarioVentas[consulta][dimension].precioVenta) * int(DiccionarioVentas[consulta][dimension].cantidadVenta)) + totalVentas
            dimension += 1
        print(separador)
        print('Subtotal: ${:.2f}'.format(totalVentas),'\nIVA:','${:.2f}'.format(totalVentas * .16))
        print('-' * 16,'\n\nTotal: ${:.2f}\n'.format(totalVentas + totalVentas * .16, 2))
        print(separador)
    else:
        print('La clave no esta registrada')

while True:
    opcionElegida = Menu()
    if opcionElegida == 1:
        RegistrarVenta()
    if opcionElegida == 2:
        ConsultarVenta()
    if opcionElegida == 3:
        break
