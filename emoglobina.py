hombre = 1
mujer = 2  

    
genero = str(input ("ingrese su genero: "))
hemoglobina = float(input ("ingrese su rango de hemoglobina: "))

if genero ≠ 1 y genero ≠ 2:
    (print("no es posible generar alerta"))
if genero == 1:
    if hemoglobina < 12.2:
        (print("baja"))
    elif hemoglobina <= 16.6:
     (print("Normal"))
    else:
       (print("Alta"))
else:
   if hemoglobina < 12.6:
      (print("Baja"))
    elif hemoglobina <= 15.0:
      (print("Normal"))
    else:
      (print("Alta"))