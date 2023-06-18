import random




marcas = ["Samsung", "LG", "Bosch", "Whirlpool", "Hisense", "Siemens", "Miele", "Haier", "Neff", "Indesit", "AEG", "Candy", "Hotpoint Ariston", "Zanussi", "Sharp", "Electrolux", "Liebherr", "Panasonic", "Gorenje", "Beko", "Frigidaire", "GE", "Maytag", "KitchenAid", "Fisher & Paykel", "Smeg"]
modelos = ["Edge", "Galaxy", "Note", "Phone", "Ultra", "Hot", "Max", "Pro", "X", "S", "M", "Intelligent"]

def generar_modelo():
    modelo = random.choice(modelos) + " " + str(random.randint(1, 1000))
    return modelo

def generar_producto():
    producto = random.choice(marcas) + " " + random.choice(modelos)
    return producto

num_productos = 100
productos_finales = []
for i in range(num_productos):
    producto_final = generar_producto() + " " + generar_modelo()
    productos_finales.append(producto_final)

print(productos_finales)

with open("test.sql", "w") as file:
    file.write("nuevos_electrodomesticos = [")
    for producto in productos_finales:
        file.write('"' + producto + '"' + "," +"\n")
    file.write("]")
