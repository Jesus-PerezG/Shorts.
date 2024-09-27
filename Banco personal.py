# Jesús Alejandro Pérez Granados
# Simulador de banco para usuario

salir=" "
Transacciones=[[],[],[],[],[]]
a=1000
b=50
while salir!="SALIR":
    i=0
    j=0
    transacciones=0
    D=0
    DC=0
    R=0
    RC=0
    C=0
    for index in Transacciones[0]:
        D+=1
    for index in Transacciones[1]:
        DC+=1
    for index in Transacciones[2]:
        R+=1
    for index in Transacciones[3]:
        RC+=1
    for index in Transacciones[4]:
        C+=1
    accion=input("""Bienvenido a tu banco. ¿Qué desea hacer?
    A. Deposita
    B. Retira
    C. Mueve a cuenta de ahorro
    D. Ver Saldo
    E. Ver transacciones
    F. Salir
    """)
    if accion == "A":
        accion1=input("¿Dónde desea depositar?\nA. Saldo\nB. Cuenta de ahorro\n")
        deposito=0
        if accion1=="A":
            deposito=int(input("Cuanto desea depositar? \n"))
            a += deposito
            print("Su nuevo saldo es $", a)
            Transacciones[0].append(deposito)
        if accion1=="B":
            deposito = int(input("Cuanto desea depositar? \n"))
            b += deposito
            print("Su nuevo saldo de la cuenta de ahorro es $", b)
            Transacciones[1].append(deposito)
    if accion == "B":
        accion2 = input("¿De dónde desea retirar?\nA. Saldo\nB. Cuenta de ahorro")
        if accion2 == "A":
            if a > 0:
                retirar = 0
                retirar = int(input("Cuanto desea retirar? \n"))
                if retirar > a:
                    print("Saldo insuficiente $", a)
                else:
                    a = a - retirar
                    print("Su nuevo saldo es $", a)
                    Transacciones[2].append(retirar)
            else:
                print("Saldo insuficiente", a)
        if accion2 == "B":
            retirar = 0
            retirar = int(input("Cuanto desea retirar? \n"))
            if b > 0:
                if retirar > b:
                    print("Saldo de su cuenta de ahorro insuficiente $", b)
                else:
                    b = b - retirar
                    print("Su nuevo saldo de su cuenta de ahorro es $", b)
                    Transacciones[3].append(retirar)
            else:
                print("Saldo insuficiente", b)
    if accion == "C":
        retirar = 0
        retirar = int(input("Cuanto desea mover a la cuenta de ahorro? \n"))
        if a > 0:
            if retirar > a:
                print("Saldo insuficiente $", a)
            else:
                a = a - retirar
                b = b + retirar
                print("Tu saldo es de $", a, "\nEl saldo de la cuenta de ahorro es $", b)
                Transacciones[4].append(retirar)
        else:
            print("Saldo insuficiente", a)
    if accion=="D":
        print("¿Cuál?\nA. Saldo\nB. Cuenta de ahorro\nC. Total de ambos")
        salda=input()
        if salda=="A":
            print("Su saldo es $",a)
        if salda=="B":
            print("Su cuenta de ahorro contiene $",b)
        if salda=="C":
            print("Su total es $",a+b)
    if accion=="E":
        print("""Depósitos:""",D)
        for i, Depositos in enumerate(Transacciones[0]):
            print(i+1,"-",Depositos)
        print("""Depósitos en cuenta de ahorro:""",DC)
        for i, Depositos in enumerate(Transacciones[1]):
            print(i + 1, "-", Depositos)
        print("""Retiros:""",R)
        for i, Retiros in enumerate(Transacciones[2]):
            print(i + 1, "-", Retiros)
        print("Retiros de cuenta de ahorro",RC)
        for i, Retiros in enumerate(Transacciones[3]):
            print(i + 1, "-", Retiros)
        print("""Cambios a Cuenta de ahorro""",C)
        for i, Cambios in enumerate(Transacciones[4]):
            print(i + 1, "-", Cambios)
        print("Transacciones totales:")
        print(D+DC+R+RC+C)
    if accion=="F" or accion=="S" or accion=="SALIR":
        salir="SALIR"
    if salir!="SALIR":
        salir=input("CONTINUAR O SALIR\n")
