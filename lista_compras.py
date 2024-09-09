lista_compras = []

while True:
    print("\nMenú:")
    print("1. Agregar artículo")
    print("2.Eliminar artículo")
    print("3. Mostrar lista")
    print("4. Salir")

    menu = input("Ingrese una opción: ")

    if menu == '1':
        articulo = input("Ingrese el nombre del artículo: ")
        lista_compras.append(articulo)
        print(f"Artículo '{articulo}' agregado a la lista.")
    elif menu == '2':
        if len(lista_compras) == 0:
            print("La lista de compras está vacía.")
        else:
            print("Lista de compras actual:")
            for i, articulo in enumerate(lista_compras):
                print(f"{i+1}. {articulo}")
            indice = int(input("Ingrese el numero del artículo a eliminar: ")) - 1
            if 0 <= indice < len(lista_compras):
                del lista_compras[indice]
                print("Artículo eliminado.")
            else:
                print("Índice inválido.")
    elif menu == '3':
        if len(lista_compras) == 0:
            print("La lista de compras está vacía.")
        else:
            print("Lista de compras:")
            for articulo in lista_compras:
                print(f"- {articulo}")
    elif menu == '4':
        print("Gracias")
        break
    else:
        print("Opción inválida. Ingrese un número del 1 al 4.")
