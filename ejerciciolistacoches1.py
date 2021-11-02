lista_coches =[]
while True:
    marca = input("Marca del coche: ")
    if marca == "fin":
        break
    modelo = input("modelo: ")
    combustible = input ("combustible: ")
    cilindrada = input("cilindrada: ")
    linea = {}
    linea["marca coche"] = marca
    linea["modelo"] = modelo
    linea["comustible"] = combustible
    linea["cilindrada"] = cilindrada
    lista_coches.append(linea)

print("lista de coches: \n", lista_coches)
