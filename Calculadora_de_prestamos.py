# Jesús Alejandro Pérez Granados
# Calculadora de Préstamos

def cuota_fija(capital, tasa, tiempo):
  cuota = capital*(1+tasa)/tiempo
  return cuota
def cuota_decreciente(capital, tasa, tiempo):
  cuota = []
  pago_total = capital
  for i in range (tiempo-2):
    pago_x = pago_total*.35
    cuota.append(pago_x+pago_x*tasa)
    pago_total -= pago_x
  cuota.append(pago_total*.52*(1+tasa))
  pago_total -= pago_total*.52
  cuota.append(pago_total*(1+tasa))
  pago_total -= pago_total
  return cuota
def cuota_creciente(capital, tasa, tiempo):
  list = cuota_decreciente(capital,tasa,tiempo)
  list.reverse()
  return list
def mostrar_resumen_prestamo(resultado, cap, meses):
  if a == 0:
    print(f'Su cuota de préstamo de {cap} a {meses} meses es de: ${resultado} por mes.')
  if a == 1:
    print(f'Su cuota decreciente de préstamo de {cap} a {meses} meses será:')
    for i in range(meses):
      print(f'Mes {i+1} - ${resultado[i]:.2f}')
  if a == 2:
    print(f'Su cuota creciente de préstamo de {cap} a {meses} meses será:')
    for i in range(meses):
      print(f'Mes {i+1} - ${resultado[i]:.2f}')


print('Bienvenido a la Calculadora de Préstamos con Diferentes Tipos de Cuotas.')

tasa = 0.1
while True:
  orden = input('Elige una opción de préstamo:\n0. Salir \n1. Cuota fija\n2. Cuota Decreciente\n3. Cuota Creciente\nContamos con una tasa fija del 10% de interés\n')
  match orden:
    case '0':
      break
    case '1':
      try:
        cap = float(input('Ingresa el capital requerido: '))
        meses = int(input('Ingresa el tiempo en meses enteros: '))
      except:
        print('El número ingresado no fue válido.')
        continue
      if tasa > 0 and meses > 0:
        pass
      else:
        print('La tasa y el tiempo deben ser positivos.')
        continue
      r = cuota_fija(cap, tasa, meses)
      a = 0
      mostrar_resumen_prestamo(r,cap,meses)
    case '2':
      try:
        cap = float(input('Ingresa el capital requerido: '))
        meses = int(input('Ingresa el tiempo en mese enteros: '))
      except:
        print('El número ingresado no fue válido.')
        continue
      if tasa > 0 and meses > 0:
        pass
      else:
        print('La tasa y el tiempo deben ser positivos.')
        continue
      r = cuota_decreciente(cap, tasa, meses)
      a = 1
      mostrar_resumen_prestamo(r, cap, meses)
    case '3':
      try:
        cap = float(input('Ingresa el capital requerido: '))
        meses = int(input('Ingresa el tiempo en mese enteros: '))
      except:
        print('El número ingresado no fue válido.')
        continue
      if tasa > 0 and meses > 0:
        pass
      else:
        print('La tasa y el tiempo deben ser positivos.')
        continue
      r = cuota_creciente(cap, tasa, meses)
      a = 2
      print(r)
      mostrar_resumen_prestamo(r, cap, meses)
    case _:
      print('Ingrese un comando válido')

print('Gracias por usar nuestra calculadora de préstamos.')