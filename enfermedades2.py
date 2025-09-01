n = int(input())  # Número de personas a evaluar

h_baja = 0
h_alta = 0
h_normal = 0
m_baja = 0
m_alta = 0
m_normal = 0

for _ in range(n):
    hb = float(input("Ingrese nivel de hemoglobina: "))
    genero = int(input("Ingrese género (1 = hombre, 2 = mujer): "))

    while genero not in (1, 2):
        genero = int(input("Género inválido. Ingrese 1 (hombre) o 2 (mujer): "))

    if genero == 1:  # Hombre
        if hb < 12.2:
            h_baja += 1
        elif hb <= 16.6:
            h_normal += 1
        else:
            h_alta += 1
    else:  # Mujer
        if hb < 12.6:
            m_baja += 1
        elif hb <= 15:
            m_normal += 1
        else:
            m_alta += 1

print(h_baja, h_alta, h_normal, m_baja, m_alta, m_normal)