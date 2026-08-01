import random
ids = []
nombres = []
tipos = []
rarezas = []
ataques = []
defensas = []
descripciones = []
#--------------------------------------------#
#--|menu_principal_aleatorizador_de_cartas|--#
#--------------------------------------------#
while True:
    print("menu principal aleatorizador de cartas")
    print("1) crear carta")
    print("2) editar carta")
    print("3) eliminar carta")
    print("4) buscar carta")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #-----------------#
    #--|crear_carta|--#
    #-----------------#
    if opcion == "1":
        if len(ids) == 0:
            id_carta = 1
        else:
            id_carta = ids[-1] + 1
        nombre = input("nombre de la carta: ")
        tipo = input("tipo de carta: ")
        rareza = input("rareza: ")
        ataque = int(input("ataque: "))
        defensa = int(input("defensa: "))
        descripcion = input("descripción: ")
        ids.append(id_carta)
        nombres.append(nombre)
        tipos.append(tipo)
        rarezas.append(rareza)
        ataques.append(ataque)
        defensas.append(defensa)
        descripciones.append(descripcion)
        print("carta registrada correctamente.")
        print("id:", id_carta)
    #------------------#
    #--|editar_carta|--#
    #------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar carta")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {tipos[i]} | {rarezas[i]} | {ataques[i]} | {defensas[i]} | {descripciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {nombres[posicion]} | {tipos[posicion]} | {rarezas[posicion]} | {ataques[posicion]} | {defensas[posicion]} | {descripciones[posicion]}")
                nombres[posicion] = input("nuevo nombre de la carta: ")
                tipos[posicion] = input("nuevo tipo de carta: ")
                rarezas[posicion] = input("nueva rareza: ")
                ataques[posicion] = int(input("nuevo ataque: "))
                defensas[posicion] = int(input("nueva defensa: "))
                descripciones[posicion] = input("nueva descripción: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #--------------------#
    #--|eliminar_carta|--#
    #--------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar carta")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {tipos[i]} | {rarezas[i]} | {ataques[i]} | {defensas[i]} | {descripciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {nombres[posicion]} | {tipos[posicion]} | {rarezas[posicion]} | {ataques[posicion]} | {defensas[posicion]} | {descripciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    tipos.pop(posicion)
                    rarezas.pop(posicion)
                    ataques.pop(posicion)
                    defensas.pop(posicion)
                    descripciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #------------------#
    #--|buscar_carta|--#
    #------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar carta")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {nombres[posicion]} | {tipos[posicion]} | {rarezas[posicion]} | {ataques[posicion]} | {defensas[posicion]} | {descripciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            suma = 0
            mayor = ataques[0]
            menor = ataques[0]
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {tipos[i]} | {rarezas[i]} | {ataques[i]} | {defensas[i]} | {descripciones[i]}")
                suma += ataques[i]
                if ataques[i] > mayor:
                    mayor = ataques[i]
                if ataques[i] < menor:
                    menor = ataques[i]
            promedio = suma / len(ids)
            print("estadísticas aleatorizador de cartas")
            print("cantidad de cartas:", len(ids))
            print("ataque total:", suma)
            print("ataque promedio:", round(promedio, 2))
            print("mayor ataque:", mayor)
            print("menor ataque:", menor)
            posicion = random.randint(0, len(ids) - 1)
            print("carta seleccionada aleatoriamente")
            print(f"{ids[posicion]} | {nombres[posicion]} | {tipos[posicion]} | {rarezas[posicion]} | {ataques[posicion]} | {defensas[posicion]} | {descripciones[posicion]}")
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el aleatorizador de cartas.")
        break
    else:
        print("opción no válida.")