import funciones as fn

pedidos = []

while True:
    print("Sistema de pedidos ")
    print("1. registrar pedido")
    print("2. listar los pedidos")
    print("3. imprimir hoja de ruta")
    print("4. salir")

    opcion = int(input("ingrese su opcion: "))

    if opcion == 1:
        fn.registrar_pedido(pedidos)
    elif opcion == 2:
        fn.listar_pedido(pedidos)
    elif opcion == 3:
        fn.imprimir_hoja_ruta(pedidos)
    elif opcion == 4:
        break
    else:
        print("opcion invalida, seleccione nuevamente")
     