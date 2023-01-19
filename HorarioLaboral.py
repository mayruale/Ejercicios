#Solicitar cantidad de hs trabajadas por dia , 
#si supera la jornada de 8hs informarle que cobra extras
#si no llega a las 8hs informarle que cobra menos
#si completa las 8 hs informarle que cobra normal

horasTrabajadasPorDia=int(input("la cantidad de horas trabajadas por dia es"))
if(horasTrabajadasPorDia>8):
    print ("cobra extras")
elif (horasTrabajadasPorDia==8):
    print ("cobra normal")
else:
    print("cobra menos")
