import random
import faker
from datetime import datetime, timedelta
import time

def generate_random_date():
    start_date = datetime(2013, 1, 1)
    end_date = datetime(2023, 12, 31)
    start_timestamp = time.mktime(start_date.timetuple())
    end_timestamp = time.mktime(end_date.timetuple())
    rand_timestamp = random.uniform(start_timestamp, end_timestamp)
    rand_date = datetime.fromtimestamp(rand_timestamp)
    return rand_date.strftime("%Y-%m-%d")

def generate_receipt():
 f = open("recibos.sql", "w")
 cantidad = 351
 for i in range(cantidad):
    f.write(f"INSERT INTO recibos (id_cliente, id_metodo_pago, fecha) VALUES ({random.randint(1,1045)} , {random.randint(1,6)} , '{generate_random_date()}');\n")

def generate_receipt_product():
    f2 = open("recibos_productos.sql", "w")
    cantidad2 = 250
    for i in range(cantidad2):
        f2.write(f"INSERT INTO recibos_productos (id_recibo, id_producto, cantidad) VALUES ({random.randint(1,351)} , {random.randint(1,566)} , {random.randint(1,50)});\n")

 print("¿Que quieres hacer?")
 print("1. Generar recibos")
 print("2. Generar recibos de productos")
 try:
    opcion = input("Opción: ")
     if opcion == 1:
        generate_receipt()
    elif opcion == 2:
        generate_receipt_product()
    else:
        print("Opción inválida")
except ValueError:
    print("Debes ingresar un número entero como opción")
    
