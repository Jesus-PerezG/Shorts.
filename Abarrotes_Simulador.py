# Jesús Alejandro Pérez Granados
# Gil Brandon Garcia Contreras

a=0
productos = {"naranja":29,"mandarina":26, "limón":30, "agua":18, "banana":22, "sabritas":23, "lechuga":44, "cereal":80, "pan":140, "coca":36}
productos_list=list(productos)
vendido = []
cliente = 0
salir = 1
while salir != 0:
    salir_a = 1
    salir_c = 1
    while salir_a != 0:
        respuesta_a = int(input("""---------------------------------------------------
- Buen días Kabuto. Gustarías realizar un cambio? -
---------------------------------------------------
1. Agregar producto
2. Eliminar producto
3. Modificar producto
4. Consultar productos
5. No deseo realizar un cambio
6. Terminar dia
---------------------------------------------------
"""))
        c_productos=0
        if respuesta_a == 1:
            for p,c in productos.items():
                c_productos+=1
                print(c_productos,".",p," -  $",c)
            new_p=input("Escribir producto: ")
            new_c=int(input("Elegir precio: "))
            productos[new_p]=new_c
            productos_list=list(productos)
            print(f"{new_p} ha sido agregado con el costo de ${new_c}")
            input("PRESIONA PARA CONTINUAR")
        elif respuesta_a == 2:
            for p,c in productos.items():
                c_productos+=1
                print(c_productos,".",p," -  $",c)
            del_p=input("Escribir nombre de producto a eliminar: ")
            del productos[del_p]
            productos_list=list(productos)
            print(f"{del_p} ha sido eliminado")
            input("PRESIONA PARA CONTINUAR")
        elif respuesta_a == 3:
            for p,c in productos.items():
                c_productos+=1
                print(c_productos,".",p," -  $",c)
            mod_p = input("Escribir nombre de producto a modificar: ")
            mod_c = input("Escribir el nuevo precio: ")
            productos[mod_p] = mod_c 
            print(f"El nuevo valor de {mod_p} es {mod_c}")
            input("PRESIONA PARA CONTINUAR")
        elif respuesta_a == 4:
            print("---------------------------------------------------")
            for p,c in productos.items():
                c_productos+=1
                print(c_productos,".",p," -  $",c)
            input("PRESIONA PARA CONTINUAR")
        elif respuesta_a == 5:
            salir_a = 0
        else:
            salir = 0
            salir_c = 0
            salir_a = 0
    compra = 0
    cliente += 1
    while salir_c != 0:
        print(f"""---------------------------------------------------
----- Bienvenido a Abarrotes Kabuto cliente {cliente} -----
---------------------------------------------------
Productos disponibles:
---------------------------------------------------""")    
        print ("-1. Vaciar carrito\n0 . Terminar compra")
        for p,c in productos.items():
            c_productos+=1
            print(c_productos,".",p," -  $",c)
        respuesta_c = int(input(f"---------------------------------------------------\nCuál deseas comprar? "))
        c_productos=0
        if respuesta_c == -1:
            compra=0
            print("Su carrito esta vacio")
        elif respuesta_c == 0:
            pago=int(input(f"---------------------------------------------------\nEl total de su compra fue {compra}. ¿Con cuánto va a pagar? "))
            if pago>= compra:
                print(f"---------------------------------------------------\nSu cambio es {pago-compra}")
                salir_c = 0
                print("Gracias por su compra\n---------------------------------------------------")
                vendido.append(compra)
            else:
                print("No, mi compa, pague bien. Está viendo cómo esta la cosa.")
        else:
            cantidad_p=int(input("---------------------------------------------------\nCantidad: "))
            for i,p in enumerate(productos_list):
                if i == respuesta_c-1:
                    compra+=productos[p]*cantidad_p
            print("El precio actual de tu compra es:",compra)
        input("PRESIONA PARA CONTINUAR")

ventas=0
d_ventas=0
for i in vendido:
    ventas += 1
    print("Venta",ventas,":",i)
    d_ventas+=i
print(ventas,"Ventas")
print("Total de ventas:",d_ventas)