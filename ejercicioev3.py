import os
import time
import csv
import json
import random

def menu():
    print('------menu-----')
    print('1. Precargar ventas')
    print('2. Crear nueva venta')
    print('3. Reporte de sueldos')    
    print('4. Ver Estadísticas')
    print('5. Salir')

def error():
    os.system('cls')
    print('la opcion ingresada no es valida')
    time.sleep(2)

def guardar_json(file_path, ventas):
    with open(file_path, 'w', encoding='utf-8') as path_ventas:
        json.dump(path_ventas, file_path, indent=4, ensure_ascii=False)

def leer_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file_path:
        return json.load(file_path)
    
def idventas():
    id_venta_mayor=0
    return id_venta_mayor
    

def cargarventas(empleados,ventas,path_ventas):
    id_venta_mayor= idVenta(ventas)
    nuevaVenta = {}
    for i in range(500):
        empleado=random.choice(empleados)
        id_venta_mayor = id_venta_mayor + 1
        id_empleado = empleado["id_vendedor"]
        id_tienda =  empleado["id_tienda"]
        fecha = "04-07-2024"
        total_venta = random.choice(range(100000,300000,100))
        nuevaVenta = {
            "id_venta": id_venta_mayor,
            "empleado": id_empleado,
            "id_tienda": id_tienda,
            "fecha": fecha,
            "total_venta": total_venta
            }
        ventas["ventas"].append(nuevaVenta)
        guardarVentas(path_ventas,ventas)
    os.system('cls')
    print('Ventas agregadas')
    time.sleep(2)

def guardarventas(file_path,ventas):
    guardar_json(file_path,ventas)



def main():
    while True:
        opc1=0
        menu()
        try:
            int(input('ingrese una opcion:'))
        except:
            error()
        if opc1< 0 or opc1> 5:
            error()
        else:
            if opc1==1:
                print('precargar ventas')
                cargarventas(ventas,empleados,path_ventas)
            elif opc1==2:
                print('crear nuevas ventas')
                crearventas(empleados,ventas,path_ventas)
            elif opc1==3:
                print('reporte de sueldo')
                reportesueldo(empleados,ventas,path_ventas)
            elif opc1==4:
                print('ver estadistica')
            elif opc1==5:
                os.system('cls')
                print('salir')
                time.sleep(2)
                break

if __name__=='__main__':
    main()
