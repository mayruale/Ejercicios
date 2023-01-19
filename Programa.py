#Pedir el sueldo por hora del empleado, calcular sueldo mensual (trabaja 8hs por dia) 
#Si no supera el presupuesto estimado ($ 80000) mostrar un mensaje de que esta contratado
#Y si lo supera, mostrar mensaje de que se contrata a medio tiempo (4hs)

sueldoPorHora=int(input("ingrese el sueldo por hora:"))
SueldoMensual=sueldoPorHora*160
print(SueldoMensual)
if SueldoMensual>160000:
    
    print("esta contratado:")
else:
    print ("se contrata por medio tiempo:")