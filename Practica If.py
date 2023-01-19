#En el if se usan mucho los operadores > y < 
#Pedir el sueldo por dia del usuario , calcular sueldo mensual (trabaja 6 dias por semana) 
# y mostrar si el sueldo total supera el minimo (60000) o no es suficiente 

sueldoPorDia=int(input("el sueldo por dia es"))
sueldoMensual=24*sueldoPorDia
print("el suelto total es", sueldoMensual)
if (sueldoMensual >= 60000):
    print ("el sueldo total supera el minimo")
else:
    print("no supera el minimo")



