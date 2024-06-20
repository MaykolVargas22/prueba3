  def registrar_pedido():
    nombre_apellido = input("Ingrese nombre y apellido del cliente: ")
    direccion = input("Ingrese dirección del cliente: ")
    sector = input("Ingrese sector del cliente (Centro, Norte, Sur): ")
    paquetes = {}
    while True:
        tipo_paquete = input("Ingrese tipo de paquete (Pequeño, Mediano, Grande): ")
        cantidad = int(input("Ingrese cantidad de paquetes: "))
        paquetes[tipo_paquete] = cantidad 
          
    pedidos.append = [{
        "nombre_apellido": nombre_apellido,
        "direccion": direccion,
        "sector": sector,
        "paquetes": paquetes
    }]
    print("Pedido registrado con éxito!")
    
def listar_pedidos():
    print("Lista de pedidos:")
    for pedido in pedidos:
        print(f"Cliente: {pedido['nombre_apellido']}")
        print(f"Dirección: {pedido['direccion']}")
        print(f"Sector: {pedido['sector']}")
        print("Paquetes:")
        for tipo_paquete, cantidad in pedido["paquetes"].items():
            print(f"  {tipo_paquete}: {cantidad}")
        print()

def imprimir_hoja_ruta():
    sector = input("Ingrese sector para imprimir hoja de ruta (Centro, Norte, Sur): ")
    pedidos_sector = [pedido for pedido in pedidos if pedido["sector"] == sector]
    if pedidos_sector:
        archivo = f"hoja_ruta_{sector}.txt"
        with open(archivo, "w") as f:
            for pedido in pedidos_sector:
                write(f"Cliente: {pedido['nombre_apellido']}\n")
                write(f"Dirección: {pedido['direccion']}\n")
                write(f"Sector: {pedido['sector']}\n")
                write("Paquetes:\n")
                for tipo_paquete, cantidad in pedido["paquetes"].items():
                    write(f"  {tipo_paquete}: {cantidad}\n")
        
        print(f"Archivo {archivo} generado con éxito!")
    else:
        print("No hay pedidos para el sector seleccionado.")
