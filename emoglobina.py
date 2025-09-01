hombre = 1
mujer = 2  

    
genero = int(input())
hemoglobina = float(input())

if int !=1 and genero != 2:
    print("no es posible generar alerta")
elif genero == 1:
    if hemoglobina < 12.2:
        (print("baja"))
    elif hemoglobina <= 16.6:
     print("Normal")
    else:
      print("Alta")
else:
    if hemoglobina < 12.6:
      print("Baja")
    elif hemoglobina <= 15.0:
      print("Normal")
    else:
      print("Alta")